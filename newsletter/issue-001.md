# NodeWatch Weekly — Issue #1 (2026-11-26)

*The health report for ComfyUI custom nodes. We track the top 300 node packs (by Comfy Registry downloads) out of 6,669 registered.*

## The big picture
- **187** of 300 popular packs are **Active** (commit within the last year); **110** look **stale**, and **106** haven't had a commit in over a year (stale), and **59** active packs are *Quiet* (6–12 months without a commit).
- In the **top 50**, 10 are stale (no commit in 12+ months), including household names:
  - **ComfyUI_essentials** (#7, 3,181,454 downloads, 1216 ★) — last commit 2025-04-14
  - **ComfyUI-Crystools** (#10, 2,535,995 downloads, 2038 ★) — last commit 2025-10-26
  - **ComfyUI_IPAdapter_plus** (#20, 1,648,253 downloads, 6190 ★) — last commit 2025-04-14
  - **ComfyUI-mxToolkit** (#21, 1,264,741 downloads, 321 ★) — last commit 2025-05-07
  - **Derfuu_ComfyUI_ModdedNodes** (#36, 797,808 downloads, 456 ★) — last commit 2024-06-22
  - **ControlAltAI_Nodes** (#39, 716,398 downloads, 211 ★) — last commit 2025-06-05
  - **ComfyUI-WD14-Tagger** (#42, 630,388 downloads, 1269 ★) — last commit 2025-07-11
  - **ComfyUI-TeaCache** (#43, 624,218 downloads, 1095 ★) — last commit 2025-07-12
- Only **13** of 300 declare a `requires-comfyui` range in pyproject.toml — so version compatibility is mostly guesswork for users.
- **36** packs shipped commits this week; **24** published a new registry release.

## 📈 Error spikes (worth checking recent issues)
- **TTS Audio Suite** — 5 error-titled issues in last 30 days vs 2.5/month baseline; 2.72 per 100K downloads — worth checking recent issues. Recent reports: [[Bug] Qwen3-ASR Shared Runtime crashes: nagisa imports OpenSeeFace's model.py](https://github.com/diodiogod/TTS-Audio-Suite/issues/387); [[Bug] Shared Runtime installation fails with `No module named 'utils.runtimes'` ](https://github.com/diodiogod/TTS-Audio-Suite/issues/382); [[Bug] MOSS-TTS 1.7B fails – missing _get_initial_cache_position](https://github.com/diodiogod/TTS-Audio-Suite/issues/381)
- **ComfyUI-DaSiWa-Nodes** — 3 error-titled issues in last 30 days vs 1.17/month baseline; 1.98 per 100K downloads — worth checking recent issues. Recent reports: [Hi-Res Regenerate crashes in `refinement_memory_budget()` when loaded-model list](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/99); [MinimaxH3 Continuity - segment decode error](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/98); [Continuity with REF2VA timeline audio reference fails: shape mismatch in audio r](https://github.com/darksidewalker/ComfyUI-DaSiWa-Nodes/issues/94)
- **AusBoss** — 5 error-titled issues in last 30 days vs 0.5/month baseline; 11.6 per 100K downloads — worth checking recent issues. Recent reports: [ComfyUI release: the pack's nightly check fails](https://github.com/ausboss/ComfyUI-AusBoss/issues/391); [Import fails on Python 3.10 (`No module named 'tomllib'`)](https://github.com/ausboss/ComfyUI-AusBoss/issues/387); [Krea2 Inpaint Masked Workflow tone match not working](https://github.com/ausboss/ComfyUI-AusBoss/issues/361)

## 🔥 Rising this week
- **FastVideo** — +114 stars in 30 days
- **VNCCS - Visual Novel Character Creation Suite** — +94 stars in 30 days
- **ComfyUI-GGUF** — +92 stars in 30 days
- **ComfyUI-WanVideoWrapper** — +87 stars in 30 days
- **Prompt Assistant** — +87 stars in 30 days
- **ComfyUI-KJNodes** — +80 stars in 30 days
- **rgthree-comfy** — +80 stars in 30 days
- **ComfyUI-Lora-Manager** — +77 stars in 30 days

## 🍴 Active forks of stale packs (suggestions, not endorsements)
- **ComfyUI-GGUF** → [molbal/ComfyUI-GGUF](https://github.com/molbal/ComfyUI-GGUF): 126 commits ahead, last commit 2026-11-16
- **ComfyUI-SaveImageWithMetaData** → [xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal](https://github.com/xxmjskxx/ComfyUI_SaveImageWithMetaDataUniversal): 684 commits ahead, last commit 2026-10-20
- **ComfyUI-WD14-Tagger** → [nestflow/ComfyUI-Booru-Tagger](https://github.com/nestflow/ComfyUI-Booru-Tagger): 58 commits ahead, last commit 2026-10-07
- **ComfyUI-SeedVR2_VideoUpscaler** → [ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT](https://github.com/ussoewwin/ComfyUI-SeedVR2-VideoUpscaler-with-TensorRT): 454 commits ahead, last commit 2026-10-28
- **Civicomfy** → [KBYSHanahira/Civicomfy](https://github.com/KBYSHanahira/Civicomfy): 67 commits ahead, last commit 2026-11-21
- **ComfyUI-Autocomplete-Plus** → [Aaalice233/ComfyUI-Autocomplete-Aaalice](https://github.com/Aaalice233/ComfyUI-Autocomplete-Aaalice): 60 commits ahead, last commit 2026-08-31

## 🚀 Fresh releases this week
- **ComfyUI-mnemic-nodes** v3.3.6 (2026-11-25)
- **WAS Node Suite v3** v3.14.10 (2026-11-24)
- **ComfyUI-ppm** v1.1.26 (2026-11-24)
- **Rebalance Pack** v2.4.4 (2026-11-24)
- **VRGameDevGirl Custom Nodes** v10.0.10 (2026-11-24)
- **ComfyUI-VideoHelperSuite** v1.7.10 (2026-11-24)
- **comfyui_AcademiaSD** v2.7.2 (2026-11-24)
- **AusBoss** v2.28.0 (2026-11-24)
- **ComfyUI-BFSNodes** v1.123.0 (2026-11-24)
- **ComfyUI-KikoTools** v1.9.0 (2026-11-24)

## 🪦 Gone missing
- **comfyui-reactor-node** — `Gourieff/comfyui-reactor-node` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-LTXVideoLoRA** — `dorpxam/ComfyUI-LTXVideoLoRA` no longer resolves on GitHub (still listed in the registry)
- **ComfyUI-SoundFlow** — `fredconex/ComfyUI-SoundFlow` no longer resolves on GitHub (still listed in the registry)
- **comfyui-upscale-by-model** — `TheBill2001/comfyui-upscale-by-model` no longer resolves on GitHub (still listed in the registry)

## Tip for node authors
Add `requires-comfyui = ">=0.3.x"` under `[tool.comfy]` in your pyproject.toml ([spec](https://docs.comfy.org/registry/specifications)) so users and tools like ComfyUI-Manager know what you support.

---
*Data: Comfy Registry API, ComfyUI-Manager node list, GitHub. Status is heuristic — "stale" can mean "finished". Methodology on the site.*
