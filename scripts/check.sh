#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/.."

echo "▸ build"
hugo --gc --minify --cleanDestinationDir --logLevel warn
echo "  ✅ built $(find public -name '*.html' | wc -l | tr -d ' ') pages"

./scripts/gates.sh
