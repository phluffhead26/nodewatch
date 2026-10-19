#!/usr/bin/env python3
"""Tag each tracked pack by FUNCTION and MODEL FAMILY (multiple allowed) using keyword rules over
name, registry description/tags, GitHub topics and README; data/category_overrides.json fixes misfires:
{"<pack id>": {"functions": [...], "models": [...]}}  (replaces) or {"add_functions"/"remove_functions"/"add_models"/"remove_models": [...]}"""
import json, os, re, subprocess, urllib.request, concurrent.futures as cf
D = os.path.join(os.path.dirname(__file__), '..', 'data')
FUNCS = {
 'Upscaling': r'upscal|super[- ]?resolution|esrgan|supir|seedvr|flashvsr|\bvsr\b',
 'Video': r'\bvideos?\b|frame[- ]?interpolat|\brife\b|\bi2v\b|\bt2v\b|\bvhs\b',
 'ControlNet & conditioning': r'controlnet|ip-?adapter|t2i[- ]?adapter|openpose|\bcanny\b|lineart|instantid|pulid|conditioning|depth ?(map|anything|estimat)|preprocessor',
 'LoRA management': r'\bloras?\b',
 'Face & portrait': r'\bfaces?\b|portrait|reactor|face ?swap|gfpgan|codeformer|instantid|pulid',
 'Masking & segmentation': r'\bmasks?\b|masking|segment|\bsam ?[23]?\b|rembg|background remov|birefnet|matting|rmbg|inspyrenet',
 'Image editing & inpainting': r'inpaint|outpaint|crop ?(and|&) ?stitch|colou?r[- ]?correct|post[- ]?process|photoshop|layer ?style|image edit',
 'Audio': r'\baudio\b|\btts\b|text[- ]to[- ]speech|\bspeech\b|\bvoice|\bmusic\b|\bsound|whisper|mmaudio|foley',
 'Text, LLM & prompting': r'\bllms?\b|\bprompts?\b|ollama|gemini|\bgpt|qwen-?vl|caption|tagger|florence|\bvlm\b|llama|chatgpt|openai',
 'Loaders, quantization & speed': r'\bgguf\b|quantiz|\bnf4\b|\bfp8\b|nunchaku|bitsandbytes|tensorrt|\bvram\b|memory|block ?swap|teacache|wavespeed|speed ?up|acceleration|offload',
 'Samplers & schedulers': r'sampler|scheduler|\bcfg\b|sigmas|guidance',
 'Workflow utilities & UI': r'workflow|utilit|\butils?\b|\blogic\b|switch|\bmath\b|metadata|show text|reroute|\bui\b|interface|manager|toolkit|toolbox|\btools?\b|save image|preview|\bnodes? pack\b|custom scripts|essentials',
 '3D': r'\b3d\b|\bmesh|trellis|hunyuan3d|gaussian splat|point ?cloud|\bglb\b',
 'Animation': r'animat|liveportrait|\bmotion\b|keyframe|\bpose transfer|frame ?pack',
}
MODELS = {
 'SD1.5': r'\bsd ?1\.5\b|\bsd15\b|stable diffusion 1\.5|\bsd1\b', 'SDXL': r'\bsdxl\b|\bpony\b|illustrious',
 'SD3': r'\bsd ?3(\.5)?\b|stable diffusion 3', 'Flux': r'\bflux', 'Wan': r'\bwan ?2\.?\d|\bwan ?video|\bwan\b|wanvideo',
 'LTX-Video': r'\bltx', 'HunyuanVideo': r'hunyuan ?video', 'Qwen-Image': r'qwen[- _]?image|qwen[- _]?edit', 'HiDream': r'hidream', 'Chroma': r'\bchroma\b',
}
# README mentions needed for a function tag (name/description/topics need only 1); None = strong fields only
README_NEED = {'Workflow utilities & UI': 10**9, 'Text, LLM & prompting': 8, 'Samplers & schedulers': 8, 'Masking & segmentation': 8, 'LoRA management': 8, 'Video': 8}
nodes = json.load(open(f'{D}/nodes.json'))['nodes']
def readme(repo):
    for f in ('README.md', 'readme.md', 'README.MD', 'Readme.md', 'README.rst', 'README'):
        try:
            with urllib.request.urlopen(f'https://raw.githubusercontent.com/{repo}/HEAD/{f}', timeout=20) as r: return r.read().decode('utf-8', 'replace')[:20000]
        except Exception: pass
    return ''
with cf.ThreadPoolExecutor(16) as ex: RM = dict(zip([n['repo'] for n in nodes], ex.map(readme, [n['repo'] for n in nodes])))
tok = os.environ.get('GITHUB_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
TOP = {}
if tok:
    repos = [n['repo'] for n in nodes]
    for i in range(0, len(repos), 50):
        ch = repos[i:i + 50]
        q = 'query{' + ' '.join(f'r{j}: repository(owner:{json.dumps(r.split("/")[0])}, name:{json.dumps(r.split("/")[1])}){{repositoryTopics(first:20){{nodes{{topic{{name}}}}}}}}' for j, r in enumerate(ch)) + '}'
        try:
            rq = urllib.request.Request('https://api.github.com/graphql', data=json.dumps({'query': q}).encode(), headers={'Authorization': f'Bearer {tok}', 'User-Agent': 'NodeWatch'})
            res = json.loads(urllib.request.urlopen(rq, timeout=60).read()).get('data') or {}
            for j, r in enumerate(ch):
                v = res.get(f'r{j}'); TOP[r] = [t['topic']['name'] for t in v['repositoryTopics']['nodes']] if v else []
        except Exception as e: print('topics error', e)
ovp = f'{D}/category_overrides.json'; OV = json.load(open(ovp)) if os.path.exists(ovp) else {}
out = {}
for n in nodes:
    strong = ' '.join([n['name'], n['repo'].split('/')[1], n['id'], n.get('description') or '', ' '.join(TOP.get(n['repo'], []))]).replace('_', ' ').replace('-', ' ').lower()
    strong_raw = ' '.join([n['name'], n['repo'], n.get('description') or '', ' '.join(TOP.get(n['repo'], []))]).lower()
    rm = RM.get(n['repo'], '').lower()
    def hit(rx, need):  # strong fields: 1 hit; README: `need` hits
        return bool(re.search(rx, strong) or re.search(rx, strong_raw)) or len(re.findall(rx, rm)) >= need
    fn = [k for k, rx in FUNCS.items() if hit(rx, README_NEED.get(k, 6))]
    md = [k for k, rx in MODELS.items() if hit(rx, 4)]
    o = OV.get(n['id'], {})
    if 'functions' in o: fn = o['functions']
    if 'models' in o: md = o['models']
    fn = [x for x in fn if x not in o.get('remove_functions', [])] + [x for x in o.get('add_functions', []) if x not in fn]
    md = [x for x in md if x not in o.get('remove_models', [])] + [x for x in o.get('add_models', []) if x not in md]
    out[n['id']] = {'functions': fn or ['Workflow utilities & UI'], 'models': md or ['Generic / any'], 'topics': TOP.get(n['repo'], []), 'readme': bool(RM.get(n['repo']))}
json.dump(out, open(f'{D}/categories.json', 'w'), indent=0)
from collections import Counter
print('functions', Counter(f for v in out.values() for f in v['functions']).most_common())
print('models', Counter(f for v in out.values() for f in v['models']).most_common())
