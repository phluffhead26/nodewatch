#!/usr/bin/env python3
"""NodeWatch data fetcher. Sources: api.comfy.org registry, ComfyUI-Manager custom-node-list.json,
GitHub commits.atom feeds + raw pyproject.toml (no API quota), GitHub REST issues API (unauthenticated
unless `gh` is logged in; 60 req/h, cached + rotated across runs)."""
import json, os, re, sys, time, subprocess, urllib.request, urllib.error, tomllib, concurrent.futures as cf
from datetime import datetime, timezone, timedelta
D = os.path.join(os.path.dirname(__file__), '..', 'data'); os.makedirs(D, exist_ok=True)
# Error-spike rule (documented on the About page)
HIST_DAYS = 210            # recent 30 days + ~6-month (180-day) baseline
SPIKE_MIN = 3              # at least 3 error-titled issues opened in the last 30 days
SPIKE_BASELINE_X = 2.0     # and >= 2x the pack's own average 30-day rate over the prior 180 days (floor 1/month)
SPIKE_PER100K = 0.5        # and >= 0.5 error issues per 100K registry downloads in 30 days (~3x the median monthly rate across tracked packs)
TOP = int(os.environ.get('NW_TOP', 300)); NOW = datetime.now(timezone.utc)
UA = {'User-Agent': 'NodeWatch/0.1 (local prototype)'}
def get(url, hdr=None, raw=False, timeout=30):
    r = urllib.request.Request(url, headers={**UA, **(hdr or {})})
    with urllib.request.urlopen(r, timeout=timeout) as f:
        b = f.read(); return (b.decode('utf-8', 'replace') if raw else json.loads(b)), f.headers
def load(n, d):
    p = os.path.join(D, n); return json.load(open(p)) if os.path.exists(p) else d
def save(n, o): json.dump(o, open(os.path.join(D, n), 'w'), indent=1, default=str)

# 1. registry
nodes, page = [], 1
while True:
    for attempt in range(5):
        try: j, _ = get(f'https://api.comfy.org/nodes?page={page}&limit=100', timeout=60); break
        except Exception as e: print('registry error', page, attempt, e); time.sleep(5 * (attempt + 1))
    else: sys.exit(f'registry fetch failed at page {page}; aborting so a partial list is not published')
    nodes += j.get('nodes', []); print(f'registry page {page}/{j.get("totalPages")}', file=sys.stderr)
    if page >= j.get('totalPages', 0): break
    page += 1
save('registry_raw.json', nodes)
try:
    mgr, _ = get('https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json')
    mgr = mgr.get('custom_nodes', [])
except Exception as e: print('manager list error', e); mgr = []
mgr_repos = {re.sub(r'\.git$', '', (m.get('reference') or '').lower().rstrip('/')) for m in mgr}

def gh_repo(u):
    m = re.match(r'https?://github\.com/([^/\s]+)/([^/\s#?]+)', u or '')
    return f'{m[1]}/{re.sub(r"\.git$", "", m[2])}' if m else None
cands = [n for n in nodes if gh_repo(n.get('repository'))]
cands.sort(key=lambda n: n.get('downloads') or 0, reverse=True)
top = cands[:TOP]

# auth mode
TOKEN = None
try:
    TOKEN = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, timeout=10).stdout.strip() or None
except Exception: pass
TOKEN = TOKEN or os.environ.get('GITHUB_TOKEN')
AUTH = {'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}
mode = 'gh-authenticated' if TOKEN else 'unauthenticated (60 req/h)'

cache = load('gh_cache.json', {})
ERR = re.compile(r'\b(error|errors|broken|break|breaks|fail|fails|failed|failing|crash|exception|traceback|not working|doesn.?t work|import failed|incompatib)', re.I)

def atom(repo):
    """Last commit via git (no API quota): newest commit across default branch + main/master."""
    import tempfile
    env = {**os.environ, 'GIT_TERMINAL_PROMPT': '0'}
    try:
        o = subprocess.run(['git', 'ls-remote', '--symref', f'https://github.com/{repo}', 'HEAD', 'refs/heads/main', 'refs/heads/master'],
                           capture_output=True, text=True, timeout=40, env=env)
        if o.returncode != 0 or not o.stdout.strip(): return {'atom_error': 404}
        m = re.search(r'ref: refs/heads/(\S+)\s+HEAD', o.stdout); br = m[1] if m else None
        heads = sorted(set(re.findall(r'refs/heads/(\S+)$', o.stdout, re.M)) | ({br} if br else set()))
        with tempfile.TemporaryDirectory() as t:
            subprocess.run(['git', 'init', '-q', '--bare', t], check=True)
            best = []
            for h in heads:
                subprocess.run(['git', '-C', t, 'fetch', '-q', '--depth', '5', '--filter=tree:0', f'https://github.com/{repo}', f'+refs/heads/{h}:refs/heads/{h}'],
                               timeout=60, env=env, capture_output=True)
                lg = subprocess.run(['git', '-C', t, 'log', '-5', '--format=%cI|%s', h], capture_output=True, text=True).stdout.strip().splitlines()
                cs = [{'date': datetime.fromisoformat(l.split('|', 1)[0]).astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'title': l.split('|', 1)[1][:140], 'branch': h} for l in lg if '|' in l]
                if cs and (not best or cs[0]['date'] > best[0]['date']): best = cs
        return {'default_branch': br, 'branches_checked': heads, 'last_commit': best[0]['date'] if best else None,
                'last_commit_branch': best[0]['branch'] if best else None, 'recent_commits': best}
    except Exception as e: return {'atom_error': str(e)[:80]}
def pyproject(repo):
    try: t, _ = get(f'https://raw.githubusercontent.com/{repo}/HEAD/pyproject.toml', raw=True)
    except Exception: return {'pyproject': False}
    try: p = tomllib.loads(t)
    except Exception: return {'pyproject': 'unparseable'}
    proj, comfy = p.get('project', {}), p.get('tool', {}).get('comfy', {})
    return {'pyproject': True, 'version': proj.get('version'), 'requires_python': proj.get('requires-python'),
            'requires_comfyui': comfy.get('requires-comfyui'), 'frontend': comfy.get('requires-comfyui-frontend') or comfy.get('comfyui-frontend-package'),
            'deps': len(proj.get('dependencies', []) or []), 'publisher': comfy.get('PublisherId')}
with cf.ThreadPoolExecutor(16) as ex:
    repos = [gh_repo(n['repository']) for n in top]
    A = dict(zip(repos, ex.map(atom, repos))); P = dict(zip(repos, ex.map(pyproject, repos)))

# GitHub issues API: rotate oldest-fetched first, stop at rate limit
order = sorted(repos, key=lambda r: cache.get(r, {}).get('fetched', ''))
api_calls = 0
for r in order:
    try:
        j, h = get(f'https://api.github.com/repos/{r}/issues?state=open&per_page=100&sort=created', {**AUTH, 'Accept': 'application/vnd.github+json'})
        api_calls += 1
        iss = [i for i in j if 'pull_request' not in i]
        old = cache.get(r, {})
        cache[r] = {'hist': old.get('hist', {}), 'hist_since': old.get('hist_since'), 'fetched': NOW.isoformat(), 'open_issues_sample': len(iss), 'open_issues_capped': len(j) >= 100,
                    'open_prs': len(j) - len(iss),
                    'error_issues': [{'n': i['number'], 'title': i['title'][:160], 'created': i['created_at'], 'url': i['html_url']}
                                     for i in iss if ERR.search(i['title'])][:15]}
        if int(h.get('X-RateLimit-Remaining', 1)) == 0: print('GitHub rate limit reached'); break
        if not TOKEN: time.sleep(0.5)
        # Error-issue history (open AND closed) for the Error-spike baseline. Incremental: after the first
        # fill, only issues updated since the last fetch are requested (usually 1 call per repo).
        hist, since = cache[r]['hist'], cache[r]['hist_since'] or (NOW - timedelta(days=HIST_DAYS)).strftime('%Y-%m-%dT%H:%M:%SZ')
        for pg in range(1, 21):
            hj, hh = get(f'https://api.github.com/repos/{r}/issues?state=all&since={since}&per_page=100&page={pg}', {**AUTH, 'Accept': 'application/vnd.github+json'})
            api_calls += 1
            for i in hj:
                if 'pull_request' not in i and ERR.search(i['title']):
                    hist[str(i['number'])] = {'created': i['created_at'], 'title': i['title'][:160], 'state': i['state'], 'url': i['html_url']}
            if len(hj) < 100 or int(hh.get('X-RateLimit-Remaining', 1)) < 5: break
        cutoff = (NOW - timedelta(days=HIST_DAYS)).isoformat()
        cache[r]['hist'] = {k: v for k, v in hist.items() if v['created'].replace('Z', '+00:00') >= cutoff}
        cache[r]['hist_since'] = NOW.strftime('%Y-%m-%dT%H:%M:%SZ')
    except urllib.error.HTTPError as e:
        if e.code == 429 or (e.code == 403 and e.headers.get('X-RateLimit-Remaining') == '0'):
            print('GitHub rate limited after', api_calls, 'calls'); break
        print('gh http', e.code, r)
        cache[r] = {**cache.get(r, {}), 'fetched': NOW.isoformat(), 'error': e.code}
    except Exception as e: print('gh err', r, e)
save('gh_cache.json', cache)

def days(s):
    try: return (NOW - datetime.fromisoformat(s.replace('Z', '+00:00'))).days
    except Exception: return None
out = []
for rank, n in enumerate(top, 1):
    r = gh_repo(n['repository']); a, p, c = A[r], P[r], cache.get(r, {})
    lv = n.get('latest_version') or {}
    dc = days(a.get('last_commit')) if a.get('last_commit') else None
    hist = list(c.get('hist', {}).values())
    recent_err = sorted([i for i in hist if (days(i['created']) if days(i['created']) is not None else 999) <= 30], key=lambda i: i['created'], reverse=True)
    base_n = sum(1 for i in hist if 30 < (days(i['created']) or 0) <= 210)
    baseline = round(base_n / 6, 2)
    per100k = round(len(recent_err) / max((n.get('downloads') or 0) / 1e5, 0.01), 2) if n.get('downloads') else None
    spike = (len(recent_err) >= SPIKE_MIN and len(recent_err) >= SPIKE_BASELINE_X * max(baseline, 1.0)
             and per100k is not None and per100k >= SPIKE_PER100K)
    errstats = {'recent_30d': len(recent_err), 'baseline_30d_avg': baseline, 'baseline_180d_total': base_n, 'per_100k_downloads': per100k,
                'ratio_vs_baseline': round(len(recent_err) / max(baseline, 1.0), 2), 'history_fetched': 'hist_since' in c and c.get('hist_since') is not None}
    notes = []
    if lv.get('deprecated'): notes.append('latest registry version deprecated')
    if n.get('status') not in (None, '', 'NodeStatusActive'): notes.append(f'registry status {n.get("status")}')
    reasons = []
    if a.get('atom_error') == 404: status = 'Stale / abandoned'; reasons.append('GitHub repo not found (deleted/private/renamed)')
    elif dc is None: status = 'Unknown'
    elif dc > 365: status = 'Stale / abandoned'; reasons.append(f'no commits in {dc} days')
    elif spike:
        status = 'Error spike'
        reasons.append(f'{len(recent_err)} error-titled issues in last 30 days vs {baseline}/month baseline; {per100k} per 100K downloads — worth checking recent issues')
    else:
        status = 'Active'; reasons.append(f'last commit {dc} days ago')
    quiet = dc is not None and 180 < dc <= 365 and status == 'Active'
    if quiet: reasons.append('Quiet: no commits in 6+ months')
    reasons += notes
    out.append({'rank': rank, 'id': n['id'], 'name': n.get('name') or n['id'], 'description': (n.get('description') or '')[:400],
        'repo': r, 'repo_url': f'https://github.com/{r}', 'publisher': (n.get('publisher') or {}).get('id'),
        'downloads': n.get('downloads'), 'stars': n.get('github_stars'), 'registry_created': n.get('created_at'),
        'latest_version': lv.get('version'), 'latest_version_date': lv.get('createdAt'),
        'registry_comfyui_version': lv.get('supported_comfyui_version') or n.get('supported_comfyui_version'),
        'in_manager_list': f'https://github.com/{r}'.lower() in mgr_repos, 'days_since_commit': dc, **a, 'pyproject': p,
        'issues': c, 'recent_error_issues': recent_err, 'error_stats': errstats, 'status': status, 'quiet': quiet, 'reasons': reasons})
prev = load('nodes.json', None)
if prev: save('nodes_prev.json', prev)
meta = {'generated': NOW.isoformat(), 'registry_total': len(nodes), 'registry_with_github': len(cands), 'manager_list_total': len(mgr),
        'tracked': len(out), 'github_mode': mode, 'api_calls_this_run': api_calls,
        'issues_coverage': sum(1 for o in out if o['issues'].get('fetched'))}
save('nodes.json', {'meta': meta, 'nodes': out}); print(json.dumps(meta, indent=1))
