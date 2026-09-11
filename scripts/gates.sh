#!/usr/bin/env bash
#
# gates.sh — every gate, run against an existing public/.
#
# The list lives here and nowhere else. It used to live in check.sh and again in
# .github/workflows/check.yml, and the two drifted: four gates were added
# locally and never wired into CI, so the checks the repo relies on were not the
# checks that ran. Build the site, then call this — locally, on a pull request,
# and before a deploy.

set -euo pipefail
cd "$(dirname "$0")/.."

[ -d public ] && [ -n "$(find public -name '*.html' -print -quit)" ] || {
  echo "❌ no built site in public/ — run hugo first" >&2; exit 1; }

echo "▸ orphaned assets";               ./scripts/check-orphans.sh
echo "▸ social cards";           python3 ./scripts/check-og.py
echo "▸ colour contrast";        python3 ./scripts/check-contrast.py
echo "▸ css architecture";       python3 ./scripts/check-css.py
echo "▸ page chrome";            python3 ./scripts/check-chrome.py
echo "▸ links, duplicates and controls"; python3 ./scripts/check-pages.py
echo "▸ bundle scope";           python3 ./scripts/check-bundles.py
echo "▸ direction safety";       python3 ./scripts/check-rtl.py
echo "▸ script selectors";       python3 ./scripts/check-js.py
