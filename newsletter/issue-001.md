# NodeWatch Weekly — Issue #1 (2026-11-11)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,457 registered.*

## The big picture
- **191** of 300 popular packs are **Active** (commit within the last year); **108** look **stale**, and **104** haven't had a commit in over a year (stale), and **60** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,144,397 downloads, 1209 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,483,734 downloads, 2030 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,372,862 downloads, 395 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,624,460 downloads, 6176 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,249,274 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 788,424 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 706,583 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 623,259 downloads, 1264 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **17** packs shipped commits this week; **15** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 4 error-titled issues in last 30 days vs 0.67/month baseline; 2.79 per 100K downloads — worth checking recent issues. Recent reports: [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94); [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81)

## 🔥 Rising this week
- **FastVideo** — +183 stars in 23 days
- **VRGameDevGirl Custom Nodes** — +101 stars in 23 days
- **ComfyUI-KJNodes** — +78 stars in 23 days
- **ComfyUI-WanVideoWrapper** — +77 stars in 23 days
- **rgthree-comfy** — +74 stars in 23 days
- **VNCCS - Visual Novel Character Creation Suite** — +69 stars in 23 days
- **Prompt Assistant** — +64 stars in 23 days
- **ComfyUI-DaSiWa-Nodes** — +64 stars in 23 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 114 commits ahead, last commit 2026-10-30
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **comfyui_AcademiaSD** v2.7.0 (2026-11-11)
- **ComfyUI-DaSiWa-Nodes** v0.5.44 (2026-11-11)
- **VRGameDevGirl Custom Nodes** v10.0.5 (2026-11-10)
- **Pixaroma** v1.4.252 (2026-11-10)
- **WAS Node Suite v3** v3.10.6 (2026-11-09)
- **ComfyUI-BFSNodes** v1.119.5 (2026-11-09)
- **VNCCS - Collection of utility nodes** v0.7.6 (2026-11-09)
- **ComfyUI-PlagueKind-Nodes** v1.6.2 (2026-11-08)
- **ComfyUI-Model-Manager** v2.8.7 (2026-11-08)
- **ComfyUI-KikoTools** v1.4.0 (2026-11-07)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
