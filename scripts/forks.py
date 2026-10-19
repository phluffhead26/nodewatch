#!/usr/bin/env python3
"""Active forks for Stale/Quiet packs (idea: u/bonalex01). Automatic suggestions, not endorsements.
For each pack: list forks (sort=newest + sort=stargazers, 100 each), keep forks pushed after upstream's last
commit, compare upstream default branch...fork:branch for up to MAX_COMPARE candidates, rank by
commits ahead + recency + fork stars. Usage: forks.py --all (full scan, box) | forks.py (rotating: packs
not scanned in 7 days, at most ROTATE packs per run, stops if REST budget < RESERVE)."""
import json, os, sys, subprocess, math, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
D = os.path.join(os.path.dirname(__file__), '..', 'data'); NOW = datetime.now(timezone.utc)
MAX_COMPARE, ROTATE, RESERVE, REFRESH_DAYS = 6, 30, 100, 7
tok = os.environ.get('GITHUB_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
H = {'Authorization': f'Bearer {tok}', 'User-Agent': 'NodeWatch/0.1', 'Accept': 'application/vnd.github+json'}
calls, remaining = 0, 9999
def get(path):
    global calls, remaining
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com/' + path, headers=H), timeout=30) as f:
        calls += 1; remaining = int(f.headers.get('X-RateLimit-Remaining', remaining)); return json.loads(f.read())
def P(s): return datetime.fromisoformat(s.replace('Z', '+00:00'))
nodes = json.load(open(f'{D}/nodes.json'))['nodes']
fp = f'{D}/forks.json'; cache = json.load(open(fp)) if os.path.exists(fp) else {}
targets = [n for n in nodes if (n['status'].startswith('Stale') or n.get('quiet')) and n.get('last_commit') and n.get('default_branch')]
if '--all' not in sys.argv:
    due = [n for n in targets if NOW - P(cache.get(n['repo'], {}).get('scanned', '2000-01-01T00:00:00Z')) > timedelta(days=REFRESH_DAYS)]
    targets = sorted(due, key=lambda n: cache.get(n['repo'], {}).get('scanned', ''))[:ROTATE]
for n in targets:
    if remaining < RESERVE: print('forks: stopping, REST budget low', remaining); break
    up, ub, ulast = n['repo'], n['default_branch'], P(n['last_commit'])
    try:
        fl = {}
        for sort in ('newest', 'stargazers'):
            for f in get(f'repos/{up}/forks?per_page=100&sort={sort}'): fl[f['full_name']] = f
        cand = [f for f in fl.values() if f.get('pushed_at') and P(f['pushed_at']) > ulast + timedelta(days=1)]
        cand.sort(key=lambda f: (f['stargazers_count'], f['pushed_at']), reverse=True)
        res = []
        for f in cand[:MAX_COMPARE]:
            base = f'repos/{up}/compare/{ub}...{f["owner"]["login"]}:{f["default_branch"]}'
            try: c = get(base + '?per_page=1')          # small payload; ahead_by/behind_by are totals
            except Exception: continue
            if c.get('ahead_by', 0) < 1: continue
            try: c['commits'] = get(base + f'?per_page=1&page={c["ahead_by"]}').get('commits') or c.get('commits')  # newest ahead commit
            except Exception: pass
            last = c['commits'][-1]['commit']['committer']['date'] if c.get('commits') else f['pushed_at']
            if P(last) <= ulast: continue
            dd = (NOW - P(last)).days
            score = round(min(c['ahead_by'], 50) * 2 + max(0, 180 - dd) / 18 + math.log2(1 + f['stargazers_count']) * 3, 1)
            res.append({'repo': f['full_name'], 'url': f['html_url'], 'branch': f['default_branch'], 'ahead': c['ahead_by'], 'behind': c['behind_by'],
                        'last_commit': last, 'stars': f['stargazers_count'], 'score': score,
                        'last_title': (c['commits'][-1]['commit']['message'].splitlines() or [''])[0][:120] if c.get('commits') else ''})
        res.sort(key=lambda x: x['score'], reverse=True)
        cache[up] = {'scanned': NOW.isoformat(), 'forks_listed': len(fl), 'candidates': len(cand), 'active': res[:5]}
    except Exception as e:
        cache[up] = {'scanned': NOW.isoformat(), 'error': str(getattr(e, 'code', e))[:60]}
    json.dump(cache, open(fp, 'w'), indent=0)   # save progress after each pack
json.dump(cache, open(fp, 'w'), indent=0)
print(f'forks: scanned {len(targets)} packs, {calls} REST calls, {remaining} remaining', file=sys.stderr)
