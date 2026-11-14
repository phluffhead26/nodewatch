# NodeWatch Weekly — Issue #1 (2026-11-14)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,501 registered.*

## The big picture
- **190** of 300 popular packs are **Active** (commit within the last year); **108** look **stale**, and **104** haven't had a commit in over a year (stale), and **60** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,152,365 downloads, 1209 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,494,819 downloads, 2030 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,380,257 downloads, 395 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#20, 1,629,577 downloads, 6176 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,252,727 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 790,487 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 708,828 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 624,680 downloads, 1264 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **22** packs shipped commits this week; **17** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-Lora-Manager** — 7 error-titled issues in last 30 days vs 3.5/month baseline; 0.76 per 100K downloads — worth checking recent issues. Recent reports: [Startup warning since multi-library removal: “Failed to save folder paths: … alr](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1206); [LoRA file paths containing "%20" break previews on Windows](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1195); ["Help" button help docs open with broken layout](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1193)
- **ComfyUI-DaSiWa-Nodes** — 4 error-titled issues in last 30 days vs 0.83/month baseline; 2.75 per 100K downloads — worth checking recent issues; latest registry version deprecated. Recent reports: [MinimaxH3 Continuity - segment decode error](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/98); [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94); [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86)

## 🔥 Rising this week
- **FastVideo** — +192 stars in 26 days
- **VRGameDevGirl Custom Nodes** — +107 stars in 26 days
- **ComfyUI-KJNodes** — +84 stars in 26 days
- **rgthree-comfy** — +78 stars in 26 days
- **ComfyUI-WanVideoWrapper** — +75 stars in 26 days
- **VNCCS - Visual Novel Character Creation Suite** — +73 stars in 26 days
- **ComfyUI-GGUF** — +70 stars in 26 days
- **Prompt Assistant** — +68 stars in 26 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 114 commits ahead, last commit 2026-10-30
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI-DaSiWa-Nodes** v0.5.49 (2026-11-14)
- **ComfyUI-PlagueKind-Nodes** v1.6.4 (2026-11-13)
- **Pixaroma** v1.4.255 (2026-11-13)
- **ComfyUI-WanVideoWrapper** v1.4.8 (2026-11-13)
- **VRGameDevGirl Custom Nodes** v10.0.6 (2026-11-12)
- **ComfyUI Image Saver** v1.27.1 (2026-11-12)
- **DemonAlone-nodes-ComfyUI** v5.8.2 (2026-11-12)
- **ComfyUI-KJNodes** v1.5.4 (2026-11-12)
- **WAS Node Suite v3** v3.10.16 (2026-11-12)
- **ComfyUI-BFSNodes** v1.121.0 (2026-11-12)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
