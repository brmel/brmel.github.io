#!/usr/bin/env bash
#
# check.sh — the local mirror of .github/workflows/check.yml.
# Run before pushing: builds the site and reports orphaned assets.
# CI adds a link crawl on top; this catches the two cheap failures locally.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "▸ build"
# --cleanDestinationDir matters after a deletion: without it Hugo leaves the
# removed pages sitting in public/ and the next deploy resurrects them.
# --logLevel warn, not --quiet: templates raise content warnings (a missing
# resource, an unresolvable link) and --quiet swallows them, which defeats the
# point of running this before pushing.
hugo --gc --minify --cleanDestinationDir --logLevel warn
echo "  ✅ built $(find public -name '*.html' | wc -l | tr -d ' ') pages"

echo "▸ orphaned assets"
./scripts/check-orphans.sh

echo "▸ social cards"
python3 ./scripts/check-og.py

echo "▸ colour contrast"
python3 ./scripts/check-contrast.py

echo "▸ css architecture"
python3 ./scripts/check-css.py

echo "▸ page chrome"
python3 ./scripts/check-chrome.py

echo "▸ links, duplicates and controls"
python3 ./scripts/check-pages.py

echo "▸ bundle scope"
python3 ./scripts/check-bundles.py

echo "▸ direction safety"
python3 ./scripts/check-rtl.py

echo "▸ script selectors"
python3 ./scripts/check-js.py
