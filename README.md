![Humanity, pop culture, internet culture and shared connections across the world](assets/observational/humanity-online-banner.webp)

AI is a routine part of building software, organizing work, and exploring ideas. It can also change a question while appearing to carry it forward: a generated explanation, program, or workflow may no longer preserve the relationship that prompted it.

This repository examines that problem through finite mathematical constructions and experiments in software, interactive environments, and scientific data. AI is used to help build and operate the research workstation. The mathematics supplies relationships to investigate; it does not automatically generate the workstation's workers, branches, or code. When an assistant attributes its own implementation choices to the mathematics, that mismatch is recorded as interpretive drift.

The work follows specifications through implementations, observed results, corrections, and further tests. The purpose is to see which relationships remain reproducible across changing conditions, and where they do not.

[![RESEARCH](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-477765?style=flat-square&labelColor=111827)](RESEARCH.md) [![MATH](https://img.shields.io/badge/MATH-FINITE_MODELS-536C91?style=flat-square&labelColor=111827)](showcase/MATHEMATICS.md) [![SYSTEMS](https://img.shields.io/badge/SYSTEMS-WORKSTATION-506977?style=flat-square&labelColor=111827)](https://github.com/huntingthereferent/autobots-assemble) [![EVIDENCE](https://img.shields.io/badge/EVIDENCE-SOURCE_RECORDS-856840?style=flat-square&labelColor=111827)](PROVENANCE.md)

**Start here:** [Watch the workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html) · [Explore the projects](showcase/PROJECT_INVENTORY.md) · [See verified results](RESEARCH_REGISTER.md)

## Selected evidence

These are reproducible or source-pinned observations, not claims that AI-generated workflows were produced by the mathematics.

| Investigation | Observed result | Original evidence and boundary |
| --- | --- | --- |
| **Finite A/B construction** | Two distinct action sequences, `BBAA` and `ABABB`, reach the same state `[2, 2, 1]` in a specified finite system, after 14 explored states. | [Native receipt](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/views/motion/convergence-receipt.json) · [Operators](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/work/arc_like_maze/math.py) · [Verifier](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/systems/workspace/ab_relational_cluster.py). This is a finite-system result, not general convergence. |
| **ARC / original SP80 SDK** | Two native entries reached official level **4/6**; a later 52-reset level-4 experiment produced **no level-5/WIN**. | [Original level-4 native run](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169) · [52-reset negative result](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534). Official game returns, not visual proxies. |
| **NIH / AACT source comparison** | Two authenticated deposited exports share **432,597 study IDs** and differ in **1,345 status fields**. Depositors report collection dates of November 4 and 9, 2022. | [Whole-archive comparison](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) · [Original owner-date linkage](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_AACT_OWNER_DATE_LINK.md). Dates are owner-attested, not independently witnessed extraction times; per-study chronology remains unresolved. |
| **WORLD / conditional finite motion** | Trial 31 checked **24 conservative inequalities** over **0.25 virtual-time units**; all three qualified hypothetical response cases lost a sufficient clearance bound within that horizon. | [Source handoff](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/ab_world/TRIAL31_SOURCE_HANDOFF.md) · [Original analytical CI](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39531157339). Not a measured collision or physical-law result. |

[**Full research register, source revisions, negative controls, and open questions →**](RESEARCH_REGISTER.md)

### What is being tested

Closed finite constructions make states, operations, and expected relationships explicit. This provides a stable reference for checking whether an implementation or explanation has changed the original question. Tests in other environments examine what remains consistent when new inputs and conditions are introduced.

AI-generated workflows are part of the working environment, not mathematical conclusions. Their usefulness and their mistakes can both be observed. A passing software test establishes its stated result; broader mathematical claims require their own evidence.

## One finite example

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg" width="680" alt="Finite A/B motion: action order changes a defined state" /></a>

This example compares action order in a [defined finite A/B construction](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py). The animation comes from the [source-owned renderer](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md); it is evidence about that model, not about human reasoning in general.

## Where separate A/B paths meet

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg" width="680" alt="Finite A/B convergence: distinct verified action paths reach the same state" /></a>

A separate [finite A/B convergence witness](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md) traces two independently checked action paths to the same state. It is a result within the specified construction, not a universal claim about unrelated systems. [Further finite experiments and limitations →](showcase/MATHEMATICS.md)

## Proof of concept in action

| Area | What you can see |
| --- | --- |
| **Research workstation** | AI-assisted workers, automated tests, execution records, and project audits. [Open workstation](https://huntingthereferent.github.io/autobots-assemble/live/work.html) |
| **Mathematics** | Original finite constructions with programs and tests showing where a relationship holds or fails. [Explore mathematics](showcase/MATHEMATICS.md) |
| **ARC and interactive environments** | Experiments that act in real game environments, compare predictions with returned states, and retain failed attempts. [ARC evidence](ARC_EVIDENCE.md) |
| **WORLD** | Simulated motion and interaction studies, including cases where a prediction reaches its limit. [WORLD research](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/ab_world) |
| **NIH and other scientific research** | Source-based comparisons and independent tests across biomedical data, biology, chemistry, economics, security, machine learning, and other fields. [Research records](RESEARCH_REGISTER.md) |
| **Software and learning tools** | Applications, interfaces, creative tools, and an online school under active development. [Project inventory](showcase/PROJECT_INVENTORY.md) |

## Detailed research and active continuations

The next section collects source-pinned observations, experiments, and test runs. **A passing test means that particular check passed**, not that every larger question has been solved. Work still in development is labeled separately.

**Selected source-pinned evidence — updated October 22, 2026.** [Current workstation source revision](https://github.com/huntingthereferent/autobots-assemble/commit/a0f4ed478122b4f4f049220900f6dea755e95f2b). These are separate lane records; open research branches are identified as **in progress**, not as merged or independently validated results.

| Lane | Source-pinned observation | Current continuation |
| --- | --- | --- |
| **ARC / original SP80 SDK** | Original SDK reached **level 4 of 6** in two reproduced native entries ([native witness](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169)); a [52-reset level-4 experiment](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534) produced **no level-5/WIN**. | Six independent [ARC-A through ARC-F continuation branches](https://github.com/huntingthereferent/autobots-assemble/pulls?q=is%3Apr+is%3Aopen+ARC) are open; [direct-observation CI](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39857776927) succeeded, which does not by itself establish new level advancement. |
| **NIH / AACT temporal** | Two authenticated AACT exports differ in **1,345 status fields** across **432,597 shared identifiers** ([comparison](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md)); reported collection dates are November 4 and 9, 2022 ([owner-date record](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_AACT_OWNER_DATE_LINK.md)). | [NIH Phase 2 lanes A–D](https://github.com/huntingthereferent/autobots-assemble/pulls?q=is%3Apr+is%3Aopen+NIH) investigate typed relations, chronology, entailment, and held-out checks; original per-study publication chronology remains unresolved. |
| **WORLD / finite motion** | [Trial 31 native checks](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39531157339) passed 59 tests; **3 qualified hypothetical fourth responses** crossed the conservative clearance-bound sufficiency limit before 0.25 virtual-time units, with **5 no-response controls**. | This is a conditional model boundary, not evidence of a fifth collision or physical measurement. [WORLD research sources](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/ab_world). |
| **Finite mathematics** | [Engine 1](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/ENGINE_ONE.md) and [Cyclic Action](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/CYCLIC_ACTION_CONTINUATION.md) provide specified finite constructions and test boundaries. | [Finite witness and counterexample index](showcase/MATHEMATICS.md); no automatic transfer of a mathematical result to other domains. |
| **Cross-disciplinary research** | The workstation has source-testing contexts and independent research contracts across disciplines. | Active draft branches include [BIO reference-sequence integrity](https://github.com/huntingthereferent/autobots-assemble/pull/463), [ECON World Bank baseline](https://github.com/huntingthereferent/autobots-assemble/pull/449), [SEC NVD metadata](https://github.com/huntingthereferent/autobots-assemble/pull/448), [CHEM formula checks](https://github.com/huntingthereferent/autobots-assemble/pull/445), [ML Iris baseline](https://github.com/huntingthereferent/autobots-assemble/pull/442), [psychology replication aggregate](https://github.com/huntingthereferent/autobots-assemble/pull/417), and [DOI metadata intake](https://github.com/huntingthereferent/autobots-assemble/pull/415). Branch existence is not a validated research outcome. |
| **Workstation / production** | [Workspace-continuity CI](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39857976499) completed successfully; [Pages deployment](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39858779353) also succeeded. | [Inspector Gadget](https://github.com/huntingthereferent/autobots-assemble/actions/workflows/inspector-gadget-all-workflows.yml) observes workflow incidents; [CI reduction proposal](https://github.com/huntingthereferent/autobots-assemble/pull/458) and [viewer counting proposal](https://github.com/huntingthereferent/autobots-assemble/pull/431) remain open. Recent protocol-test failures require inspection rather than an assumed diagnosis. |
| **Interactive tools / education** | Active implementation work includes [Science Notebook](https://github.com/huntingthereferent/autobots-assemble/pull/480), [Reading Room](https://github.com/huntingthereferent/autobots-assemble/pull/479), [Worksheet Studio](https://github.com/huntingthereferent/autobots-assemble/pull/476), and [learner dashboard](https://github.com/huntingthereferent/autobots-assemble/pull/474). | Open development branches, not verified end-user browser acceptance. |

**Evidence boundary:** a successful run establishes its stated checks. Workflow activity, draft pull requests, and generated implementations are recorded separately from mathematical conclusions.

[**Inspect the research register and original witnesses →**](RESEARCH_REGISTER.md) · [Evidence types and limits](PROVENANCE.md) · [Selected case studies](SELECTED_WORK.md)

### Method note — testing relationships across workflow sequences

The research uses finite mathematical relationships as reference conditions. AI-assisted implementations and workflow results are compared against those conditions; agreement in a written explanation does not establish mathematical correspondence.

A single workflow may be insufficient to characterize the behavior of a sequence. The current question is whether repeated execution, interruption, and correction produce distinguishable patterns over time. The proposed wave-like behavior remains a hypothesis, not a measured result.

The [Unstupid harness](https://github.com/huntingthereferent/autobots-assemble/tree/main/interfaces/math) provides finite-world probes and scripted challenge tests. Live AI-agent conditioning and its effect on subsequent task performance have not yet been established.

### Research method

A bounded test records its source, predicted change, permitted action or transformation, returned result, and independent comparison. Failed predictions remain visible. Mathematical correspondence, executable behavior, language interpretation, and physical measurement each require their own evidence.

[Operational research method](docs/RESEARCH_METHOD.md) · [Research notebook](RESEARCH.md) · [Language Referent / A/B](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md)

### Background

This is independent work, not a claim of institutional affiliation or a finished theory. Research claims stand or fall on their sources, test conditions, and limits.

**Total cost for everything presented here: $20.**

**Time:** The documented development spans at least one month (September–October 2026), with earlier groundwork predating those records. Total working hours have not been tracked.

## Expansion model

The operational pattern is **propose or construct → test → audit → retain evidence → continue**. A supported output can be considered for a further pass, and additional workers or branches can be introduced under explicit evidence, authorization, and resource conditions. Reaching a cap calls for inspecting an admissible alternate construction or expanding available resources; it does not guarantee unlimited continuation.

| Existing research / infrastructure | Capacity unlocked by expansion | Potential new capability |
| --- | --- | --- |
| Finite A/B mathematics and construction engines | More CPU cores, RAM, parallel search, formal verification tools | Larger candidate spaces, deeper correspondence checks, independent proof and counterexample searches |
| Language referent and regrounding records | Local models, speech/text datasets, repeatable evaluation environments | Controlled language experiments, multilingual comparison, auditable representation changes |
| Native ARC experiments | Parallel isolated runtimes, faster replay, durable checkpoints | Wider action-search experiments, systematic failure analysis, repeatable evaluations |
| A/B WORLD and interactive simulations | Accelerated simulation, more memory, instrumentation | Larger world ensembles, parameter sweeps, eventual hardware-in-the-loop experiments |
| NIH / temporal source comparison | Local data lake, databases, high-throughput storage and compute | Larger source reconciliations, lineage checks, reproducible scientific data audits |
| Workstation workers and handoffs | Dedicated servers, job queues, orchestration, isolated execution | More simultaneous bounded workers, durable handoffs, scheduled verification, recovery after interruption |
| Software foundations and product prototypes | Build farms, test infrastructure, staging and production hosting | Professional QA, packaged software, services, deployable products |
| Audit viewer and provenance records | Indexed artifact storage, test dashboards, independent runners | Per-project evidence inspection, reproducible audit packages, cross-run comparison |

## Infrastructure progression

| Environment | Operational gain |
| --- | --- |
| Current GitHub and local workstation | Multiple active research lanes with constrained compute, execution time, and manual continuation |
| Dedicated local workstation and servers | Larger memory and storage, local models, parallel workers, persistent experiments, automated build and audit queues |
| Private compute laboratory | Cluster scheduling, isolated environments, large-scale simulation, shared datasets, redundant storage, continuous evaluation |
| Advanced research and engineering facility | Specialized compute, laboratory instruments, fabrication, physical prototypes, independent engineering and verification |
| Product and research operations | Reproducible releases, deployed systems, maintenance, security, customer-facing applications, and continuing research |

These are possible capabilities unlocked by equipment, engineering, and funding—not claims that all have already been implemented. Specific workloads must be benchmarked and integrations validated. The research remains portable in intent; each new execution environment has its own technical and evidentiary requirements.

**Current reviewed evidence (October 21, 2026):** [Research register](RESEARCH_REGISTER.md) · [Historical provenance](PROVENANCE.md) · [Research overview](RESEARCH.md) · [Mathematical constructions](showcase/MATHEMATICS.md) · [Language referent](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md) · [Workstation](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/README.md) · [Research method](docs/RESEARCH_METHOD.md)

[**Research overview**](RESEARCH.md) · [Method](docs/RESEARCH_METHOD.md) · [Evidence register](RESEARCH_REGISTER.md) · [Selected cases](SELECTED_WORK.md) · [Live research viewer](https://huntingthereferent.github.io/autobots-assemble/live/)

---

## Research records and paths

| Path | What is there |
| --- | --- |
| [Selected implementations](SELECTED_WORK.md) | Concrete code and investigations |
| [Complete inventory](showcase/PROJECT_INVENTORY.md) | The larger range of work, including unfinished lanes |
| [Research evidence and limits](PROVENANCE.md) | What is observed, inferred, independently checked or still open |
| [Source-pinned research register](RESEARCH_REGISTER.md) | Exact inputs, published witnesses, negative controls, and what remains unproven |
| [Source index](showcase/SOURCE_INDEX.md) | Entry points to implementation records |
| [Finite-state correspondence](docs/FINITE_STATE_CONJUGACY.md) | Domain-specific mathematics, not a model of people |
| [Native ARC runs](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs) | Recorded actions and replay evidence |
| [Workstation](https://github.com/huntingthereferent/autobots-assemble/tree/main/systems/workspace) | Workers, handoffs, workflows and independent verification |
| [Visual provenance](VISUAL_PROVENANCE.md) | How the words and illustrations relate without replacing one another |

[Research method](docs/RESEARCH_METHOD.md) · [Visual provenance](VISUAL_PROVENANCE.md)

*AI assists with workflows, code, and writing. Source specifications, execution results, interpretations, and corrections remain distinguishable in the research record.*
