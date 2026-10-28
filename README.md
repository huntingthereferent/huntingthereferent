![Humanity, pop culture, internet culture and shared connections across the world](assets/observational/humanity-online-banner.webp)

[![RESEARCH](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-477765?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#research) [![MATH](https://img.shields.io/badge/MATH-FINITE_MODELS-536C91?style=flat-square&labelColor=111827)](https://huntingthereferent.github.io/autobots-assemble/live/work.html#math) [![EVIDENCE](https://img.shields.io/badge/EVIDENCE-SOURCE_RECORDS-856840?style=flat-square&labelColor=111827)](PROVENANCE.md)

I investigate continuity through movement and changing relationships. My geometric research direction uses a moving torus: finite systems map aspects of that movement through explicitly defined states, transitions, and relationships. I build bounded mathematical and computational worlds, compare their actual results with expected results, and use the differences to determine what to correct next. The public repository is an evolving body of research and implementation, not a finished theory or a complete realization of continuity.

**Explore:** [Research](#research-focus) · [Method](#research-method) · [Finite A/B](#finite-ab-constructions) · [Test results](#selected-research-records)

## Research focus

- **Language and continuity** — following a referent through changes in wording, context, and interpretation. [Language Referent contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT_CONTRACT.md) · [Traversal runtime](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/referent_traversal.py)
- **Finite systems and moving toroidal geometry** — specifying finite periodic spaces, actual transition rules, changing relationships, and tests of whether correspondences survive changes in resolution. [Mathematical notes](showcase/MATHEMATICS.md) · [Shape contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md)
- **Native investigations** — comparing results against the original ARC, WORLD, and scientific-data sources, each under its own evidence rules. [Selected work](SELECTED_WORK.md) · [Research register](RESEARCH_REGISTER.md)

## Research method

Start with an explicitly defined finite system, its permitted movement, and the relationships being tested. Record what the transition predicts, execute it, and compare the observed result with the prediction. Keep the failed attempts as well as the successes, so the next correction starts from the real difference. A simulated outcome, a native test result, and an independently checked result are not interchangeable.

**Follow a worked example:** [From relation to execution to evidence](docs/TRACEWORK_THEORY_TO_EVIDENCE.md) connects defined mathematics to its actual code and source receipts, while keeping separate experiments separate.

I work independently, without institutional affiliation. The public implementations and their recorded evidence determine the scope of each claim.

<details>
<summary><strong>How the work stays connected — Tracework</strong></summary>

**Tracework** is the developing finite-system research and implementation environment in which I map movement and relationships while retaining what was changed, where it came from, what actually happened, and what remains unresolved. When a test moves forward, the source, the observed return, and the failures should remain traceable. Each investigation retains its own model and verification rules. The public implementation is **incomplete by design and under active development**: its bounded systems and evidence do not yet constitute a complete mathematical or executable model of moving toroidal continuity.

**[Open the interactive work and evidence viewer](https://huntingthereferent.github.io/autobots-assemble/live/work.html)**

<details>
<summary>Technical sources, implementation boundaries, and other research areas</summary>

| Area | Inspect |
| --- | --- |
| **Mathematical research** — finite models, constraints, proofs, and counterexamples | [Source mathematics](showcase/MATHEMATICS.md) · [Method](docs/RESEARCH_METHOD.md) |
| **Tracework implementation** — bounded handoffs, provenance, and source-linked movement | [Runtime and architecture](https://github.com/huntingthereferent/autobots-assemble/blob/main/TRACEWORK.md) · [Architecture](https://github.com/huntingthereferent/autobots-assemble/blob/main/ARCHITECTURE.md) · [Workspace sources](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/README.md) |
| **ARC / WORLD / NIH** — independent experiments under native evidence rules | [ARC evidence](ARC_EVIDENCE.md) · [WORLD sources](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/ab_world) · [NIH register](RESEARCH_REGISTER.md) |
| **Other projects** — applications, software, and source editions | [Project inventory](showcase/PROJECT_INVENTORY.md) |

Tracework was previously described as the *workstation*. Historical identifiers remain in the code where renaming would break provenance or compatibility. A shared evidence carrier does **not** make these research lanes one mathematical experiment.

</details>

</details>

## Selected research records

| Investigation | Native result and limit |
| --- | --- |
| **Finite A/B** | Distinct paths `BBAA` and `ABABB` reach `[2, 2, 1]` after 14 explored states **in one defined finite system**. [Pinned receipt](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/views/motion/convergence-receipt.json) · [Operators](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/work/arc_like_maze/math.py) |
| **ARC / original SP80 SDK** | **2 of 50** native resets reached official level **4/6** on October 21. A later **52 of 52** level-4 resets **did not reach** level 5 or WIN. [Native witness](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169) · [Failed follow-up](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534) |
| **NIH / AACT** | Two authenticated deposited exports share **432,597 study IDs**, with **1,345 differing status fields**. Underlying extract chronology is unresolved; these are *not* proven chronological status transitions. [Source comparison](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) |
| **WORLD / conditional motion** | Trial 31 checked **24 conservative inequalities** through a **0.25-unit** virtual-time horizon. Three hypothetical response cases lost a sufficient clearance bound; **no physical collision was observed**. [Source record](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/ab_world/TRIAL31_SOURCE_HANDOFF.md) · [Analytical check](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39531157339) |

[Complete evidence register, negative controls, and open questions](RESEARCH_REGISTER.md) · [Source-pinned code revision (October 26, 2026)](https://github.com/huntingthereferent/autobots-assemble/commit/c0ecc828a5fafd9d2c19e2a50d815c536d08c8be) · [Reviewed evidence snapshot (October 21, 2026)](https://github.com/huntingthereferent/autobots-assemble/commit/7916709e16e14cb1222639f385746abc882effe1)

## Finite A/B constructions

**Action order changes the state**

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg" width="680" alt="Finite A/B: different action orders yield different states in a defined model" /></a>

Different action orders produce different results in this [specified finite system](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py).

**Different A/B paths converge**

<a href="https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md"><img src="https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg" width="680" alt="Finite A/B: two separately verified action histories arrive at the same state" /></a>

Two independently checked action histories reach the same state **within that finite model**. [Source-generated visual and convergence receipt](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md). This is not evidence of universal convergence or of a physical system doing the same thing.

## Technical notes and audits

<details>
<summary>Expand the cognitive and communication vocabulary</summary>

The terms below describe parts of my experience, not separate deliberate steps or a proven neurological mechanism. I use *comparison* for something instinctual and already in motion, even while I am doing other things. My choice is whether to express what I notice, not whether that comparison happens.

**Mismatch-driven — noticing and correcting relationships**
- Mismatch detection; perceptual acuity; perceptual fluency
- Epistemic vigilance; recursive metacognition; reflexive self-modeling

Differences can become apparent without my searching for them. When words lose the relationship I mean, I correct them; revisiting those expressions helps explain the recursion in my communication.

**Embodied relational cognition — perception, movement, and learning**
- Embodied cognition; perception–action coupling; sensorimotor integration; proprioception
- Motor affordances; sensorimotor constraints; physical scaffolding
- Implicit cognition; automaticity; tacit knowledge
- Spontaneous and implicit motor learning; motor automaticity; sensorimotor adaptation
- Movement variability; task-integrated movement; dynamic balance
- Allostasis; cognitive–motor interference

This ongoing comparison continues alongside ordinary activity and spontaneous movement; it does not require deliberate verbal reasoning.

**Communication — spontaneous emotional expression**
- Discomfort and feeling can remain visible in communication, without deliberate disclosure

Every human has their own referent. I recognize myself among other people without treating them as interchangeable with me. Emotional responses arise and enter my ongoing, instinctual processing. I use words like *comparison*, *mismatch*, and *recursion* to describe aspects of that experience, but explaining it can make the process appear to be a deliberate sequence of analytical steps. That is not how I experience it. Language is how I unpack what I notice into something communicable, and I may correct those words to preserve the actual relationship.

**Truth-telling — parrhesia**
- Frank expression and correction; preserving what I mean as it moves

I call the choice to express what I notice and understand *artifacting*. I can choose not to speak; when I do, I try to preserve the actual referent and correct my words when necessary.


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

**The central distinction:** This is an inventory of language James can move through, not a claim that every pronoun is his preferred gender pronoun. The referent remains James while the perspective, relationship, or wording changes.


</details>

<details>
<summary><strong>Language Referent and continuity — AI-assisted repository self-audit (October 25, 2026)</strong></summary>

*An AI-assisted internal reading of public source files, not independent peer review or a fresh execution of the complete test suite.*

This source-level audit examines how James Muneoka's Language Referent research is represented in the Tracework repository. Its central concern is continuity: how a relationship can remain identifiable while language, context, observations, or computational representations change. The repository does not treat similar wording as sufficient evidence of the same relationship. Instead, it asks what survives a transition and what supports that conclusion.

The implementations go beyond storing earlier statements. Referent traversal records the current relation and direction, the relationships that survived or changed, available evidence, unresolved boundaries, and provenance. Those records allow subsequent movement to revisit earlier observations without automatically restoring an outdated interpretation. When a proposed continuation fails, the system can retain the useful observations, expose the unresolved boundary, and attempt to reground the original inquiry.

This also clarifies the role of *meta* in the work. Rather than defining it as a separate supervisory layer, the implementation permits the result of one movement to become input to another pass under the same evidence contract. Earlier movements can therefore become objects of inspection, correction, and continuation. Retention is modeled as preserved relational structure, not merely as a collection of remembered sentences.

James's broader research direction uses movement in language as an observable starting point for investigating how humans retain and follow thought. The repository supplies computational representations of parts of that inquiry; it does not establish a neural mechanism or an empirically validated model of the human brain.

The same continuity requirements extend into finite mathematics, handoffs between independent systems, and the geometry of a growing computational world. Each domain retains its own evidence and rules; provenance connects their movements without asserting that the domains are identical.

**Finite toroidal mapping and world expansion.** The current finite two-coordinate periodic example is the set

\[
W_N=(\mathbb{Z}/N\mathbb{Z})\times(\mathbb{Z}/N\mathbb{Z}),\qquad N\in\mathbb{Z}_{>0}.
\]

A finite system's movement requires a specified transition function \(F_N:W_N\times U_N\to W_N\), with \(U_N\) its admitted inputs or actions. The periodic coordinate space alone does not define movement or determine relationships. A relationship can be represented explicitly at each step, for example by \(R_n\subseteq W_N\times W_N\); the rule relating \(R_n\) to \(R_{n+1}\) must be specified and tested rather than inferred from a drawing.

For an integer scale factor \(k\geq 2\), the map

\[
E_{N,k}([x]_N,[y]_N)=([kx]_{kN},[ky]_{kN})
\]

embeds the finite coordinate set \(W_N\) into \(W_{kN}\). It does not, on its own, prove that movement is preserved. Given an explicit action correspondence \(\iota_{N,k}:U_N\to U_{kN}\), the transition-compatibility condition is

\[
E_{N,k}(F_N(w,u))=F_{kN}(E_{N,k}(w),\iota_{N,k}(u)).
\]

This equality is a condition to verify for the chosen systems, not an established universal result. The smooth torus \(\mathbb{T}^2=S^1\times S^1\), the finite periodic set \(W_N\), and the separately implemented finite cubical three-torus are distinct mathematical constructions. A rendered torus is not itself evidence that an implementation preserves the intended movement.

James describes continuity geometrically as a **moving torus**. Finite systems are used to map aspects of its movement and changing relationships; their bounded representations must not be mistaken for the entirety of continuity. The existing projection is one research construction, not the completed Tracework environment. [Finite mapping definitions and test obligations](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md).

**Audit assessment (October 25 source review, with the geometric framing clarified October 28):** The repository contains explicit contracts and code for traversal, regrounding, provenance, recursive re-entry, and evidence-bounded handoffs. The growing-world projection remains a limited implementation rather than an integrated canonical Tracework world. Quantitative retention measurements and neuroscience validation are not established by the inspected source. This was a read-only source audit, not an executed full test suite.

**Inspect the underlying structures:** [Language Referent contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT_CONTRACT.md) · [Shape contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md) · [Referent traversal](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/referent_traversal.py) · [Natural provenance](https://github.com/huntingthereferent/autobots-assemble/blob/main/protocols/core/provenance.md) · [Regrounding](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/REGROUNDING.md) · [Continuous handoff](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/handoff/CONTINUOUS_HANDOFF.md) · [Growing finite-world projection](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/toroidal_projection.py) · [Animated toroidal tracing](https://huntingthereferent.github.io/autobots-assemble/growing-toroidal-world.html)

</details>

<details>
<summary><strong>Why build continuity infrastructure early?</strong></summary>

I see this work in the context of a world already saturated with information, automation, and increasingly interconnected systems. Concern about where humanity is heading is not unusual. The question for me is not whether I can predict a civilizational collapse; it is what happens when systems keep growing faster than their ability to preserve sources, relationships, and reliable paths for correction.

Breakdowns do not have to arrive all at once. They can appear as smaller, traceable failures while a system still seems to function. My working direction is to build the continuity and evidence infrastructure *one step early*: preserve the original referent, record what actually changes, keep failures visible, and make regrounding possible before errors compound.

</details>

<details>
<summary><strong>Development history and project provenance</strong></summary>

The public development record covers September–October 2026 and builds on mathematical work begun earlier. The reported direct expenditure for the setup presented here is **$20**; this is not an estimate of the project's total development cost or the value of the time invested. Working hours have not been formally tracked.

Source history preserves the project's development and distinguishes research notes from original observations, tests, and unresolved questions.

</details>

**Documentation:** [Research method](docs/RESEARCH_METHOD.md) · [Research notebook](RESEARCH.md) · [Evidence and provenance](PROVENANCE.md) · [Project inventory](showcase/PROJECT_INVENTORY.md) · [Visual provenance](VISUAL_PROVENANCE.md)

---

*The factory must grow.*
