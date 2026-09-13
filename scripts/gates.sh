#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/.."

[ -d public ] && [ -n "$(find public -name '*.html' -print -quit)" ] || {
  echo "❌ no built site in public/ — run hugo first" >&2; exit 1; }

echo "▸ orphaned assets";               ./scripts/checks/check-orphans.sh
echo "▸ social cards";           python3 ./scripts/checks/check-og.py
echo "▸ colour contrast";        python3 ./scripts/checks/check-contrast.py
echo "▸ css architecture";       python3 ./scripts/checks/check-css.py
echo "▸ page chrome";            python3 ./scripts/checks/check-chrome.py
echo "▸ links, duplicates and controls"; python3 ./scripts/checks/check-pages.py
echo "▸ direction safety";       python3 ./scripts/checks/check-rtl.py
echo "▸ script selectors";       python3 ./scripts/checks/check-js.py
echo "▸ html validity";          python3 ./scripts/checks/check-html.py
