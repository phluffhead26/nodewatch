#!/usr/bin/env python3
"""Star velocity. Nightly: one GraphQL query per 50 repos (stargazerCount) -> data/star_history.json snapshot.
Velocity = today's stars minus the snapshot nearest 30 (and 7) days ago.
Until a full 30-day window exists, the delta is over the longest span available (span_30d says how many days)."""
import json, os, sys, subprocess, math, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
D = os.path.join(os.path.dirname(__file__), '..', 'data'); NOW = datetime.now(timezone.utc); TODAY = NOW.strftime('%Y-%m-%d')
tok = os.environ.get('GITHUB_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
if not tok: sys.exit('stars.py needs GITHUB_TOKEN or gh auth (GraphQL requires a token)')
H = {'Authorization': f'Bearer {tok}', 'User-Agent': 'NodeWatch/0.1'}
def req(url, data=None, accept='application/vnd.github+json'):
    r = urllib.request.Request(url, data=json.dumps(data).encode() if data else None, headers={**H, 'Accept': accept})
    with urllib.request.urlopen(r, timeout=60) as f: return json.loads(f.read())
nodes = json.load(open(f'{D}/nodes.json'))['nodes']; repos = [n['repo'] for n in nodes]
hp = f'{D}/star_history.json'; hist = json.load(open(hp)) if os.path.exists(hp) else {}
# 1. current counts via GraphQL (aliases, 50 repos/query)
cur, calls = {}, 0
for i in range(0, len(repos), 50):
    chunk = repos[i:i + 50]
    q = 'query{' + ' '.join(f'r{j}: repository(owner:{json.dumps(r.split("/")[0])}, name:{json.dumps(r.split("/")[1])}){{stargazerCount}}' for j, r in enumerate(chunk)) + '}'
    try: res = req('https://api.github.com/graphql', {'query': q}); calls += 1
    except urllib.error.HTTPError as e: print('graphql error', e.code); continue
    for j, r in enumerate(chunk):
        v = (res.get('data') or {}).get(f'r{j}')
        if v: cur[r] = v['stargazerCount']
for r, s in cur.items(): hist.setdefault(r, {})[TODAY] = s
print(f'GraphQL star snapshot: {len(cur)}/{len(repos)} repos, {calls} queries', file=sys.stderr)
# 2. No backfill: as of Oct 2026 GitHub's list-stargazers endpoint returns 404 for repos you don't own
#    (REST and GraphQL `stargazers` edges come back empty), GH Archive is heavily sampled, and registry
#    github_stars lag GitHub. So velocity is computed purely from these nightly snapshots, starting 2026-10-19.
bmeta = {}
# trim to 400 days
lim = (NOW - timedelta(days=400)).strftime('%Y-%m-%d')
hist = {r: {d: v for d, v in sorted(h.items()) if d >= lim} for r, h in hist.items()}
json.dump(hist, open(hp, 'w'), separators=(',', ':'), sort_keys=True)
def delta(h, days):
    if TODAY not in h or len(h) < 2: return None, None
    target = (NOW - timedelta(days=days)).strftime('%Y-%m-%d')
    older = [d for d in h if d <= target] or [min(h)]
    base = max(older) if [d for d in h if d <= target] else min(h)
    if base == TODAY: return None, None
    return h[TODAY] - h[base], (NOW.date() - datetime.strptime(base, '%Y-%m-%d').date()).days
out = {}
for r in repos:
    h = hist.get(r, {}); d30, span30 = delta(h, 30); d7, span7 = delta(h, 7)
    s = h.get(TODAY)
    out[r] = {'stars_now': s, 'stars_30d': d30, 'span_30d': span30, 'stars_7d': d7, 'span_7d': span7,
              'per_week': round(d30 / span30 * 7, 1) if d30 is not None and span30 else None,
              'rel_30d_pct': round(100 * d30 / max(s - d30, 1), 1) if d30 is not None and s else None,
              'capped': bmeta.get(r, {}).get('capped', False)}
first = min((min(h) for h in hist.values() if h), default=TODAY)
json.dump({'date': TODAY, 'history_since': first, 'graphql_queries': calls, 'repos': out}, open(f'{D}/stars.json', 'w'), indent=0)
