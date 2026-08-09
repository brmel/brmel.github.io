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
hugo --gc --minify --quiet --cleanDestinationDir
echo "  ✅ built $(find public -name '*.html' | wc -l | tr -d ' ') pages"

echo "▸ orphaned assets"
./scripts/check-orphans.sh
