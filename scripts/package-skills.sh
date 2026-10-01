#!/usr/bin/env bash
# Packages each skill for surfaces that don't read this plugin directly.
#   ./scripts/package-skills.sh          -> dist/<skill>.zip (Claude.ai: Settings → Capabilities → Skills → Upload)
#   ./scripts/package-skills.sh --codex  -> also copies the skills into ~/.codex/skills
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
dist="$root/dist"
rm -rf "$dist" && mkdir -p "$dist"

for skill in "$root"/skills/*/; do
  name="$(basename "$skill")"
  (cd "$root/skills" && zip -qr "$dist/$name.zip" "$name")
  echo "packaged dist/$name.zip"
done

if [[ "${1:-}" == "--codex" ]]; then
  target="${CODEX_HOME:-$HOME/.codex}/skills"
  mkdir -p "$target"
  for skill in "$root"/skills/*/; do
    name="$(basename "$skill")"
    rm -rf "${target:?}/$name"
    cp -R "$skill" "$target/$name"
    echo "installed $target/$name"
  done
fi
