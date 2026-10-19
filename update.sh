#!/usr/bin/env bash
# Refresh NodeWatch data and rebuild the static site. Re-runnable.
# REST budget per run (Actions GITHUB_TOKEN = 1,000/h): fetch.py ~600 (issues + incremental issue history),
# forks.py rotating ≤30 stale/quiet packs not scanned in 7 days (~8 calls each, stops below 100 remaining).
# Stars and repo topics use GraphQL (separate budget, ~12 queries). Full fork scan: python3 scripts/forks.py --all
# Env: NW_TOP (default 300), GITHUB_TOKEN (optional; `gh auth` is used automatically if present).
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/fetch.py
python3 scripts/stars.py || echo "stars.py failed (needs a token); continuing"
python3 scripts/forks.py || echo "forks.py failed; continuing with cached forks"
python3 scripts/categorize.py || echo "categorize.py failed; continuing with cached categories"
python3 scripts/build.py
echo "Site in $(pwd)/site — preview: python3 -m http.server 8080 -d site"
