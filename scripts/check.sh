#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/.."

echo "▸ build"
hugo --gc --cleanDestinationDir --logLevel warn --printI18nWarnings --panicOnWarning
echo "  ✅ built $(find public -name '*.html' | wc -l | tr -d ' ') pages"

./scripts/gates.sh
