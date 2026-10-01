#!/usr/bin/env python3
"""Build the portable ChatGPT plugin ZIP from its distributable files."""

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "plugin.json").read_text())
    interface = manifest["extensions"]["com.openai"]["interface"]
    for field, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000)):
        if not 0 < len(interface[field]) <= limit:
            raise ValueError(f"{field} must contain 1–{limit} characters")

    if len(interface.get("defaultPrompt", [])) > 3:
        raise ValueError("At most three starter prompts are allowed")
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if not interface.get(field, "").startswith("https://"):
            raise ValueError(f"{field} must be an HTTPS URL")

    files = {root / "plugin.json", root / "mcp.json"}
    files.update(root.glob("skills/**/*.md"))
    for field in ("logo", "composerIcon", "logoDark", "composerIconDark"):
        if field not in interface:
            continue
        asset = (root / interface[field]).resolve()
        if not asset.is_relative_to(root) or not asset.is_file():
            raise ValueError(f"Invalid or missing asset for {field}")
        if asset.stat().st_size > 5 * 1024 * 1024:
            raise ValueError(f"Asset for {field} exceeds 5 MiB")
        files.add(asset)

    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    name, version = manifest["name"], manifest["version"]
    if any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in name):
        raise ValueError("Unsafe plugin name")
    if any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_" for c in version):
        raise ValueError("Unsafe plugin version")
    archive = dist / f"{name}-{version}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for path in sorted(files):
            if path.is_symlink():
                raise ValueError(f"Symlinks are not packaged: {path}")
            bundle.write(path, f"{name}/{path.relative_to(root).as_posix()}")
    with ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError("Archive integrity check failed")
        skills = sum(p.endswith("/SKILL.md") for p in bundle.namelist())
    print(f"{archive}\n{len(files)} files; {skills} skills; listing and composer icons included")


if __name__ == "__main__":
    main()
