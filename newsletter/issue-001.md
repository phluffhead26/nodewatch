# NodeWatch Weekly — Issue #1 (2026-11-19)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,583 registered.*

## The big picture
- **189** of 300 popular packs are **Active** (commit within the last year); **110** look **stale**, and **106** haven't had a commit in over a year (stale), and **59** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,165,327 downloads, 1213 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,512,082 downloads, 2037 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,392,023 downloads, 398 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,637,689 downloads, 6184 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,258,177 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 793,754 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 712,253 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 627,249 downloads, 1265 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **26** packs shipped commits this week; **18** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 4 error-titled issues in last 30 days vs 1.0/month baseline; 2.7 per 100K downloads — worth checking recent issues. Recent reports: [Hi-Res Regenerate crashes in `refinement_memory_budget()` when loaded-model list](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/99); [MinimaxH3 Continuity - segment decode error](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/98); [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94)

## 🔥 Rising this week
- **FastVideo** — +196 stars in 30 days
- **ComfyUI-GGUF** — +97 stars in 30 days
- **VRGameDevGirl Custom Nodes** — +95 stars in 30 days
- **ComfyUI-KJNodes** — +88 stars in 30 days
- **rgthree-comfy** — +87 stars in 30 days
- **Prompt Assistant** — +87 stars in 30 days
- **VNCCS - Visual Novel Character Creation Suite** — +87 stars in 30 days
- **ComfyUI-WanVideoWrapper** — +82 stars in 30 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 126 commits ahead, last commit 2026-11-16
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI Impact Pack** v9.1.0 (2026-11-19)
- **DemonAlone-nodes-ComfyUI** v5.8.5 (2026-11-19)
- **ComfyUI-Model-Manager** v2.8.8 (2026-11-18)
- **ComfyUI Image Saver** v1.28.0 (2026-11-17)
- **ComfyUI-KikoTools** v1.5.0 (2026-11-17)
- **VRGameDevGirl Custom Nodes** v10.0.8 (2026-11-17)
- **ComfyUI F5-TTS** v1.0.28 (2026-11-16)
- **ComfyUI-DaSiWa-Nodes** v0.5.58 (2026-11-16)
- **comfyui_AcademiaSD** v2.7.1 (2026-11-16)
- **WAS Node Suite v3** v3.12.2 (2026-11-14)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
