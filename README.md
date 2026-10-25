![Humanity, pop culture, internet culture and shared connections across the world](assets/observational/humanity-online-banner.webp)

## James Muneoka

I'm an independent builder and researcher who likes following questions across subjects, finding where explanations stop fitting what I can observe, and making things to test what happens next. My interests range from language and finite mathematics to interactive worlds, software, and the ordinary ways people learn and work. I don't claim a formal affiliation or that every experiment leads somewhere; I care about keeping the work inspectable, including when it fails.

### What I'm building

**Tracework** is the finite-system environment I'm building: a way to take a real problem, preserve its source and relationships, move through bounded states and handoffs, compare expected and observed returns, and continue from what the evidence actually supports. Different projects keep their own models while sharing a traceable path through the work.

**The version shown on GitHub is a public proof of concept and development preview**, not the complete standalone system. The repository contains working runtime components, finite mathematical examples, source-backed research, tests, and a read-only viewer. Together they demonstrate what a finite system can look like in practice: defined inputs and actions, inspectable transitions, explicit boundaries, recorded outcomes, and recoverable continuation. The public viewer shows only the evidence available to it; it is not a live view of every private process.

The broader mathematical architecture is being developed through these components. The finite examples demonstrate their own stated properties; they do not by themselves prove a universal theory or imply that every planned Tracework capability is already implemented.

[![RESEARCH](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-477765?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#research) [![MATH](https://img.shields.io/badge/MATH-FINITE_MODELS-536C91?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math) [![TRACEWORK](https://img.shields.io/badge/TRACEWORK-EXECUTION_%26_EVIDENCE-506977?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html) [![EVIDENCE](https://img.shields.io/badge/EVIDENCE-SOURCE_RECORDS-856840?style=flat-square&labelColor=111827)](PROVENANCE.md)

**Research instruments inside Tracework:** [Mathematical viewer](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math) · [ARC native records](https://huntingthereferent.github.io/autobots-assemble/live/work.html#arc) · [WORLD investigations](https://huntingthereferent.github.io/autobots-assemble/live/work.html#world) · [NIH source comparisons](https://huntingthereferent.github.io/autobots-assemble/live/work.html#nih) · [Open research inside Tracework](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math)

**Start here:** [Watch Tracework](https://huntingthereferent.github.io/autobots-assemble/live/work.html) · [Explore the projects](showcase/PROJECT_INVENTORY.md) · [Inspect the research register](RESEARCH_REGISTER.md)

## What is operating

The original mathematical research, **Tracework**, and the separate experimental projects are related but not interchangeable:

| Layer | What it does | Inspect |
| --- | --- | --- |
| **Mathematical research** | Constructs defined finite models, predictions, comparisons, and counterexamples. | [Explore in workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math) · [Mathematical source notes](showcase/MATHEMATICS.md) · [Method](docs/RESEARCH_METHOD.md) |
| **Tracework / GitHub proof of concept** | Demonstrates finite, source-linked work through states, relationships, handoffs, native returns and provenance. The GitHub viewer is a public observation surface, not the entire standalone system. | [Live execution and research view](https://huntingthereferent.github.io/autobots-assemble/live/work.html) · [Architecture](https://github.com/huntingthereferent/autobots-assemble/blob/main/ARCHITECTURE.md) |
| **Research and applications** | Test specific questions in ARC, WORLD, NIH/data work, software, interactive tools, and other independent lanes. | [Project inventory](showcase/PROJECT_INVENTORY.md) · [Selected work](SELECTED_WORK.md) |

Tracework is the **current public name** of the environment previously described in the records as the *workstation*, *Process Workstation*, or *AI-workstation*. Existing file paths, runtime identifiers, dated witnesses, and historical labels retain their original meaning. A naming change does not retroactively change their evidence.

## Selected source-pinned results

These examples show different kinds of returns, not one claim of general success.

| Investigation | Recorded observation | Evidence and limit |
| --- | --- | --- |
| **Finite A/B construction** | The distinct action words `BBAA` and `ABABB` reach `[2, 2, 1]` in a specified finite system after 14 explored states. | [Native receipt](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/views/motion/convergence-receipt.json) · [Operators](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/work/arc_like_maze/math.py). This is a result in that finite model. |
| **ARC / original SP80 SDK** | Two native entries reached official level **4/6**; a later 52-reset level-4 experiment did **not** reach level 5 or WIN. | [Level-4 native witness](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169) · [Negative follow-up](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534). Native returns, not visual approximations. |
| **NIH / AACT source comparison** | Two checksum-authenticated deposited exports share **432,597 study IDs** and differ in **1,345 status fields**. | [Archive comparison](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) · [Date-source boundary](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_AACT_OWNER_DATE_LINK.md). Reported collection dates do not establish per-study chronology. |
| **WORLD / conditional motion** | Trial 31 checked **24 conservative inequalities** through a **0.25-unit** virtual-time horizon; the three qualified hypothetical response cases lost a sufficient clearance bound before that horizon ended. | [Source record](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/ab_world/TRIAL31_SOURCE_HANDOFF.md) · [Native analytical checks](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39531157339). A bound failure is not an observed physical collision. |

[**Full evidence register — source revisions, negative controls, limits and open questions →**](RESEARCH_REGISTER.md)

## The finite constructions

### One finite example

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg" width="680" alt="Finite A/B motion showing changes under defined actions" /></a>

In this [finite construction](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py), action order changes a defined state. The rendering is derived from a specified model, not a claim about unrelated systems.

### Where separate A/B paths meet

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg" width="680" alt="Two distinct verified action paths returning to the same finite state" /></a>

A separate [convergence receipt](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md) verifies two different action histories reaching the same defined state. The two visualizations are examples of finite, checkable movement; Tracework is the infrastructure used to carry and inspect work across investigations.

## Research and development areas

| Area | Where to inspect |
| --- | --- |
| **ARC native environments** | [Inspect saved routes in workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html#arc) · [Original evidence](ARC_EVIDENCE.md) |
| **WORLD** | [Inspect in workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html#world) · [Source records](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/ab_world) |
| **Scientific data / NIH** | [Inspect in workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html#nih) · [Source-owned evidence](RESEARCH_REGISTER.md) |
| **Software and tools** | [Programs, creative interfaces, online learning and applications](showcase/PROJECT_INVENTORY.md) |
| **Tracework implementation** | [Runtime, source editions, independent work lanes and audit records](https://github.com/huntingthereferent/autobots-assemble/blob/main/TRACEWORK.md) |

## Method and scope

Specify the system and admissible actions, predict a return, execute at the relevant native boundary, compare the actual return, and preserve both witnesses and counterexamples. Keep **proposed**, **simulated**, **observed**, **independently checked**, and **still unresolved** distinct. Tracework can retain that history while work moves, but it does not replace the native source or proof criteria.

The work is independent and does not claim institutional affiliation or a completed universal theory. The current platform includes opt-in and manually admitted operations; a public viewer is not proof of a fully unattended hosted system.

### Development background

The public development record covers September–October 2026 and builds on mathematical work begun earlier. The reported direct expenditure for the setup presented here is **$20**; this is not an estimate of the project's total development cost or the value of the time invested. Working hours have not been formally tracked.

This profile and the linked research materials have been developed and revised through Tracework, previously called the AI-workstation. The record distinguishes generated documentation from the underlying definitions, source observations, tests, and unresolved questions.

[Research method](docs/RESEARCH_METHOD.md) · [Research notebook](RESEARCH.md) · [Evidence and provenance](PROVENANCE.md) · [Full project inventory](showcase/PROJECT_INVENTORY.md) · [Visual provenance](VISUAL_PROVENANCE.md)

---

*The factory must grow.*
