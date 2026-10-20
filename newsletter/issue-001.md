# NodeWatch Weekly — Issue #1 (2026-10-20)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,115 registered.*

## The big picture
- **198** of 300 popular packs are **Active** (commit within the last year); **102** look **stale**, and **98** haven't had a commit in over a year (stale), and **66** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 9 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,080,813 downloads, 1200 ★) — last commit 2025-04-14
  - **ComfyUI Impact Subpack** (#11, 2,316,326 downloads, 390 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#18, 1,586,301 downloads, 6148 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,222,821 downloads, 319 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 771,498 downloads, 454 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 688,805 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 618,524 downloads, 1095 ★) — last commit 2025-07-12
  - **ComfyUI-WD14-Tagger** (#43, 610,955 downloads, 1254 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **26** packs shipped commits this week; **28** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- No unusual error spikes this week.

## 🔥 Rising this week
- **VRGameDevGirl Custom Nodes** — +14 stars in 1 days
- **FastVideo** — +7 stars in 1 days
- **comfyui_AcademiaSD** — +4 stars in 1 days
- **ComfyUI_LayerStyle** — +3 stars in 1 days
- **ComfyUI-ppm** — +3 stars in 1 days
- **Pixaroma** — +3 stars in 1 days
- **rgthree-comfy** — +2 stars in 1 days
- **ComfyUI Impact Pack** — +2 stars in 1 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 100 commits ahead, last commit 2026-10-18
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 679 commits ahead, last commit 2026-10-13
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 418 commits ahead, last commit 2026-10-12
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI_MieNodes** v1.4.2 (2026-10-20)
- **DemonAlone-nodes-ComfyUI** v5.1.0 (2026-10-19)
- **ComfyUI-ppm** v1.1.15 (2026-10-19)
- **ComfyUI-DaSiWa-Nodes** v0.5.32 (2026-10-19)
- **ComfyUI-Lora-Manager** v1.2.6 (2026-10-19)
- **comfyui_AcademiaSD** v2.6.4 (2026-10-19)
- **WAS Node Suite v3** v3.5.8 (2026-10-19)
- **Prompt Stash** v1.8.0 (2026-10-18)
- **ComfyUI-Inpaint-CropAndStitch** v3.0.18 (2026-10-18)
- **ComfyUI-BFSNodes** v1.115.1 (2026-10-18)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
