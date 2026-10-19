# NodeWatch Weekly — Issue #1 (2026-10-19)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,098 registered.*

## The big picture
- **191** of 300 popular packs are **Active** (commit within the last year); **102** look **stale**, and **98** haven't had a commit in over a year (stale), and **66** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 9 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,077,730 downloads, 1200 ★) — last commit 2025-04-14
  - **ComfyUI Impact Subpack** (#11, 2,313,705 downloads, 390 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#18, 1,584,581 downloads, 6148 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,221,517 downloads, 319 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 770,774 downloads, 454 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 687,919 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 618,359 downloads, 1097 ★) — last commit 2025-07-12
  - **ComfyUI-WD14-Tagger** (#43, 610,353 downloads, 1254 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **30** packs shipped commits this week; **14** published a new registry release.

## ⚠️ Possibly broken
- **ComfyUI-KJNodes** — 4 error/breakage issues opened in last 60 days. Recent reports: [WidgetToString.IS_CHANGED fails when the optional any_input is not in the prompt](https://github.com/kijai/ComfyUI-KJNodes/issues/774); [Resize image v2 throws error with nvidia_rtx_vsr](https://github.com/kijai/ComfyUI-KJNodes/issues/773); [An error occurred during the execution of the node.](https://github.com/kijai/ComfyUI-KJNodes/issues/769)
- **rgthree-comfy** — 3 error/breakage issues opened in last 60 days. Recent reports: [cant work on new comfyui with error](https://github.com/rgthree/rgthree-comfy/issues/795); [Broken workflow drag-and-drop node positioning/style](https://github.com/rgthree/rgthree-comfy/issues/768); [Broken Preview on Power Lora Loader +  Civitai.red ](https://github.com/rgthree/rgthree-comfy/issues/765)
- **ComfyUI-VideoHelperSuite** — 3 error/breakage issues opened in last 60 days. Recent reports: [Load Video (upload) UI breaks, doesn't allow parameter changes](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/734); [plugin load failed TypeError: Cannot read properties of null (reading 'includes'](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/725); [VHS_LoadVideo: deleting an already-executed input video crashes prompt_worker on](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/717)
- **ComfyUI-RMBG** — 3 error/breakage issues opened in last 60 days. Recent reports: [ComfyUI-RMBG Fix ERROR](https://github.com/1038lab/ComfyUI-RMBG/issues/220); [load_nodes() except-handler raises NameError (module_name), so one failed option](https://github.com/1038lab/ComfyUI-RMBG/issues/217); [Florence2 (RMBG) fails with transformers 5.x — `'Florence2LanguageConfig' object](https://github.com/1038lab/ComfyUI-RMBG/issues/216)
- **ComfyUI-Lora-Manager** — 4 error/breakage issues opened in last 60 days. Recent reports: [Backslash paths are now forward slash, leading to workflows breaking](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1149); [Enrich Feature Not Working](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1133); [Failed to fetch model from CivitAI](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1127)
- **FastVideo** — 3 error/breakage issues opened in last 60 days. Recent reports: [[Bug] tests/test_fasth3_packaging.py: stale TORCH_CUDA_ARCH_LIST assertions fail](https://github.com/hao-ai-lab/FastVideo/issues/1928); [[Bug] MPS generation fails when multiprocessing worker returns output tensors](https://github.com/hao-ai-lab/FastVideo/issues/1846); [[kernel] [Feature] NVFP4 QAT: fix broken measurement plumbing and build MFU foun](https://github.com/hao-ai-lab/FastVideo/issues/1722)
- **ComfyUI MCP | Agent Panel** — 12 error/breakage issues opened in last 60 days. Recent reports: [panel_add_node SaveVideo errors on getter-only widgetId after creating node](https://github.com/artokun/comfyui-mcp-panel/issues/2306); [Fix panel_save_workflow fetch failure while websocket remains connected](https://github.com/artokun/comfyui-mcp-panel/issues/2302); [panel_set_widget / panel_edit_node cannot target nodes whose id is a non-integer](https://github.com/artokun/comfyui-mcp-panel/issues/2297)

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
