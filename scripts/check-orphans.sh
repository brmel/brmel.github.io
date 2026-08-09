#!/usr/bin/env bash
#
# check-orphans.sh — find asset files that nothing references.
#
# Scans assets/ and static/images/ and reports any file whose name does not
# appear in content/, layouts/, config.toml, or another asset. Catches the
# leftovers a deletion leaves behind: a stylesheet whose only consumer was a
# layout that is gone, an image whose article was removed.
#
# Whitelisted by design:
#   assets/css/extended/*.css  — PaperMod globs these into its stylesheet bundle,
#                                so they are consumed without being named anywhere.
#   static/favicon.ico, CNAME, robots.txt — served by path, never referenced.
#
# ADVISORY MODE: exits 0 while known orphans are still being cleaned up
# (issue #2). Set STRICT=1 — and flip STRICT_DEFAULT to 1 once issue #5 has
# merged — to make orphans fail the build.
#
# Portable to bash 3.2 (macOS default): no mapfile, no associative arrays.

set -euo pipefail
cd "$(dirname "$0")/.."

STRICT_DEFAULT=0
STRICT="${STRICT:-$STRICT_DEFAULT}"

SEARCH_PATHS="content layouts config.toml assets"

# Files consumed by convention rather than by name.
is_whitelisted() {
  case "$1" in
    assets/css/extended/*.css) return 0 ;;
    static/favicon.ico|static/CNAME|static/robots.txt) return 0 ;;
    *) return 1 ;;
  esac
}

count=0
orphan_list=""

while IFS= read -r asset; do
  [ -n "$asset" ] || continue
  is_whitelisted "$asset" && continue

  base=$(basename "$asset")
  # Hugo Pipes calls use asset-relative paths ("css/extended/tokens.css"),
  # markdown uses bare filenames ("blades.png"). Accept either.
  rel_from_assets=${asset#assets/}

  if grep -rqIF -- "$base" $SEARCH_PATHS --exclude="$base" 2>/dev/null; then
    continue
  fi
  if grep -rqIF -- "$rel_from_assets" $SEARCH_PATHS --exclude="$base" 2>/dev/null; then
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
echo "(advisory — set STRICT=1 to fail on orphans)"
exit 0
