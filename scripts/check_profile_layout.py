#!/usr/bin/env python3
"""Protect the current research-profile visual sequence without freezing prose.

The previous guard checked a retired profile layout and a writing/README.md
path no longer present in this repository. This baseline is the main-branch
profile immediately before the 2026-10-27 source-to-evidence documentation edit.

The guard retains banner bytes, badge links and immediate-below-banner placement, section order, and
the two source-generated finite visuals, while permitting research prose edits.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = "d1ca11e31b0313488a209051c50867b2a34a9353"
README = ROOT / "README.md"
BANNER = "assets/observational/humanity-online-banner.webp"
FINITE = "https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg"
CONVERGENCE = "https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg"
HEADINGS = (
    "## Research focus",
    "## Research method",
    "## Selected research records",
    "## Tracework",
    "## Finite A/B constructions",
    "## Technical notes and audits",
)


def frozen_file(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def visible_graphics(readme: str) -> list[str]:
    images = []
    for match in re.finditer(
        r'!\[[^\]]*\]\(([^)]+)\)|<img\b[^>]*\bsrc="([^"]+)"',
        readme,
    ):
        url = match.group(1) or match.group(2)
        if re.search(r"\.(?:svg|png|webp)(?:$|\?)", url):
            images.append(url)
    return images


def badge_line(text: str) -> str | None:
    return next((line for line in text.splitlines()
                 if line.startswith("[![RESEARCH]")), None)


def main() -> int:
    now = README.read_text(encoding="utf-8")
    old = frozen_file("README.md").decode("utf-8")
    errors = []

    # The cover is still the actual image file, not a newly inserted rendering.
    if now.splitlines()[0] != old.splitlines()[0]:
        errors.append("The first-line Humanity banner changed.")
    if (ROOT / BANNER).read_bytes() != frozen_file(BANNER):
        errors.append("The frozen Humanity banner bytes changed.")

    # Protect original graphic order and source; badges are not counted as graphics.
    expected = [BANNER, FINITE, CONVERGENCE]
    if visible_graphics(old) != expected:
        errors.append("Pinned main-branch baseline has an unexpected visual sequence.")
    if visible_graphics(now) != expected:
        errors.append(f"Graphic order/source changed: {visible_graphics(now)!r}")

    before_badges = badge_line(old)
    after_badges = badge_line(now)
    if before_badges is None or after_badges != before_badges:
        errors.append("Research badges or destinations changed.")
    elif now.count(after_badges) != 1:
        errors.append("Research badge strip is missing or duplicated.")

    # Keep the research badge strip directly below the banner, before prose.
    # Do not allow it to drift into the Tracework section or below the intro.
    expected_opening = now.splitlines()[0] + "\n\n" + (after_badges or "") + "\n\n"
    if not after_badges or not now.startswith(expected_opening):
        errors.append("Research badges must appear immediately below the banner.")
    badge_at = now.find(after_badges) if after_badges else -1
    intro_at = now.find("I investigate how relationships remain identifiable")
    nav_at = now.find("**Explore:**")
    research_at = now.find("## Research focus\n")
    if not (0 <= badge_at < intro_at < nav_at < research_at):
        errors.append("Research introduction and navigation must follow the top badges.")

    # Layout order is intentional; additions within sections may evolve.
    baseline_headings = [
        line for line in old.splitlines() if line.startswith("## ")
    ]
    current_headings = [
        line for line in now.splitlines() if line.startswith("## ")
    ]
    if tuple(baseline_headings) != HEADINGS:
        errors.append("Pinned profile baseline heading sequence is unexpected.")
    if tuple(current_headings) != HEADINGS:
        errors.append("The agreed research section order was changed.")

    if "# THE HUMAN WALL" in now:
        errors.append("The Human Wall was duplicated in the research profile.")
    if "\n# James\n" in now:
        errors.append("The redundant profile name heading returned.")

    # Keep both generated graphics associated with their existing source captions.
    finite_head = now.find("## Finite A/B constructions\n")
    first_caption = now.find("**Action order changes the state**")
    second_caption = now.find("**Different A/B paths converge**")
    first_graphic = now.find('src="' + FINITE + '" width="680"')
    second_graphic = now.find('src="' + CONVERGENCE + '" width="680"')
    next_section = now.find("## Technical notes and audits\n")
    if not (0 <= finite_head < first_caption < first_graphic <
            second_caption < second_graphic < next_section):
        errors.append("Finite A/B captions and source graphics no longer align.")

    if errors:
        print("PROFILE VISUAL LOCK: FAILED")
        for error in errors:
            print(" - " + error)
        return 1
    print("PROFILE VISUAL LOCK: PASSED")
    print("Banner, top badges, research section order, and 680px finite graphics are preserved.")
    print("Research prose may evolve without changing the agreed visual layout.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
