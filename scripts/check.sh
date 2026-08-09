#!/usr/bin/env bash
#
# check.sh — the local mirror of .github/workflows/check.yml.
# Run before pushing: builds the site and reports orphaned assets.
# CI adds a link crawl on top; this catches the two cheap failures locally.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "▸ build"
hugo --gc --minify --quiet
echo "  ✅ built $(find public -name '*.html' | wc -l | tr -d ' ') pages"

echo "▸ orphaned assets"
./scripts/check-orphans.sh
