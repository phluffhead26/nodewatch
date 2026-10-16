#!/usr/bin/env bash
# Refresh NodeWatch data and rebuild the static site. Re-runnable; GitHub issue data is cached and
# rotated (oldest first) so repeated unauthenticated runs gradually cover all packs.
# Env: NW_TOP (default 300), GITHUB_TOKEN (optional; `gh auth login` is used automatically if present).
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/fetch.py
python3 scripts/build.py
echo "Site in $(pwd)/site — preview: python3 -m http.server 8080 -d site"
