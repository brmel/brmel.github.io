#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/../.."

STRICT_DEFAULT=1
STRICT="${STRICT:-$STRICT_DEFAULT}"

SEARCH_PATHS="content layouts config.toml assets"

is_whitelisted() {
  case "$1" in
    assets/css/extended/*.css) return 0 ;;
    static/favicon.ico|static/CNAME|static/robots.txt) return 0 ;;
    *) return 1 ;;
  esac
}

stray=$(find static -type f \( -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' -o -name '*.webp' -o -name '*.gif' \) \
        ! -name 'favicon*' ! -name 'apple-touch-icon.png' ! -path 'static/og/*' 2>/dev/null | sort)
if [ -n "$stray" ]; then
  echo "❌ image(s) under static/, which bypasses the image pipeline:"
  echo "$stray" | sed 's/^/   /'
  echo "   move them to assets/ or the page bundle that uses them"
  exit 1
fi

count=0
orphan_list=""

while IFS= read -r asset; do
  [ -n "$asset" ] || continue
  is_whitelisted "$asset" && continue

  base=$(basename "$asset")
  stem=${base%.*}
  rel_from_assets=${asset#assets/}

  if grep -rqIF -- "$base" $SEARCH_PATHS --exclude="$base" 2>/dev/null; then
    continue
  fi
  if grep -rqIF -- "$rel_from_assets" $SEARCH_PATHS --exclude="$base" 2>/dev/null; then
    continue
  fi
  if grep -rqIF -- "$stem" $SEARCH_PATHS --exclude="$base" 2>/dev/null; then
    continue
  fi

  count=$((count + 1))
  orphan_list="${orphan_list}   ${asset}"$'\n'
done <<EOF
$(find assets static/images -type f 2>/dev/null | sort)
EOF

if [ "$count" -eq 0 ]; then
  echo "✅ no orphaned assets"
  exit 0
fi

echo "⚠️  ${count} orphaned asset(s) — referenced by nothing:"
printf '%s' "$orphan_list"

if [ "$STRICT" = "1" ]; then
  echo
  echo "❌ failing: STRICT=1"
  exit 1
fi

echo
echo "(advisory — STRICT=0)"
exit 0
