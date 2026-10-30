# NodeWatch Weekly — Issue #1 (2026-10-30)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,283 registered.*

## The big picture
- **193** of 300 popular packs are **Active** (commit within the last year); **106** look **stale**, and **102** haven't had a commit in over a year (stale), and **64** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 11 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,110,900 downloads, 1201 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,440,389 downloads, 2017 ★) — last commit 2025-10-26
  - **ComfyUI Impact Subpack** (#11, 2,343,025 downloads, 393 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#19, 1,603,985 downloads, 6154 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,235,574 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 779,538 downloads, 455 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 697,401 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 620,309 downloads, 1095 ★) — last commit 2025-07-12
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **25** packs shipped commits this week; **25** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **ComfyUI-DaSiWa-Nodes** — 3 error-titled issues in last 30 days vs 0.83/month baseline; 2.2 per 100K downloads — worth checking recent issues. Recent reports: [Forge visual mode fails with 2 reference images: MTMDChatHandler(_process_mtmd_p](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/86); [RTX_UpscalerRefiner Runtime Error more RAM required / disk-backed safety limit.](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/81); [H3 Enhanced Upscaler barks an out of memory error at me when basic ultimate upsc](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/77)

## 🔥 Rising this week
- **FastVideo** — +138 stars in 11 days
- **VRGameDevGirl Custom Nodes** — +64 stars in 11 days
- **ComfyUI-WanVideoWrapper** — +55 stars in 11 days
- **ComfyUI-KJNodes** — +43 stars in 11 days
- **rgthree-comfy** — +42 stars in 11 days
- **Qwen Multiangle Camera** — +42 stars in 11 days
- **VNCCS - Visual Novel Character Creation Suite** — +33 stars in 11 days
- **VNCCS - Collection of utility nodes** — +33 stars in 11 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 104 commits ahead, last commit 2026-10-21
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 450 commits ahead, last commit 2026-10-23
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 57 commits ahead, last commit 2026-10-12
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **rgthree-comfy** v1.0.2610300006 (2026-10-30)
- **ComfyUI-ppm** v1.1.21 (2026-10-29)
- **WAS Node Suite v3** v3.8.3 (2026-10-29)
- **Pixaroma** v1.4.240 (2026-10-29)
- **Deno Custom Nodes** v0.7.123 (2026-10-28)
- **ComfyUI-KikoTools** v1.3.0 (2026-10-27)
- **VNCCS - Visual Novel Character Creation Suite** v3.3.2 (2026-10-27)
- **ComfyUI-mnemic-nodes** v3.2.2 (2026-10-27)
- **DemonAlone-nodes-ComfyUI** v5.5.2 (2026-10-27)
- **VNCCS - Collection of utility nodes** v0.7.1 (2026-10-27)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
