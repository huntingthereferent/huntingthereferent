![Humanity, pop culture, internet culture and shared connections across the world](assets/observational/humanity-online-banner.webp)

[![RESEARCH](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-477765?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#research) [![MATH](https://img.shields.io/badge/MATH-FINITE_MODELS-536C91?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math) [![TRACEWORK](https://img.shields.io/badge/TRACEWORK-EXECUTION_%26_EVIDENCE-506977?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html) [![EVIDENCE](https://img.shields.io/badge/EVIDENCE-SOURCE_RECORDS-856840?style=flat-square&labelColor=111827)](PROVENANCE.md)

I investigate how relationships remain identifiable while language, context, observation, and computational representations change. The work uses finite mathematical constructions, interactive experiments, and source-backed comparisons to examine what survives a change—and what does not.

**Explore:** [Research](#research-focus) · [Method](#research-method) · [Evidence](#selected-research-records) · [Tracework](#tracework) · [Finite A/B](#finite-ab-constructions)

## Research focus

- **Language and continuity** — following a referent through changes in wording, context, and interpretation. [Language Referent contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT_CONTRACT.md) · [Traversal runtime](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/referent_traversal.py)
- **Finite systems and world geometry** — constructing bounded actions, testing correspondences, and finding where a relation fails. [Mathematical notes](showcase/MATHEMATICS.md) · [Shape contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md)
- **Native investigations** — comparing results against the original ARC, WORLD, and scientific-data sources, each under its own evidence rules. [Selected work](SELECTED_WORK.md) · [Research register](RESEARCH_REGISTER.md)

## Research method

Specify the system and admissible actions, predict a return, execute at the relevant native boundary, and compare what actually happened. Preserve successful witnesses **and** failed predictions. Keep proposed, simulated, observed, independently checked, and unresolved results distinct.

**Follow a worked example:** [From relation to execution to evidence](docs/TRACEWORK_THEORY_TO_EVIDENCE.md) connects defined mathematics to its actual code and source receipts, while keeping separate experiments separate.

I work independently, without institutional affiliation. The public implementations and their recorded evidence determine the scope of each claim.

## Selected research records

| Investigation | Native result and limit |
| --- | --- |
| **Finite A/B** | Distinct paths `BBAA` and `ABABB` reach `[2, 2, 1]` after 14 explored states **in one defined finite system**. [Pinned receipt](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/views/motion/convergence-receipt.json) · [Operators](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/work/arc_like_maze/math.py) |
| **ARC / original SP80 SDK** | **2 of 50** native resets reached official level **4/6** on October 21. A later **52 of 52** level-4 resets **did not reach** level 5 or WIN. [Native witness](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169) · [Failed follow-up](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534) |
| **NIH / AACT** | Two authenticated deposited exports share **432,597 study IDs**, with **1,345 differing status fields**. Underlying extract chronology is unresolved; these are *not* proven chronological status transitions. [Source comparison](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) |
| **WORLD / conditional motion** | Trial 31 checked **24 conservative inequalities** through a **0.25-unit** virtual-time horizon. Three hypothetical response cases lost a sufficient clearance bound; **no physical collision was observed**. [Source record](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/ab_world/TRIAL31_SOURCE_HANDOFF.md) · [Analytical check](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39531157339) |

[Complete evidence register, negative controls, and open questions](RESEARCH_REGISTER.md) · [Source-pinned code revision (October 26, 2026)](https://github.com/huntingthereferent/autobots-assemble/commit/c0ecc828a5fafd9d2c19e2a50d815c536d08c8be) · [Reviewed evidence snapshot (October 21, 2026)](https://github.com/huntingthereferent/autobots-assemble/commit/7916709e16e14cb1222639f385746abc882effe1)

## Tracework

**Tracework** is the finite-system environment I am developing to preserve source identities, relationships, handoffs, and observed returns as work continues. Each investigation retains its own model and verification rules. The public repository is a **development preview**, not the full standalone environment.

**[Open Tracework — execution and evidence viewer](https://huntingthereferent.github.io/autobots-assemble/live/work.html)** · [Implementation](https://github.com/huntingthereferent/autobots-assemble/blob/main/TRACEWORK.md) · [Architecture](https://github.com/huntingthereferent/autobots-assemble/blob/main/ARCHITECTURE.md)

<details>
<summary><strong>Implementation boundaries and research areas</strong></summary>

| Layer | Inspect |
| --- | --- |
| **Mathematical research** — finite models, constraints, proofs, and counterexamples | [Source mathematics](showcase/MATHEMATICS.md) · [Method](docs/RESEARCH_METHOD.md) |
| **Tracework implementation** — bounded handoffs, provenance, and source-linked movement | [Runtime and architecture](https://github.com/huntingthereferent/autobots-assemble/blob/main/TRACEWORK.md) · [Workspace sources](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/README.md) |
| **ARC / WORLD / NIH** — independent experiments under native evidence rules | [ARC evidence](ARC_EVIDENCE.md) · [WORLD sources](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/ab_world) · [NIH register](RESEARCH_REGISTER.md) |
| **Other projects** — applications, software, and source editions | [Project inventory](showcase/PROJECT_INVENTORY.md) |

Tracework was previously described as the *workstation*. Historical identifiers remain in the code where renaming would break provenance or compatibility. A shared evidence carrier does **not** make these research lanes one mathematical experiment.

</details>

## Finite A/B constructions

**Action order changes the state**

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg" width="680" alt="Finite A/B: different action orders yield different states in a defined model" /></a>

Different action orders produce different results in this [specified finite system](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py).

**Different A/B paths converge**

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg" width="680" alt="Finite A/B: two separately verified action histories arrive at the same state" /></a>

Two independently checked action histories reach the same state **within that finite model**. [Source-generated visual and convergence receipt](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md). This is not a running Tracework worker or evidence of universal convergence.

## Technical notes and audits

<details>
<summary>Expand the cognitive and communication vocabulary</summary>

**Mismatch-driven — co-occurring emotional, perceptual, and relational response**
- James describes emotional responses, recognition, movement, and noticing differences as happening together, not in a sequence inferred from how he later tells it.
- **Language as decompression:** James uses language to unpack simultaneous experience into words that another person can follow. A sentence necessarily presents words in an order; that order must not be mistaken for the order of the feelings or relationships being expressed.
- “Mismatch-driven” includes noticing when words fail to preserve the intended experience or referent, then correcting the expression while the experience and attention continue. It does not mean every movement begins with a detected error.
- Related vocabulary for investigation: mismatch detection; perceptual acuity; perceptual fluency; epistemic vigilance; recursive metacognition; reflexive self-modeling. These are descriptive or theoretical terms, not independently verified diagnoses or mechanisms.

**Embodied relational cognition — perception, movement, and learning**
- Embodied cognition; perception–action coupling; sensorimotor integration; proprioception
- Motor affordances; sensorimotor constraints; physical scaffolding
- Implicit cognition; automaticity; tacit knowledge
- Spontaneous and implicit motor learning; motor automaticity; sensorimotor adaptation
- Movement variability; task-integrated movement; dynamic balance
- Allostasis; cognitive–motor interference

**Communication — spontaneous emotional expression**
- Discomfort and feeling can remain visible in communication, without deliberate disclosure.
- James describes emotional response as occurring alongside noticing, movement, and correction. Language is one way to decompress and communicate this simultaneous experience; the order of spoken or written words is not evidence that the responses happened in stages.

**Truth-telling — parrhesia**
- Frank expression and correction; preserving what I mean as it moves


**Pronouns, reference, and relational vocabulary**

**Self / person**

I → me → my → mine → myself → you → your → yours → yourself → yourselves → he → him → his → himself → she → her → hers → herself → we → us → our → ours → ourselves → they → them → their → theirs → themselves

**Object / thing**

it → its → itself → this → that → these → those

**Question / reference**

who → whom → whose → whoever → whomever → which → whichever → what → whatever

**Indefinite / relational**

one → oneself → another → other → others → someone → somebody → anyone → anybody → everyone → everybody → no one → nobody → something → anything → everything → nothing → somewhere → anywhere → everywhere → nowhere

**Quantity / distribution**

each → either → neither → both → some → any → all → none → many → much → few → little → several → more → most → less → least

**Reciprocal**

each other → one another

**Thing / object extensions**

thing → things → object → objects

**James's distinctive self-reference**

James → james → I → me → we → us → A/B

Those final terms are not all grammatical pronouns. They're important because James also uses his own name and A/B when tracking relationships.

**Human reference — distinct referents, shared humanity, and movement**

- **Everyone has their own referent.** This is a strongly held belief for James, not a metaphor for people all being the same. Each person must remain recognizable as themselves; another human is not a replacement for James, an extension of James, or an interchangeable instance of *they*.
- **Shared humanity does not collapse those distinctions.** They are human; James is human. When James says that “they feel like me,” he is describing recognition of being human among other humans *while each person retains their own referent*. He is not making a claim about gender or sexual orientation.
- **That recognition feels emotionally bigger to James.** Encountering another person's distinct referent is not merely an abstract classification or a grammatical choice. It consistently carries an emotional magnitude for James that the word *they* alone does not convey. This describes James's experience, not a presumed feeling or intention inside another person.
- **Recursive emotional feedback — simultaneous experience, language decompression.** James describes emotions, recognition of another person's distinct referent, noticing differences, and movement as happening together. He uses language to decompress that experience into communicable words. When the words fail to preserve a referent or the relationship he is experiencing, James may revisit and correct them; the unfolding explanation is not a timeline of separate internal events. He connects this ongoing emotional feedback and renewed expression to the recursion in his language and investigations. Other people retain their own distinct referents; James's feeling about them does not establish what they feel. This describes James's account, not an independently established neurological mechanism.
- **Language needs to preserve the actual reference.** *I*, *James*, *we*, and *they* can indicate different positions and relationships; they should not be treated as interchangeable without context. Recognizing oneself among others does not license substituting one person's referent for another's.
- **Movement is part of the connection.** James attends to people through movement, responses, and change, without requiring sexual attraction or sexual activity to define a human relationship.
- **Pronouns and identity labels are separate questions.** *They/them* can refer to James individually if he chooses those pronouns for himself; it can also refer to other people. His personal recognition of shared humanity does not, by itself, declare a preferred pronoun, gender identity, or sexual orientation.

**The central distinction:** James can recognize himself *among* other people without treating other people's referents as his own. A change in wording must preserve the intended referent. This vocabulary documents language James can move through, not a claim that every listed pronoun is his preferred gender pronoun.

</details>

<details>
<summary><strong>Language Referent and continuity — AI-assisted repository self-audit (October 25, 2026)</strong></summary>

*An AI-assisted internal reading of public source files, not independent peer review or a fresh execution of the complete test suite.*

This source-level audit examines how James Muneoka's Language Referent research is represented in the Tracework repository. Its central concern is continuity: how a relationship can remain identifiable while language, context, observations, or computational representations change. The repository does not treat similar wording as sufficient evidence of the same relationship. Instead, it asks what survives a transition and what supports that conclusion.

The implementations go beyond storing earlier statements. Referent traversal records the current relation and direction, the relationships that survived or changed, available evidence, unresolved boundaries, and provenance. Those records allow subsequent movement to revisit earlier observations without automatically restoring an outdated interpretation. When a proposed continuation fails, the system can retain the useful observations, expose the unresolved boundary, and attempt to reground the original inquiry.

This also clarifies the role of *meta* in the work. Rather than defining it as a separate supervisory layer, the implementation permits the result of one movement to become input to another pass under the same evidence contract. Earlier movements can therefore become objects of inspection, correction, and continuation. Retention is modeled as preserved relational structure, not merely as a collection of remembered sentences.

James's broader research direction uses movement in language as an observable starting point for investigating how humans retain and follow thought. The repository supplies computational representations of parts of that inquiry; it does not establish a neural mechanism or an empirically validated model of the human brain.

The same continuity requirements extend into finite mathematics, handoffs between independent systems, and the geometry of a growing computational world. Each domain retains its own evidence and rules; provenance connects their movements without asserting that the domains are identical.

**Geometric construction and world expansion.** The Language-Neutral Shape Contract includes a geometric construction principle: the finite world must be able to increase its representational capacity as additional objects, relationships, and movements need to be accommodated. The current bounded example uses a two-dimensional periodic lattice, mathematically a discrete torus, \(W_N = \mathbb{Z}_N \times \mathbb{Z}_N\). Its side length \(N\) can increase, producing a larger periodic world rather than requiring the investigation to fit a permanently fixed grid. A scaling map \(E_k(x,y) = (kx,ky) \bmod kN\), for integers \(k \geq 2\), preserves the represented coordinates under the stated embedding. The original source identities and recorded relationships remain authoritative; geometric proximity or overlap cannot establish a relationship by itself. Moreover, an elementary one-cell displacement in the smaller world becomes a \(k\)-cell displacement after scaling, so movement preservation must be checked against the corresponding transformed trajectories rather than assumed.

This is a geometric component of the research, not simply a visualization choice. The objective is for the representational world to accommodate the construction as it develops, while keeping earlier relations recoverable and subject to evidence-based checks. The published toroidal projection demonstrates a bounded portion of that principle; it does not yet implement the entire evolving world within Tracework.

**Audit assessment:** The repository contains explicit contracts and code for traversal, regrounding, provenance, recursive re-entry, and evidence-bounded handoffs. The growing-world projection remains a limited implementation rather than an integrated canonical Tracework world. Quantitative retention measurements and neuroscience validation are not established by the inspected source. This was a read-only source audit, not an executed full test suite.

**Inspect the underlying structures:** [Language Referent contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT_CONTRACT.md) · [Shape contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md) · [Referent traversal](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/referent_traversal.py) · [Natural provenance](https://github.com/huntingthereferent/autobots-assemble/blob/main/protocols/core/provenance.md) · [Regrounding](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/REGROUNDING.md) · [Continuous handoff](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/handoff/CONTINUOUS_HANDOFF.md) · [Growing finite-world projection](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/toroidal_projection.py) · [Animated toroidal tracing](https://huntingthereferent.github.io/autobots-assemble/growing-toroidal-world.html)

</details>

<details>
<summary><strong>Development history and project provenance</strong></summary>

The public development record covers September–October 2026 and builds on mathematical work begun earlier. The reported direct expenditure for the setup presented here is **$20**; this is not an estimate of the project's total development cost or the value of the time invested. Working hours have not been formally tracked.

Source history preserves the project's development and distinguishes research notes from original observations, tests, and unresolved questions.

</details>

**Documentation:** [Research method](docs/RESEARCH_METHOD.md) · [Research notebook](RESEARCH.md) · [Evidence and provenance](PROVENANCE.md) · [Project inventory](showcase/PROJECT_INVENTORY.md) · [Visual provenance](VISUAL_PROVENANCE.md)

---

*The factory must grow.*
