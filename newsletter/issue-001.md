# NodeWatch Weekly — Issue #1 (2026-11-20)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,586 registered.*

## The big picture
- **189** of 300 popular packs are **Active** (commit within the last year); **110** look **stale**, and **106** haven't had a commit in over a year (stale), and **59** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,167,536 downloads, 1213 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,515,505 downloads, 2037 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,394,109 downloads, 398 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,639,102 downloads, 6184 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,259,131 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 794,331 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 712,824 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 627,688 downloads, 1265 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **27** packs shipped commits this week; **29** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 4 error-titled issues in last 30 days vs 1.0/month baseline; 2.69 per 100K downloads — worth checking recent issues. Recent reports: [Hi-Res Regenerate crashes in `refinement_memory_budget()` when loaded-model list](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/99); [MinimaxH3 Continuity - segment decode error](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/98); [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94)

## 🔥 Rising this week
- **FastVideo** — +165 stars in 30 days
- **ComfyUI-GGUF** — +95 stars in 30 days
- **Prompt Assistant** — +89 stars in 30 days
- **ComfyUI-KJNodes** — +84 stars in 30 days
- **VRGameDevGirl Custom Nodes** — +84 stars in 30 days
- **rgthree-comfy** — +83 stars in 30 days
- **VNCCS - Visual Novel Character Creation Suite** — +82 stars in 30 days
- **ComfyUI-WanVideoWrapper** — +80 stars in 30 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 126 commits ahead, last commit 2026-11-16
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI-DaSiWa-Nodes** v0.5.60 (2026-11-20)
- **ComfyUI_Custom_Nodes_AlekPet** v1.3.0 (2026-11-20)
- **ComfyUI-VRAM-Manager** v2.5.3 (2026-11-20)
- **ComfyUI-Nunchaku QwenImage&Z-Image Turbo LoraStack** v2.6.9 (2026-11-20)
- **ComfyUI Impact Pack** v9.1.1 (2026-11-19)
- **ComfyUI-mnemic-nodes** v3.3.4 (2026-11-19)
- **DemonAlone-nodes-ComfyUI** v5.8.5 (2026-11-19)
- **Pixaroma** v1.4.262 (2026-11-19)
- **ComfyUI-KikoTools** v1.6.0 (2026-11-18)
- **ComfyUI-BFSNodes** v1.122.4 (2026-11-18)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
