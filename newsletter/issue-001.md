# NodeWatch Weekly — Issue #1 (2026-10-19)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,100 registered.*

## The big picture
- **198** of 300 popular packs are **Active** (commit within the last year); **102** look **stale**, and **98** haven't had a commit in over a year (stale), and **66** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 9 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,077,955 downloads, 1200 ★) — last commit 2025-04-14
  - **ComfyUI Impact Subpack** (#11, 2,313,917 downloads, 390 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#18, 1,584,714 downloads, 6148 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,221,602 downloads, 319 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 770,831 downloads, 454 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 687,990 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 618,373 downloads, 1097 ★) — last commit 2025-07-12
  - **ComfyUI-WD14-Tagger** (#43, 610,405 downloads, 1254 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **27** packs shipped commits this week; **14** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- No unusual error spikes this week.

## 🚀 Fresh releases this week
- **ComfyUI-DaSiWa-Nodes** v0.5.32 (2026-10-19)
- **comfyui_AcademiaSD** v2.6.4 (2026-10-19)
- **ComfyUI-Inpaint-CropAndStitch** v3.0.18 (2026-10-18)
- **DemonAlone-nodes-ComfyUI** v5.0.1 (2026-10-18)
- **ComfyUI-ppm** v1.1.14 (2026-10-18)
- **VNCCS - Visual Novel Character Creation Suite** v3.3.1 (2026-10-17)
- **ComfyUI-BFSNodes** v1.111.0 (2026-10-17)
- **D2-nodes-ComfyUI** v40.0.1 (2026-10-17)
- **ComfyUI-KikoTools** v1.2.0 (2026-10-17)
- **Basic data handling** v2.2.0 (2026-10-16)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
