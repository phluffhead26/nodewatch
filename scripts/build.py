#!/usr/bin/env python3
"""Builds static site from data/nodes.json into site/ and newsletter draft into newsletter/."""
import json, os, html, shutil
from datetime import datetime, timezone, timedelta
R = os.path.join(os.path.dirname(__file__), '..'); S = os.path.join(R, 'site')
J = json.load(open(f'{R}/data/nodes.json')); M, N = J['meta'], J['nodes']
P = os.path.join(R, 'data/nodes_prev.json'); prev = {n['id']: n for n in json.load(open(P))['nodes']} if os.path.exists(P) else {}
NOW = datetime.fromisoformat(M['generated']); WEEK = NOW - timedelta(days=7)
SITE = 'https://phluffhead26.github.io/nodewatch/'
def jl(name, d):
    q = os.path.join(R, 'data', name); return json.load(open(q)) if os.path.exists(q) else d
STARS = jl('stars.json', {}); FORKS = jl('forks.json', {}); CATS = jl('categories.json', {})
SV = STARS.get('repos', {}); HSINCE = STARS.get('history_since', '—')
for n in N:
    v = SV.get(n['repo'], {}); n['vel'] = v
    n['s30'] = v.get('stars_30d'); n['span'] = v.get('span_30d'); n['pw'] = v.get('per_week'); n['rel'] = v.get('rel_30d_pct')
    f = FORKS.get(n['repo'], {}); n['afork'] = f.get('active', []) if (n['status'].startswith('Stale') or n.get('quiet')) else []
    t = CATS.get(n['id'], {}); n['fn'] = t.get('functions', []); n['md'] = t.get('models', [])
import re as _re
slug = lambda x: _re.sub(r'[^a-z0-9]+', '-', x.lower().replace('&', 'and').replace('.', '')).strip('-')
FN_ALL = sorted({x for n in N for x in n['fn']}); MD_ALL = sorted({x for n in N for x in n['md']}, key=lambda x: (x == 'Generic / any', x))
def span_note(n): return f"+{n['s30']} in {n['span']}d" if n.get('s30') is not None else '—'
e = lambda x: html.escape(str(x if x is not None else '—'))
def dt(s):
    try: return datetime.fromisoformat(str(s).replace('Z', '+00:00'))
    except Exception: return None
def d10(s): return (s or '—')[:10]
CSS = """body{font:15px/1.5 system-ui,sans-serif;margin:0;background:#0f1115;color:#e6e6e6}a{color:#7cb7ff}header{background:#171a21;padding:12px 24px;border-bottom:1px solid #2a2f3a}
header a{margin-right:18px;font-weight:600}main{padding:20px 24px;max-width:1200px;margin:auto}table{border-collapse:collapse;width:100%}th,td{padding:6px 8px;border-bottom:1px solid #252a33;text-align:left;vertical-align:top}
th{cursor:pointer;background:#171a21;position:sticky;top:0}.b{padding:2px 8px;border-radius:10px;font-size:12px;white-space:nowrap}.Active{background:#1f5130}.Error{background:#6b4a10}.Stale{background:#5a1f1f}.Unknown{background:#444}.Fork{background:#24477a}.tag{display:inline-block;background:#222833;border-radius:4px;padding:1px 7px;margin:2px;font-size:13px}button{background:#24477a;color:#eee;border:0;padding:6px 10px;border-radius:4px;cursor:pointer;margin-right:6px}
input,select{background:#171a21;color:#eee;border:1px solid #333;padding:6px;border-radius:4px;margin-right:8px}.muted{color:#999;font-size:13px}.card{background:#171a21;padding:12px 16px;border-radius:8px;margin:12px 0}"""
def page(title, body, depth=0):
    up = '../' * depth
    return f"""<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width"><title>{e(title)} · NodeWatch</title><link rel=stylesheet href="{up}style.css"></head>
<body><header><a href="{up}index.html">NodeWatch</a><a href="{up}changes.html">What changed this week</a><a href="{up}about.html">About / methodology</a></header><main><div class=card style='border-left:4px solid #c90'><b>Heads up:</b> statuses are automated heuristics from commit dates, registry metadata and issue titles. &quot;Stale&quot; can mean &quot;finished and stable&quot;; &quot;Error spike&quot; means error-titled issues are unusually high for that pack lately — worth checking recent issues, not a verdict that it is broken. Always check the repo.</div>{body}</main><script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script></body></html>"""
SIGNUP = """<div class=card id=signup><b>Get the weekly NodeWatch report: what broke, what went stale, what shipped.</b>
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="9aeaac30-d209-476b-a30c-c48486ecf584"></script>
<div class=muted>Form not showing? <a href="https://nodewatch-news.beehiiv.com/subscribe">Subscribe here</a>.</div></div>"""
def badge(s): return f'<span class="b {s.split()[0]}">{e(s)}</span>'
shutil.rmtree(S, ignore_errors=True); os.makedirs(f'{S}/node')
open(f'{S}/style.css', 'w').write(CSS)
idx = [{k: n.get(k) for k in ('rank', 'id', 'name', 'repo', 'downloads', 'stars', 'last_commit', 'days_since_commit', 'status', 'quiet')} |
       {'open_issues': n['issues'].get('open_issues_sample'), 'err': len(n['recent_error_issues']), 'per100k': n.get('error_stats', {}).get('per_100k_downloads'), 'req': n['pyproject'].get('requires_comfyui') or n.get('registry_comfyui_version'), 'desc': n['description'][:160], 's30': n['s30'], 'span': n['span'], 'pw': n['pw'], 'rel': n['rel'], 'af': len(n['afork']), 'fn': n['fn'], 'md': n['md']} for n in N]
open(f'{S}/data.json', 'w').write(json.dumps(idx)); shutil.copy(f'{R}/data/nodes.json', f'{S}/nodes-full.json')
from collections import Counter
c = Counter(n['status'] for n in N)
open(f'{S}/index.html', 'w').write(page('Index', f"""<h1>NodeWatch</h1><p class=muted>Tracking the top {M['tracked']} ComfyUI custom node packs (by registry downloads) out of {M['registry_total']} in the Comfy Registry. Updated {d10(M['generated'])}. GitHub mode: {e(M['github_mode'])}; issue data for {M['issues_coverage']}/{M['tracked']} packs.</p>
<p>{' '.join(f'{badge(k)} {v}' for k, v in c.most_common())}</p>
{SIGNUP}<p class=muted>Browse by function: {' · '.join(f'<a href="category/{slug(x)}.html">{e(x)}</a>' for x in FN_ALL)}<br>By model family: {' · '.join(f'<a href="model/{slug(x)}.html">{e(x)}</a>' for x in MD_ALL)}</p>
<p><input id=q placeholder="Search name, repo, description…" size=40><select id=st><option value="">All statuses</option><option value="__quiet">Quiet (6–12 mo)</option>{''.join(f'<option>{k}</option>' for k in c)}<option value="__fork">Has active fork</option></select><select id=fn><option value="">All functions</option>{''.join(f'<option>{e(x)}</option>' for x in FN_ALL)}</select><select id=md><option value="">All model families</option>{''.join(f'<option>{e(x)}</option>' for x in MD_ALL)}</select><button id=tr>🔥 Trending (stars gained)</button> <button id=trr>Trending relative to size</button> <span id=cnt class=muted></span></p>
<table><thead><tr><th data-k=rank>#</th><th data-k=name>Pack</th><th data-k=status>Status</th><th data-k=downloads>Downloads</th><th data-k=stars>Stars</th><th data-k=s30>Stars (30d)†</th><th data-k=last_commit>Last commit</th><th data-k=open_issues>Open issues*</th><th data-k=err>Error issues (30d)</th><th data-k=per100k>per 100K dl</th><th data-k=req>ComfyUI req.</th></tr></thead><tbody id=tb></tbody></table>
<p class=muted>† Stars gained, from nightly GitHub snapshots that started {e(HSINCE)}; until 30 days of history exist this is the gain over the days available (hover for span and per-week rate). * open issues excluding PRs, sampled from the first 100 open items; blank = not yet fetched (GitHub rate limit).</p>
<script>
let D=[],sk='rank',sd=1;const $=s=>document.querySelector(s);
fetch('data.json').then(r=>r.json()).then(d=>{{D=d;R()}});
function R(){{const q=$('#q').value.toLowerCase(),st=$('#st').value;
let r=D.filter(n=>(!st||n.status==st||(st=='__quiet'&&n.quiet)||(st=='__fork'&&n.af))&&(!$('#fn').value||n.fn.includes($('#fn').value))&&(!$('#md').value||n.md.includes($('#md').value))&&(!q||(n.name+' '+n.repo+' '+n.desc+' '+n.id).toLowerCase().includes(q)));
r.sort((a,b)=>{{let x=a[sk],y=b[sk];if(x==null)return 1;if(y==null)return -1;return (x>y?1:x<y?-1:0)*sd}});
$('#cnt').textContent=r.length+' packs';
$('#tb').innerHTML=r.map(n=>`<tr><td>${{n.rank}}</td><td><a href="node/${{encodeURIComponent(n.id)}}.html">${{esc(n.name)}}</a><div class=muted>${{esc(n.repo)}}</div></td><td><span class="b ${{n.status.split(' ')[0]}}">${{n.status}}</span>${{n.quiet?' <span class="b Unknown">Quiet</span>':''}}${{n.af?' <span class="b Fork">Has active fork</span>':''}}</td><td>${{(n.downloads||0).toLocaleString()}}</td><td>${{n.stars??''}}</td><td title="${{n.span?('over '+n.span+' days; '+n.pw+'/week; '+n.rel+'% of prior stars'):'collecting'}}">${{n.s30!=null?('+'+n.s30):''}}</td><td>${{(n.last_commit||'').slice(0,10)}}</td><td>${{n.open_issues??''}}</td><td>${{n.err||''}}</td><td>${{n.err?n.per100k:''}}</td><td>${{esc(n.req||'')}}</td></tr>`).join('')}}
function esc(s){{return String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c])}}
$('#q').oninput=R;$('#st').onchange=R;$('#fn').onchange=R;$('#md').onchange=R;$('#tr').onclick=()=>{{sk='s30';sd=-1;R()}};$('#trr').onclick=()=>{{sk='rel';sd=-1;R()}};document.querySelectorAll('th').forEach(t=>t.onclick=()=>{{const k=t.dataset.k;sd=sk==k?-sd:(['downloads','stars','s30','rel','last_commit','err','per100k','open_issues'].includes(k)?-1:1);sk=k;R()}});
</script>"""))
def forks_html(n):
    if not (n['status'].startswith('Stale') or n.get('quiet')): return ''
    f = FORKS.get(n['repo'])
    if not f: return '<h2>Active forks</h2><p class=muted>Not scanned yet.</p>'
    rows = ''.join(f'<tr><td><a href="{e(x["url"])}">{e(x["repo"])}</a><div class=muted>{e(x["last_title"])}</div></td><td>{x["ahead"]} ahead / {x["behind"]} behind</td><td>{d10(x["last_commit"])}</td><td>{x["stars"]} ★</td></tr>' for x in f.get('active', [])[:3])
    return f'<h2>Active forks</h2><p class=muted>Automatic suggestions, not endorsements: forks with commits newer than upstream, ranked by commits ahead, recency and stars. Read the fork\'s README and diff before switching. Scanned {d10(f.get("scanned"))}: {f.get("forks_listed", 0)} forks checked.</p>' + (f'<table><tr><th>Fork</th><th>Commits</th><th>Last commit</th><th>Stars</th></tr>{rows}</table>' if rows else '<p class=muted>No fork found that is ahead of upstream with newer commits.</p>')
for n in N:
    p, i, es = n['pyproject'], n['issues'], n.get('error_stats', {})
    errs = ''.join(f'<li><a href="{e(x["url"])}">#{x["n"]}</a> {e(x["title"])} <span class=muted>{d10(x["created"])}</span></li>' for x in i.get('error_issues', [])) or '<li class=muted>None found' + ('' if i.get('fetched') else ' (issues not fetched yet — GitHub rate limit)') + '</li>'
    rec = ''.join(f'<li><a href="{e(x["url"])}">{e(x["title"])}</a> <span class=muted>{d10(x["created"])} · {e(x.get("state"))}</span></li>' for x in n['recent_error_issues']) or '<li class=muted>None</li>'
    cm = ''.join(f'<li>{d10(x["date"])} <span class=muted>[{e(x.get("branch"))}]</span> {e(x["title"])}</li>' for x in n.get('recent_commits', []))
    body = f"""<h1>{e(n['name'])} {badge(n['status'])}</h1><p>{e(n['description'])}</p><p class=muted>Why: {e('; '.join(n['reasons']))}</p>
<div class=card><table>
<tr><th>Repo</th><td><a href="{e(n['repo_url'])}">{e(n['repo'])}</a> (default branch {e(n.get('default_branch'))})</td></tr>
<tr><th>Registry</th><td><a href="https://registry.comfy.org/nodes/{e(n['id'])}">{e(n['id'])}</a> · publisher {e(n['publisher'])} · latest {e(n['latest_version'])} ({d10(n['latest_version_date'])}) · in Manager list: {'yes' if n['in_manager_list'] else 'no'}</td></tr>
<tr><th>Popularity</th><td>rank #{n['rank']} · {n['downloads'] or 0:,} downloads · {e(n['stars'])} stars</td></tr>
<tr><th>Tags</th><td>{' '.join(f'<a class=tag href="../category/{slug(x)}.html">{e(x)}</a>' for x in n['fn'])} {' '.join(f'<a class=tag href="../model/{slug(x)}.html">{e(x)}</a>' for x in n['md'])}</td></tr>
<tr><th>Star velocity</th><td>{('+' + str(n['s30']) + f" stars in the last {n['span']} days · {n['pw']}/week · {n['rel']}% of prior total") if n.get('s30') is not None else 'collecting (nightly snapshots started ' + e(HSINCE) + ')'}</td></tr>
<tr><th>Error issues</th><td>{e(es.get('recent_30d'))} error-titled issues opened in last 30 days (open+closed) · {e(es.get('per_100k_downloads'))} per 100K downloads · baseline {e(es.get('baseline_30d_avg'))}/month over prior 6 months ({e(es.get('baseline_180d_total'))} total) · {e(es.get('ratio_vs_baseline'))}× baseline <span class=muted>(Error spike needs ≥3, ≥2× baseline, ≥0.5 per 100K)</span></td></tr>
<tr><th>Last commit</th><td>{d10(n.get('last_commit'))} ({e(n.get('days_since_commit'))} days ago)</td></tr>
<tr><th>Open issues</th><td>{e(i.get('open_issues_sample'))}{'+' if i.get('open_issues_capped') else ''} issues, {e(i.get('open_prs'))} PRs <span class=muted>(fetched {d10(i.get('fetched'))})</span></td></tr>
<tr><th>pyproject.toml</th><td>{'present' if p.get('pyproject') is True else e(p.get('pyproject') or 'missing')} · version {e(p.get('version'))} · requires-comfyui <b>{e(p.get('requires_comfyui'))}</b> · frontend {e(p.get('frontend'))} · requires-python {e(p.get('requires_python'))} · {e(p.get('deps'))} deps</td></tr>
<tr><th>Registry ComfyUI req.</th><td>{e(n.get('registry_comfyui_version'))}</td></tr></table></div>
{forks_html(n)}<h2>Error-titled issues, last 30 days</h2><ul>{rec}</ul><h2>Open issues mentioning errors / breakage</h2><ul>{errs}</ul><h2>Recent commits</h2><ul>{cm or '<li class=muted>n/a</li>'}</ul>{SIGNUP}"""
    open(f'{S}/node/{n["id"]}.html', 'w').write(page(n['name'], body, 1))
# changes
commits = sorted([n for n in N if (dt(n.get('last_commit')) or NOW - timedelta(999)) >= WEEK], key=lambda n: n['last_commit'], reverse=True)
rel = sorted([n for n in N if (dt(n.get('latest_version_date')) or NOW - timedelta(999)) >= WEEK], key=lambda n: n['latest_version_date'], reverse=True)
newerr = [(n, x) for n in N for x in n['recent_error_issues'] if (dt(x['created']) or NOW - timedelta(999)) >= WEEK]
sc = [(n, prev[n['id']]['status']) for n in N if n['id'] in prev and prev[n['id']]['status'] != n['status']]
entered = [n for n in N if prev and n['id'] not in prev]
rising = sorted([n for n in N if n.get('s30')], key=lambda n: n['s30'], reverse=True)[:15]
forked = sorted([n for n in N if n['afork']], key=lambda n: n['afork'][0]['score'], reverse=True)
L = lambda n: f'<a href="node/{e(n["id"])}.html">{e(n["name"])}</a>'
body = f"""<h1>What changed this week</h1><p class=muted>{d10(WEEK.isoformat())} → {d10(M['generated'])}</p>{SIGNUP}
<h2>Rising this week (stars gained)</h2><ul>{''.join(f'<li>{L(n)} — +{n["s30"]} stars in {n["span"]}d ({n["rel"]}% growth)</li>' for n in rising) or f'<li class=muted>Collecting: star snapshots started {e(HSINCE)}; the first deltas appear after the next nightly run.</li>'}</ul>
<h2>Active forks of stale/quiet packs ({len(forked)})</h2><p class=muted>Automatic suggestions, not endorsements — check the fork's README.</p><ul>{''.join(f'<li>{L(n)} → <a href="{e(n["afork"][0]["url"])}">{e(n["afork"][0]["repo"])}</a>: {n["afork"][0]["ahead"]} commits ahead, last {d10(n["afork"][0]["last_commit"])}, {n["afork"][0]["stars"]} ★</li>' for n in forked[:25])}</ul>
<h2>Status changes since last run ({len(sc)})</h2><ul>{''.join(f'<li>{L(n)}: {e(o)} → {badge(n["status"])}</li>' for n, o in sc) or '<li class=muted>None (or first run — no previous snapshot)</li>'}</ul>
<h2>New registry releases ({len(rel)})</h2><ul>{''.join(f'<li>{d10(n["latest_version_date"])} {L(n)} v{e(n["latest_version"])}</li>' for n in rel)}</ul>
<h2>Packs with commits ({len(commits)})</h2><ul>{''.join(f'<li>{d10(n["last_commit"])} {L(n)} — {e(n["recent_commits"][0]["title"])}</li>' for n in commits)}</ul>
<h2>New error-titled issues ({len(newerr)})</h2><ul>{''.join(f'<li>{L(n)}: <a href="{e(x["url"])}">{e(x["title"])}</a></li>' for n, x in newerr) or '<li class=muted>None in sampled repos</li>'}</ul>
<h2>Entered the top {M['tracked']} ({len(entered)})</h2><ul>{''.join(f'<li>{L(n)}</li>' for n in entered) or '<li class=muted>n/a</li>'}</ul>"""
open(f'{S}/changes.html', 'w').write(page('What changed', body))
open(f'{S}/about.html', 'w').write(page('About', f"""<h1>Methodology</h1><ul>
<li>Pack list: Comfy Registry API (api.comfy.org/nodes, {M['registry_total']} packs) cross-checked with ComfyUI-Manager custom-node-list.json ({M['manager_list_total']} entries). Top {M['tracked']} by registry downloads with a GitHub repo.</li>
<li>Stars & downloads: registry. Last commit: <code>git ls-remote</code> + shallow treeless fetch of default branch and main/master (newest wins). pyproject.toml: raw.githubusercontent.com, parsed per the registry spec (<code>[tool.comfy] requires-comfyui</code>).</li>
<li>Issues: GitHub REST API ({e(M['github_mode'])}), cached and rotated oldest-first each run. Error issues = open issue titles matching error/broken/fail/crash/traceback/etc.</li>
<li><b>Star velocity</b> (idea from Reddit user <a href="https://www.reddit.com/user/Luke2642/">u/Luke2642</a>, who built the <a href="https://luke2642.github.io/comfyui_new_node_finder/">ComfyUI New Node Finder</a>): stars gained over the last 30 days, from nightly GitHub stargazer-count snapshots (GraphQL) starting {e(HSINCE)}. Until a full 30-day window exists the gain is over the days available. Historical backfill wasn't possible: GitHub's list-stargazers API no longer returns other people's repos.</li>
<li><b>Active forks</b> (idea from Reddit user <a href="https://www.reddit.com/user/bonalex01/">u/bonalex01</a>): for Stale and Quiet packs, up to 200 forks (newest + most-starred) are listed; forks pushed after upstream's last commit are compared against upstream's default branch, and those ahead with newer commits are ranked by commits ahead (capped at 50) ×2 + recency + 3×log2(1+stars). Automatic suggestions, not endorsements. Refreshed weekly on a rotating subset.</li>
<li><b>Categories</b>: function and model-family tags from keyword rules over the pack name, registry description, GitHub topics and README (README mentions need repeated hits), plus manual overrides for misfires. Packs can have several tags; packs with no model-specific mentions are "Generic / any".</li>
<li>Status: <b>Stale / abandoned</b> = repo gone, or no commit &gt;365 days. <b>Quiet</b> (note on Active packs) = no commit in 6–12 months. <b>Error spike</b> = worth checking recent issues (not a verdict). All three must hold: (1) ≥3 error-titled issues (open or closed, PRs excluded) opened in the last 30 days; (2) that is ≥2× the pack's own average 30-day rate over the prior 180 days (baseline floored at 1/month); (3) ≥0.5 such issues per 100K registry downloads in those 30 days (about 3× the median monthly rate across tracked packs), so big packs aren't penalized for volume. Error-titled = title matches error/broken/fail/crash/exception/traceback/not working/incompatible etc. Deprecated or non-active registry entries are shown as notes, not a status. <b>Active</b> = otherwise. Heuristic only — a stable "finished" pack may be flagged stale.</li></ul>"""))
# category / model landing pages + sitemap
def table(rows):
    return '<table><tr><th>#</th><th>Pack</th><th>Status</th><th>Downloads</th><th>Stars</th><th>Stars (30d)</th><th>Last commit</th><th>Error issues (30d)</th></tr>' + ''.join(
        f'<tr><td>{n["rank"]}</td><td><a href="../node/{e(n["id"])}.html">{e(n["name"])}</a><div class=muted>{e(n["description"][:120])}</div></td><td>{badge(n["status"])}{" <span class=\"b Unknown\">Quiet</span>" if n.get("quiet") else ""}{" <span class=\"b Fork\">Has active fork</span>" if n["afork"] else ""}</td><td>{n["downloads"] or 0:,}</td><td>{e(n["stars"])}</td><td>{("+" + str(n["s30"])) if n.get("s30") is not None else ""}</td><td>{d10(n.get("last_commit"))}</td><td>{len(n["recent_error_issues"]) or ""}</td></tr>' for n in rows) + '</table>'
urls = ['', 'changes.html', 'about.html']
for kind, field, allv in (('category', 'fn', FN_ALL), ('model', 'md', MD_ALL)):
    os.makedirs(f'{S}/{kind}', exist_ok=True)
    for v in allv:
        rows = [n for n in N if v in n[field]]; cc = Counter(n['status'] for n in rows)
        label = (f'{v} ComfyUI custom nodes' if kind == 'category' else (f'ComfyUI {v} custom nodes' if v != 'Generic / any' else 'Model-agnostic ComfyUI custom nodes'))
        title = f'{label}: which ones still work'
        intro = (f'{len(rows)} of the {M["tracked"]} most-downloaded ComfyUI custom node packs are tagged <b>{e(v)}</b>. '
                 f'{cc.get("Active", 0)} are active, {cc.get("Stale / abandoned", 0)} look stale (no commit in a year or repo gone), {cc.get("Error spike", 0)} show an error spike. '
                 'Statuses are refreshed nightly from GitHub and the Comfy Registry — check each pack page for recent issues, ComfyUI version requirements and active forks.')
        body = f'<h1>{e(title)}</h1><p>{intro}</p>{SIGNUP}{table(rows)}<p class=muted>Tags are assigned automatically from descriptions, topics and READMEs; <a href="../about.html">methodology</a>.</p>'
        html_ = page(title, body, 1).replace('<title>', f'<meta name=description content="{e(title)}. Status, last commit, stars and error reports for {len(rows)} packs, updated nightly."><title>', 1)
        open(f'{S}/{kind}/{slug(v)}.html', 'w').write(html_); urls.append(f'{kind}/{slug(v)}.html')
urls += [f'node/{n["id"]}.html' for n in N]
open(f'{S}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{d10(M["generated"])}</lastmod></url>' for u in urls) + '</urlset>\n')
open(f'{S}/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
# newsletter
os.makedirs(f'{R}/newsletter', exist_ok=True)
top50 = N[:50]; stale = [n for n in N if n['status'].startswith('Stale')]; old = [n for n in stale if (n['days_since_commit'] or 0) > 365]
pb = [n for n in N if n['status'] == 'Error spike']
nl = f"""# NodeWatch Weekly — Issue #1 ({d10(M['generated'])})

*The health report for ComfyUI custom nodes. We track the top {M['tracked']} node packs (by Comfy Registry downloads) out of {M['registry_total']:,} registered.*

## The big picture
- **{c['Active']}** of {M['tracked']} popular packs are **Active** (commit within the last year); **{len(stale)}** look **stale**, and **{len(old)}** haven't had a commit in over a year (stale), and **{sum(1 for n in N if n.get('quiet'))}** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, {sum(1 for n in top50 if n['status'].startswith('Stale'))} are stale (no commit in 12+ months), including household names:
""" + ''.join(f"  - **{n['name']}** (#{n['rank']}, {n['downloads']:,} downloads, {n['stars']} ★) — last commit {d10(n['last_commit'])}\n" for n in [n for n in top50 if n['status'].startswith('Stale')][:8]) + f"""- Only **{sum(1 for n in N if n['pyproject'].get('requires_comfyui'))}** of {M['tracked']} declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **{sum(1 for n in N if (n['days_since_commit'] or 999) <= 7)}** packs shipped commits this week; **{len(rel)}** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
""" + (''.join(f"- **{n['name']}** — {'; '.join(n['reasons'])}. Recent reports: " + '; '.join(f"[{x['title'][:80]}]({x['url']})" for x in n['recent_error_issues'][:3]) + '\n' for n in pb) or '- No unusual error spikes this week.\n') + f"""
## 🔥 Rising this week
""" + (''.join(f"- **{n['name']}** — +{n['s30']} stars in {n['span']} days\n" for n in rising[:8]) or f'- Star tracking started {HSINCE}; first numbers next week.\n') + """
## 🍴 Active forks of stale packs (suggestions, not endorsements)
""" + ''.join(f"- **{n['name']}** → [{n['afork'][0]['repo']}]({n['afork'][0]['url']}): {n['afork'][0]['ahead']} commits ahead, last commit {d10(n['afork'][0]['last_commit'])}\n" for n in forked[:6]) + """
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
