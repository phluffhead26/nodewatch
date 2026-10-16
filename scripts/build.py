#!/usr/bin/env python3
"""Builds static site from data/nodes.json into site/ and newsletter draft into newsletter/."""
import json, os, html, shutil
from datetime import datetime, timezone, timedelta
R = os.path.join(os.path.dirname(__file__), '..'); S = os.path.join(R, 'site')
J = json.load(open(f'{R}/data/nodes.json')); M, N = J['meta'], J['nodes']
P = os.path.join(R, 'data/nodes_prev.json'); prev = {n['id']: n for n in json.load(open(P))['nodes']} if os.path.exists(P) else {}
NOW = datetime.fromisoformat(M['generated']); WEEK = NOW - timedelta(days=7)
e = lambda x: html.escape(str(x if x is not None else '—'))
def dt(s):
    try: return datetime.fromisoformat(str(s).replace('Z', '+00:00'))
    except Exception: return None
def d10(s): return (s or '—')[:10]
CSS = """body{font:15px/1.5 system-ui,sans-serif;margin:0;background:#0f1115;color:#e6e6e6}a{color:#7cb7ff}header{background:#171a21;padding:12px 24px;border-bottom:1px solid #2a2f3a}
header a{margin-right:18px;font-weight:600}main{padding:20px 24px;max-width:1200px;margin:auto}table{border-collapse:collapse;width:100%}th,td{padding:6px 8px;border-bottom:1px solid #252a33;text-align:left;vertical-align:top}
th{cursor:pointer;background:#171a21;position:sticky;top:0}.b{padding:2px 8px;border-radius:10px;font-size:12px;white-space:nowrap}.Active{background:#1f5130}.Possibly{background:#6b4a10}.Stale{background:#5a1f1f}.Unknown{background:#444}
input,select{background:#171a21;color:#eee;border:1px solid #333;padding:6px;border-radius:4px;margin-right:8px}.muted{color:#999;font-size:13px}.card{background:#171a21;padding:12px 16px;border-radius:8px;margin:12px 0}"""
def page(title, body, depth=0):
    up = '../' * depth
    return f"""<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width"><title>{e(title)} · NodeWatch</title><link rel=stylesheet href="{up}style.css"></head>
<body><header><a href="{up}index.html">NodeWatch</a><a href="{up}changes.html">What changed this week</a><a href="{up}about.html">About / methodology</a></header><main><div class=card style='border-left:4px solid #c90'><b>Heads up:</b> statuses are automated heuristics from commit dates, registry metadata and issue titles. &quot;Stale&quot; can mean &quot;finished and stable&quot;; &quot;Possibly broken&quot; means users are reporting errors, not that it is confirmed broken. Always check the repo.</div>{body}</main></body></html>"""
def badge(s): return f'<span class="b {s.split()[0]}">{e(s)}</span>'
shutil.rmtree(S, ignore_errors=True); os.makedirs(f'{S}/node')
open(f'{S}/style.css', 'w').write(CSS)
idx = [{k: n.get(k) for k in ('rank', 'id', 'name', 'repo', 'downloads', 'stars', 'last_commit', 'days_since_commit', 'status', 'quiet')} |
       {'open_issues': n['issues'].get('open_issues_sample'), 'err': len(n['recent_error_issues']), 'req': n['pyproject'].get('requires_comfyui') or n.get('registry_comfyui_version'), 'desc': n['description'][:160]} for n in N]
open(f'{S}/data.json', 'w').write(json.dumps(idx)); shutil.copy(f'{R}/data/nodes.json', f'{S}/nodes-full.json')
from collections import Counter
c = Counter(n['status'] for n in N)
open(f'{S}/index.html', 'w').write(page('Index', f"""<h1>NodeWatch</h1><p class=muted>Tracking the top {M['tracked']} ComfyUI custom node packs (by registry downloads) out of {M['registry_total']} in the Comfy Registry. Updated {d10(M['generated'])}. GitHub mode: {e(M['github_mode'])}; issue data for {M['issues_coverage']}/{M['tracked']} packs.</p>
<p>{' '.join(f'{badge(k)} {v}' for k, v in c.most_common())}</p>
<p><input id=q placeholder="Search name, repo, description…" size=40><select id=st><option value="">All statuses</option><option value="__quiet">Quiet (6–12 mo)</option>{''.join(f'<option>{k}</option>' for k in c)}</select><span id=cnt class=muted></span></p>
<table><thead><tr><th data-k=rank>#</th><th data-k=name>Pack</th><th data-k=status>Status</th><th data-k=downloads>Downloads</th><th data-k=stars>Stars</th><th data-k=last_commit>Last commit</th><th data-k=open_issues>Open issues*</th><th data-k=err>Recent error issues</th><th data-k=req>ComfyUI req.</th></tr></thead><tbody id=tb></tbody></table>
<p class=muted>* open issues excluding PRs, sampled from the first 100 open items; blank = not yet fetched (GitHub rate limit).</p>
<script>
let D=[],sk='rank',sd=1;const $=s=>document.querySelector(s);
fetch('data.json').then(r=>r.json()).then(d=>{{D=d;R()}});
function R(){{const q=$('#q').value.toLowerCase(),st=$('#st').value;
let r=D.filter(n=>(!st||n.status==st||(st=='__quiet'&&n.quiet))&&(!q||(n.name+' '+n.repo+' '+n.desc+' '+n.id).toLowerCase().includes(q)));
r.sort((a,b)=>{{let x=a[sk],y=b[sk];if(x==null)return 1;if(y==null)return -1;return (x>y?1:x<y?-1:0)*sd}});
$('#cnt').textContent=r.length+' packs';
$('#tb').innerHTML=r.map(n=>`<tr><td>${{n.rank}}</td><td><a href="node/${{encodeURIComponent(n.id)}}.html">${{esc(n.name)}}</a><div class=muted>${{esc(n.repo)}}</div></td><td><span class="b ${{n.status.split(' ')[0]}}">${{n.status}}</span>${{n.quiet?' <span class="b Unknown">Quiet</span>':''}}</td><td>${{(n.downloads||0).toLocaleString()}}</td><td>${{n.stars??''}}</td><td>${{(n.last_commit||'').slice(0,10)}}</td><td>${{n.open_issues??''}}</td><td>${{n.err||''}}</td><td>${{esc(n.req||'')}}</td></tr>`).join('')}}
function esc(s){{return String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c])}}
$('#q').oninput=R;$('#st').onchange=R;document.querySelectorAll('th').forEach(t=>t.onclick=()=>{{const k=t.dataset.k;sd=sk==k?-sd:(['downloads','stars','last_commit','err','open_issues'].includes(k)?-1:1);sk=k;R()}});
</script>"""))
for n in N:
    p, i = n['pyproject'], n['issues']
    errs = ''.join(f'<li><a href="{e(x["url"])}">#{x["n"]}</a> {e(x["title"])} <span class=muted>{d10(x["created"])}</span></li>' for x in i.get('error_issues', [])) or '<li class=muted>None found' + ('' if i.get('fetched') else ' (issues not fetched yet — GitHub rate limit)') + '</li>'
    cm = ''.join(f'<li>{d10(x["date"])} <span class=muted>[{e(x.get("branch"))}]</span> {e(x["title"])}</li>' for x in n.get('recent_commits', []))
    body = f"""<h1>{e(n['name'])} {badge(n['status'])}</h1><p>{e(n['description'])}</p><p class=muted>Why: {e('; '.join(n['reasons']))}</p>
<div class=card><table>
<tr><th>Repo</th><td><a href="{e(n['repo_url'])}">{e(n['repo'])}</a> (default branch {e(n.get('default_branch'))})</td></tr>
<tr><th>Registry</th><td><a href="https://registry.comfy.org/nodes/{e(n['id'])}">{e(n['id'])}</a> · publisher {e(n['publisher'])} · latest {e(n['latest_version'])} ({d10(n['latest_version_date'])}) · in Manager list: {'yes' if n['in_manager_list'] else 'no'}</td></tr>
<tr><th>Popularity</th><td>rank #{n['rank']} · {n['downloads'] or 0:,} downloads · {e(n['stars'])} stars</td></tr>
<tr><th>Last commit</th><td>{d10(n.get('last_commit'))} ({e(n.get('days_since_commit'))} days ago)</td></tr>
<tr><th>Open issues</th><td>{e(i.get('open_issues_sample'))}{'+' if i.get('open_issues_capped') else ''} issues, {e(i.get('open_prs'))} PRs <span class=muted>(fetched {d10(i.get('fetched'))})</span></td></tr>
<tr><th>pyproject.toml</th><td>{'present' if p.get('pyproject') is True else e(p.get('pyproject') or 'missing')} · version {e(p.get('version'))} · requires-comfyui <b>{e(p.get('requires_comfyui'))}</b> · frontend {e(p.get('frontend'))} · requires-python {e(p.get('requires_python'))} · {e(p.get('deps'))} deps</td></tr>
<tr><th>Registry ComfyUI req.</th><td>{e(n.get('registry_comfyui_version'))}</td></tr></table></div>
<h2>Open issues mentioning errors / breakage</h2><ul>{errs}</ul><h2>Recent commits</h2><ul>{cm or '<li class=muted>n/a</li>'}</ul>"""
    open(f'{S}/node/{n["id"]}.html', 'w').write(page(n['name'], body, 1))
# changes
commits = sorted([n for n in N if (dt(n.get('last_commit')) or NOW - timedelta(999)) >= WEEK], key=lambda n: n['last_commit'], reverse=True)
rel = sorted([n for n in N if (dt(n.get('latest_version_date')) or NOW - timedelta(999)) >= WEEK], key=lambda n: n['latest_version_date'], reverse=True)
newerr = [(n, x) for n in N for x in n['recent_error_issues'] if (dt(x['created']) or NOW - timedelta(999)) >= WEEK]
sc = [(n, prev[n['id']]['status']) for n in N if n['id'] in prev and prev[n['id']]['status'] != n['status']]
entered = [n for n in N if prev and n['id'] not in prev]
L = lambda n: f'<a href="node/{e(n["id"])}.html">{e(n["name"])}</a>'
body = f"""<h1>What changed this week</h1><p class=muted>{d10(WEEK.isoformat())} → {d10(M['generated'])}</p>
<h2>Status changes since last run ({len(sc)})</h2><ul>{''.join(f'<li>{L(n)}: {e(o)} → {badge(n["status"])}</li>' for n, o in sc) or '<li class=muted>None (or first run — no previous snapshot)</li>'}</ul>
<h2>New registry releases ({len(rel)})</h2><ul>{''.join(f'<li>{d10(n["latest_version_date"])} {L(n)} v{e(n["latest_version"])}</li>' for n in rel)}</ul>
<h2>Packs with commits ({len(commits)})</h2><ul>{''.join(f'<li>{d10(n["last_commit"])} {L(n)} — {e(n["recent_commits"][0]["title"])}</li>' for n in commits)}</ul>
<h2>New error/breakage issues ({len(newerr)})</h2><ul>{''.join(f'<li>{L(n)}: <a href="{e(x["url"])}">{e(x["title"])}</a></li>' for n, x in newerr) or '<li class=muted>None in sampled repos</li>'}</ul>
<h2>Entered the top {M['tracked']} ({len(entered)})</h2><ul>{''.join(f'<li>{L(n)}</li>' for n in entered) or '<li class=muted>n/a</li>'}</ul>"""
open(f'{S}/changes.html', 'w').write(page('What changed', body))
open(f'{S}/about.html', 'w').write(page('About', f"""<h1>Methodology</h1><ul>
<li>Pack list: Comfy Registry API (api.comfy.org/nodes, {M['registry_total']} packs) cross-checked with ComfyUI-Manager custom-node-list.json ({M['manager_list_total']} entries). Top {M['tracked']} by registry downloads with a GitHub repo.</li>
<li>Stars & downloads: registry. Last commit: <code>git ls-remote</code> + shallow treeless fetch of default branch and main/master (newest wins). pyproject.toml: raw.githubusercontent.com, parsed per the registry spec (<code>[tool.comfy] requires-comfyui</code>).</li>
<li>Issues: GitHub REST API ({e(M['github_mode'])}), cached and rotated oldest-first each run. Error issues = open issue titles matching error/broken/fail/crash/traceback/etc.</li>
<li>Status: <b>Stale / abandoned</b> = repo gone, or no commit &gt;365 days. <b>Quiet</b> (note on Active packs) = no commit in 6–12 months. <b>Possibly broken</b> = ≥3 error-titled issues opened in 60 days, deprecated latest version, or non-active registry status. <b>Active</b> = otherwise. Heuristic only — a stable "finished" pack may be flagged stale.</li></ul>"""))
# newsletter
os.makedirs(f'{R}/newsletter', exist_ok=True)
top50 = N[:50]; stale = [n for n in N if n['status'].startswith('Stale')]; old = [n for n in stale if (n['days_since_commit'] or 0) > 365]
pb = [n for n in N if n['status'] == 'Possibly broken']
nl = f"""# NodeWatch Weekly — Issue #1 ({d10(M['generated'])})

*The health report for ComfyUI custom nodes. We track the top {M['tracked']} node packs (by Comfy Registry downloads) out of {M['registry_total']:,} registered.*

## The big picture
- **{c['Active']}** of {M['tracked']} popular packs are **Active** (commit within the last year); **{len(stale)}** look **stale**, and **{len(old)}** haven't had a commit in over a year (stale), and **{sum(1 for n in N if n.get('quiet'))}** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, {sum(1 for n in top50 if n['status'].startswith('Stale'))} are stale (no commit in 12+ months), including household names:
""" + ''.join(f"  - **{n['name']}** (#{n['rank']}, {n['downloads']:,} downloads, {n['stars']} ★) — last commit {d10(n['last_commit'])}\n" for n in [n for n in top50 if n['status'].startswith('Stale')][:8]) + f"""- Only **{sum(1 for n in N if n['pyproject'].get('requires_comfyui'))}** of {M['tracked']} declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **{sum(1 for n in N if (n['days_since_commit'] or 999) <= 7)}** packs shipped commits this week; **{len(rel)}** published a new registry release.

## ⚠️ Possibly broken
""" + (''.join(f"- **{n['name']}** — {'; '.join(n['reasons'])}. Recent reports: " + '; '.join(f"[{x['title'][:80]}]({x['url']})" for x in n['recent_error_issues'][:3]) + '\n' for n in pb) or '- Nothing flagged this week.\n') + f"""
## 🚀 Fresh releases this week
""" + ''.join(f"- **{n['name']}** v{n['latest_version']} ({d10(n['latest_version_date'])})\n" for n in rel[:10]) + f"""
## 🪦 Gone missing
""" + (''.join(f"- **{n['name']}** — `{n['repo']}` no longer resolves on GitHub (still listed in the registry)\n" for n in N if n.get('atom_error') == 404) or '- None\n') + f"""
## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
"""
open(f'{R}/newsletter/issue-001.md', 'w').write(nl); print('built', len(N), 'pages')
