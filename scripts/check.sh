#!/usr/bin/env bash
#
# check.sh — what CI runs, locally. Builds the site, then runs every gate.
# The gate list itself lives in gates.sh, so this and CI cannot disagree.

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

./scripts/gates.sh
