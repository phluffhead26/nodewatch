# NodeWatch Weekly — Issue #1 (2026-11-06)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,375 registered.*

## The big picture
- **192** of 300 popular packs are **Active** (commit within the last year); **107** look **stale**, and **103** haven't had a commit in over a year (stale), and **63** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,130,467 downloads, 1207 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,466,121 downloads, 2025 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,360,356 downloads, 395 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,615,975 downloads, 6173 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,243,490 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 784,544 downloads, 455 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 702,927 downloads, 212 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 621,451 downloads, 1097 ★) — last commit 2025-07-12
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **21** packs shipped commits this week; **24** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 4 error-titled issues in last 30 days vs 0.67/month baseline; 2.85 per 100K downloads — worth checking recent issues; latest registry version deprecated. Recent reports: [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94); [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81)

## 🔥 Rising this week
- **FastVideo** — +162 stars in 18 days
- **VRGameDevGirl Custom Nodes** — +93 stars in 18 days
- **ComfyUI-WanVideoWrapper** — +73 stars in 18 days
- **ComfyUI-KJNodes** — +64 stars in 18 days
- **rgthree-comfy** — +59 stars in 18 days
- **ComfyUI-DaSiWa-Nodes** — +58 stars in 18 days
- **Qwen Multiangle Camera** — +53 stars in 18 days
- **ComfyUI-GGUF** — +52 stars in 18 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 114 commits ahead, last commit 2026-10-30
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **VRGameDevGirl Custom Nodes** v10.0.1 (2026-11-04)
- **ComfyUI-BFSNodes** v1.118.0 (2026-11-04)
- **VNCCS - Collection of utility nodes** v0.7.2 (2026-11-04)
- **D2-nodes-ComfyUI** v43.0.0 (2026-11-04)
- **ComfyUI-mnemic-nodes** v3.3.2 (2026-11-03)
- **Basic data handling** v2.2.1 (2026-11-03)
- **VNCCS - Visual Novel Character Creation Suite** v3.3.4 (2026-11-03)
- **WAS Node Suite v3** v3.9.5 (2026-11-03)
- **ComfyUI-DaSiWa-Nodes** v0.5.38 (2026-11-03)
- **ComfyUI-VRAM-Manager** v2.5.2 (2026-11-03)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
