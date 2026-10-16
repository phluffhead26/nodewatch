# NodeWatch Weekly — Issue #1 (2026-10-16)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,058 registered.*

## The big picture
- **193** of 300 popular packs are **Active** (commit within the last year); **102** look **stale**, and **98** haven't had a commit in over a year (stale), and **63** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 9 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,068,842 downloads, 1199 ★) — last commit 2025-04-14
  - **ComfyUI Impact Subpack** (#11, 2,305,562 downloads, 387 ★) — last commit 2025-07-22
  - **ComfyUI_IPAdapter_plus** (#18, 1,579,494 downloads, 6143 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,217,311 downloads, 318 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 768,403 downloads, 454 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 685,106 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-TeaCache** (#42, 617,788 downloads, 1097 ★) — last commit 2025-07-12
  - **ComfyUI-WD14-Tagger** (#43, 608,533 downloads, 1244 ★) — last commit 2025-07-11
- Only **12** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **27** packs shipped commits this week; **21** published a new registry release.

## ⚠️ Possibly broken
- **ComfyUI-VideoHelperSuite** — 3 error/breakage issues opened in last 60 days. Recent reports: [Load Video (upload) UI breaks, doesn't allow parameter changes](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/734); [plugin load failed TypeError: Cannot read properties of null (reading 'includes'](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/725); [VHS_LoadVideo: deleting an already-executed input video crashes prompt_worker on](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/717)
- **ComfyUI-SeedVR2_VideoUpscaler** — 3 error/breakage issues opened in last 60 days. Recent reports: [torch.compile + GGUF + BlockSwap still fails with quantized_weight guard error i](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler/issues/649); [Compatibility shims register phantom `flash_attn` / `bitsandbytes` modules, brea](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler/issues/640); [[Windows] bitsandbytes safety stub causes custom-node import failure after Unico](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler/issues/621)
- **ComfyUI-Lora-Manager** — 3 error/breakage issues opened in last 60 days. Recent reports: [Enrich Feature Not Working](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1133); [Failed to fetch model from CivitAI](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1127); [Metadata_hook error on latest](https://github.com/willmiao/ComfyUI-Lora-Manager/issues/1097)
- **FastVideo** — 4 error/breakage issues opened in last 60 days. Recent reports: [[Bug] FastH3 regional torch.compile fails after ~5 distinct prompt lengths (Fail](https://github.com/hao-ai-lab/FastVideo/issues/1940); [[Bug] tests/test_fasth3_packaging.py: stale TORCH_CUDA_ARCH_LIST assertions fail](https://github.com/hao-ai-lab/FastVideo/issues/1928); [[Bug] MPS generation fails when multiprocessing worker returns output tensors](https://github.com/hao-ai-lab/FastVideo/issues/1846)
- **ComfyUI MCP | Agent Panel** — 12 error/breakage issues opened in last 60 days. Recent reports: [panel_add_node SaveVideo errors on getter-only widgetId after creating node](https://github.com/artokun/comfyui-mcp-panel/issues/2306); [Fix panel_save_workflow fetch failure while websocket remains connected](https://github.com/artokun/comfyui-mcp-panel/issues/2302); [panel_set_widget / panel_edit_node cannot target nodes whose id is a non-integer](https://github.com/artokun/comfyui-mcp-panel/issues/2297)

## 🚀 Fresh releases this week
- **comfyui_AcademiaSD** v2.5.5 (2026-10-16)
- **Basic data handling** v2.2.0 (2026-10-16)
- **ComfyUI-DaSiWa-Nodes** v0.5.28 (2026-10-16)
- **Pixaroma** v1.4.218 (2026-10-16)
- **ComfyUI-BFSNodes** v1.106.3 (2026-10-16)
- **ComfyUI-Krea2T-Enhancer** v1.5.0 (2026-10-16)
- **DemonAlone-nodes-ComfyUI** v4.8.0 (2026-10-15)
- **ComfyUI-KikoTools** v1.1.2 (2026-10-15)
- **ComfyUI-Tripo** v2.0.0 (2026-10-14)
- **ComfyUI Nvidia VFX Nodes** v0.2.1 (2026-10-13)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
