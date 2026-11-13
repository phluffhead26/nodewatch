# NodeWatch Weekly — Issue #1 (2026-11-13)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,488 registered.*

## The big picture
- **190** of 300 popular packs are **Active** (commit within the last year); **108** look **stale**, and **104** haven't had a commit in over a year (stale), and **60** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,149,859 downloads, 1209 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,491,300 downloads, 2030 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,377,821 downloads, 395 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,628,048 downloads, 6176 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,251,644 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 789,840 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 708,177 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 624,235 downloads, 1264 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **18** packs shipped commits this week; **16** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-Lora-Manager** — 7 error-titled issues in last 30 days vs 3.5/month baseline; 0.77 per 100K downloads — worth checking recent issues. Recent reports: [Startup warning since multi-library removal: “Failed to save folder paths: … alr](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1206); [LoRA file paths containing "%20" break previews on Windows](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1195); ["Help" button help docs open with broken layout](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1193)
- **ComfyUI-DaSiWa-Nodes** — 3 error-titled issues in last 30 days vs 0.83/month baseline; 2.07 per 100K downloads — worth checking recent issues; latest registry version deprecated. Recent reports: [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94); [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81)

## 🔥 Rising this week
- **FastVideo** — +190 stars in 25 days
- **VRGameDevGirl Custom Nodes** — +104 stars in 25 days
- **ComfyUI-KJNodes** — +81 stars in 25 days
- **rgthree-comfy** — +77 stars in 25 days
- **ComfyUI-WanVideoWrapper** — +76 stars in 25 days
- **VNCCS - Visual Novel Character Creation Suite** — +71 stars in 25 days
- **ComfyUI-GGUF** — +67 stars in 25 days
- **Prompt Assistant** — +66 stars in 25 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 114 commits ahead, last commit 2026-10-30
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI Image Saver** v1.27.0 (2026-11-12)
- **DemonAlone-nodes-ComfyUI** v5.8.2 (2026-11-12)
- **ComfyUI-DaSiWa-Nodes** v0.5.45 (2026-11-11)
- **comfyui_AcademiaSD** v2.7.0 (2026-11-11)
- **VRGameDevGirl Custom Nodes** v10.0.5 (2026-11-10)
- **ComfyUI-Spectrum-MiniMax-H3** v0.2.30 (2026-11-10)
- **Pixaroma** v1.4.252 (2026-11-10)
- **WAS Node Suite v3** v3.10.6 (2026-11-09)
- **ComfyUI-BFSNodes** v1.119.5 (2026-11-09)
- **VNCCS - Collection of utility nodes** v0.7.6 (2026-11-09)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
