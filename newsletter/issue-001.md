# NodeWatch Weekly — Issue #1 (2026-11-01)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,310 registered.*

## The big picture
- **193** of 300 popular packs are **Active** (commit within the last year); **106** look **stale**, and **102** haven't had a commit in over a year (stale), and **64** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,116,519 downloads, 1205 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,448,761 downloads, 2017 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,348,193 downloads, 395 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#19, 1,607,285 downloads, 6162 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,237,829 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 780,951 downloads, 455 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 699,011 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 620,648 downloads, 1097 ★) — last commit 2025-07-12
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **27** packs shipped commits this week; **23** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 3 error-titled issues in last 30 days vs 0.67/month baseline; 2.18 per 100K downloads — worth checking recent issues. Recent reports: [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81); [H3 Enhanced Upscaler barks an out of memory error at me when basic ultimate upsc](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/77)

## 🔥 Rising this week
- **FastVideo** — +143 stars in 13 days
- **VRGameDevGirl Custom Nodes** — +71 stars in 13 days
- **ComfyUI-WanVideoWrapper** — +65 stars in 13 days
- **rgthree-comfy** — +50 stars in 13 days
- **ComfyUI-KJNodes** — +49 stars in 13 days
- **Qwen Multiangle Camera** — +48 stars in 13 days
- **VNCCS - Visual Novel Character Creation Suite** — +45 stars in 13 days
- **VNCCS - Collection of utility nodes** — +40 stars in 13 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 104 commits ahead, last commit 2026-10-21
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 450 commits ahead, last commit 2026-10-23
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI-KikoTools** v1.3.1 (2026-11-01)
- **ComfyUI-DaSiWa-Nodes** v0.5.36 (2026-11-01)
- **ComfyUI Impact Pack** v8.30.0 (2026-11-01)
- **CG Use Everywhere** v8.0.1 (2026-11-01)
- **ComfyUI-SAM2** v1.1.0 (2026-11-01)
- **Prompt Stash** v1.8.1 (2026-10-31)
- **Pixaroma** v1.4.244 (2026-10-31)
- **ComfyUI-ppm** v1.1.24 (2026-10-31)
- **D2-nodes-ComfyUI** v42.0.0 (2026-10-31)
- **WM Chatterbox TTS Revised** v2.0.6 (2026-10-30)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
