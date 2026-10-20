#!/usr/bin/env python3
"""Protect the agreed About Me visual sequence without freezing research writing.

Baseline: the immutable 2026-10-20 profile commit, also retained as the
profile-visual-freeze-2026-10-20 branch.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = "d82e73d0c4e04ff6c6542583369e686fd9ce3929"
README = ROOT / "README.md"
BANNER = "assets/observational/humanity-online-banner.webp"
MAP = "https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/traces/internet-map.svg"
FINITE = "https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg"
CONVERGENCE = "https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg"


def frozen_file(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def section(text: str, first: str, last: str) -> str:
    if first not in text or last not in text:
        raise ValueError(f"Missing section boundary: {first} / {last}")
    return text.split(first, 1)[1].split(last, 1)[0]


def visible_images(readme: str) -> list[str]:
    images = []
    for m in re.finditer(
        r'!\[[^\]]*\]\(([^)]+)\)|<img\b[^>]*\bsrc="([^"]+)"',
        readme,
    ):
        url = m.group(1) or m.group(2)
        if re.search(r"\.(?:svg|png|webp)(?:$|\?)", url):
            images.append(url)
    return images


def main() -> int:
    now = README.read_text(encoding="utf-8")
    old = frozen_file("README.md").decode("utf-8")
    errors = []
    if now.splitlines()[0] != old.splitlines()[0]:
        errors.append("Humanity banner at the top changed.")
    if (ROOT / BANNER).read_bytes() != frozen_file(BANNER):
        errors.append("Frozen humanity banner artwork changed.")
    wall_now = section(now, "# THE HUMAN WALL\n", "## I'm James.\n")
    wall_old = section(old, "# THE HUMAN WALL\n", "## I'm James.\n")
    if wall_now != wall_old:
        errors.append("The sustained Human Wall text changed.")

    def badge_line(s: str) -> str:
        return s.split("## I'm James.\n", 1)[1].lstrip("\n").splitlines()[0]

    if badge_line(now) != badge_line(old):
        errors.append("Badges under James's name changed or moved.")

    expected = [BANNER, MAP, FINITE, CONVERGENCE]
    found = visible_images(now)
    if found != expected:
        errors.append(f"Visible graphic order/set changed: {found!r}")
    headings = [
        "# THE HUMAN WALL", "## I'm James.", "## Stories & conversations",
        "## The internet map", "## Research & selected work",
        "## How I investigate the question", "## One finite example",
        "## Research records and paths", "## Where separate A/B paths meet",
    ]
    locations = [now.find(h + "\n") for h in headings]
    if any(p < 0 for p in locations) or locations != sorted(locations):
        errors.append("The frozen profile section order changed.")

    for path in (FINITE, CONVERGENCE):
        if not re.search(r'<img\b[^>]*src="' + re.escape(path) + r'"[^>]*width="680"', now):
            errors.append(f"A/B graphic is missing its independent 680px presentation: {path}")
    for unwanted in (
        "assets/observational/people-and-work.svg",
        "assets/observational/continuity-loom.svg",
        "assets/observational/continuity-legend.svg",
        "assets/observational/movement.svg",
        "views/world-continuity/latest.svg",
    ):
        if unwanted in now:
            errors.append(f"Previously removed visual returned: {unwanted}")
    if errors:
        print("PROFILE VISUAL LOCK: FAILED")
        for e in errors:
            print(" - " + e)
        print("For an intentional layout redesign, update this guard in the same reviewed change.")
        return 1
    print("PROFILE VISUAL LOCK: PASSED")
    print("Human Wall, banner, name/badges and four visual assets remain in the frozen order.")
    print("Supporting research prose and source links may continue to evolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
