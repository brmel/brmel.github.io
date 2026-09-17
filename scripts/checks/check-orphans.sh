#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/../.."

SEARCH_PATHS="content layouts config.toml assets data"

stray=$(find static -type f \( -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' -o -name '*.webp' -o -name '*.gif' \) \
        ! -name 'favicon*' ! -name 'apple-touch-icon.png' ! -path 'static/og/*' | sort)
if [ -n "$stray" ]; then
  echo "❌ image(s) under static/, which bypasses the image pipeline:"
  echo "$stray" | sed 's/^/   /'
  echo "   move them to assets/ or the page bundle that uses them"
  exit 1
fi

orphans=""
while IFS= read -r asset; do
  case "$asset" in assets/css/extended/*.css) continue ;; esac
  base=$(basename "$asset")
  for needle in "$base" "${asset#assets/}" "${base%.*}"; do
    grep -rqIF --exclude="$base" -- "$needle" $SEARCH_PATHS && continue 2
  done
  orphans="${orphans}   ${asset}"$'\n'
done < <(find assets -type f | sort)

if [ -n "$orphans" ]; then
  echo "❌ asset(s) referenced by nothing:"
  printf '%s' "$orphans"
  exit 1
fi
echo "✅ no orphaned assets"
