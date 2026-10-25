# NodeWatch Weekly — Issue #1 (2026-10-25)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,203 registered.*

## The big picture
- **195** of 300 popular packs are **Active** (commit within the last year); **104** look **stale**, and **100** haven't had a commit in over a year (stale), and **66** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,096,231 downloads, 1201 ★) — last commit 2025-04-14
  - **ComfyUI Impact Subpack** (#11, 2,330,000 downloads, 393 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#18, 1,595,167 downloads, 6154 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,229,455 downloads, 320 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#35, 775,782 downloads, 455 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#38, 693,307 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#41, 619,425 downloads, 1095 ★) — last commit 2025-07-12
  - **ComfyUI-WD14-Tagger** (#42, 614,053 downloads, 1259 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **19** packs shipped commits this week; **13** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 3 error-titled issues in last 30 days vs 0.83/month baseline; 2.24 per 100K downloads — worth checking recent issues. Recent reports: [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81); [H3 Enhanced Upscaler barks an out of memory error at me when basic ultimate upsc](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/77)

## 🔥 Rising this week
- **FastVideo** — +95 stars in 6 days
- **VRGameDevGirl Custom Nodes** — +37 stars in 6 days
- **Qwen Multiangle Camera** — +32 stars in 6 days
- **ComfyUI-KJNodes** — +28 stars in 6 days
- **rgthree-comfy** — +23 stars in 6 days
- **ComfyUI Nvidia VFX Nodes** — +19 stars in 6 days
- **ComfyUI-Easy-Use** — +16 stars in 6 days
- **VNCCS - Visual Novel Character Creation Suite** — +16 stars in 6 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 100 commits ahead, last commit 2026-10-18
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 679 commits ahead, last commit 2026-10-13
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 418 commits ahead, last commit 2026-10-12
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI-BFSNodes** v1.115.33 (2026-10-24)
- **Deno Custom Nodes** v0.7.122 (2026-10-24)
- **WM Chatterbox TTS Revised** v2.0.5 (2026-10-23)
- **ComfyUI-ppm** v1.1.17 (2026-10-22)
- **ComfyUI-Model-Manager** v2.8.6 (2026-10-22)
- **ComfyUI-Inpaint-CropAndStitch** v3.0.20 (2026-10-21)
- **DemonAlone-nodes-ComfyUI** v5.3.1 (2026-10-21)
- **ComfyUI_MieNodes** v1.4.4 (2026-10-21)
- **ComfyUI-DaSiWa-Nodes** v0.5.33 (2026-10-21)
- **comfyui_AcademiaSD** v2.6.4 (2026-10-19)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
