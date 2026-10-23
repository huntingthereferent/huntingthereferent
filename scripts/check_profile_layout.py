#!/usr/bin/env python3
"""Validate the current public profile without freezing its wording or layout.

This guard checks the entry point, local resources, and navigability.
Research prose, headings, graphic order, and design are free to evolve.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BANNER = "assets/observational/humanity-online-banner.webp"


def check(text: str) -> list[str]:
    errors = []
    lines = text.splitlines()
    if not lines:
        return ["Profile README is empty"]

    banner = re.fullmatch(r"!\[[^\]]+\]\(([^)]+)\)", lines[0].strip())
    if not banner or banner.group(1) != BANNER:
        errors.append("The first line must link the existing profile banner")
    if not (ROOT / BANNER).is_file():
        errors.append("Profile banner asset is missing")

    introduction = next((line for line in lines[1:] if line.strip()), "")
    if not introduction.startswith("**Tracework**"):
        errors.append("Start the profile by explaining Tracework")

    badge_markers = ("[![RESEARCH]", "[![MATH]", "[![TRACEWORK]", "[![EVIDENCE]")
    badge_positions = [text.find(marker) for marker in badge_markers]
    if any(text.count(marker) != 1 for marker in badge_markers):
        errors.append("Each of the four research navigation badges must appear once")
    start = text.find("**Start here:**")
    if start < 0 or any(pos < 0 or pos >= start for pos in badge_positions):
        errors.append("Research badges must come before the primary navigation")

    for label in ("Watch Tracework", "Explore the projects", "Inspect the research register"):
        if f"[{label}](" not in text:
            errors.append(f"Primary navigation missing: {label}")

    # A missing local link is an actual defect; prose and visual choices are not.
    for destination in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        destination = destination.split("#", 1)[0]
        if not destination or "://" in destination or destination.startswith(("mailto:", "#")):
            continue
        if not (ROOT / destination).is_file():
            errors.append(f"Local link target missing: {destination}")

    for asset in re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', text):
        if "://" not in asset and not (ROOT / asset.split("#", 1)[0]).is_file():
            errors.append(f"Local image target missing: {asset}")

    return sorted(set(errors))


def main() -> int:
    errors = check(README.read_text(encoding="utf-8"))
    if errors:
        print("PROFILE PRESENTATION: FAILED")
        for error in errors:
            print(" - " + error)
        return 1
    print("PROFILE PRESENTATION: PASSED")
    print("Entry point, banner, research navigation, and local resources are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
