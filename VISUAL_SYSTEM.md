# Visual illustrations — supplementary sources

[← Research profile](README.md) · [Visual provenance of the words](VISUAL_PROVENANCE.md) · [Research](RESEARCH.md)

The profile begins with the humanity-and-internet-culture banner, the research introduction and source index. Its later visuals include two separately displayed, source-generated animated finite A/B witnesses. The older people-and-work illustration and the static A/B atlas/legend are archived here rather than displayed on the profile. No diagram substitutes for original research evidence.

[![People, early internet, games, conversation, language, and code connected on a neon observation field](assets/observational/people-and-work.svg)](assets/observational/people-and-work.svg)

**[View the earlier connected visual](assets/observational/people-and-work.svg)** · [Finite A/B movement on the profile](README.md#one-finite-example) · [A/B convergence on the profile](README.md#where-separate-ab-paths-meet) · [Source and evidence index](PROVENANCE.md)

## What the image is for

This is a small navigational picture, not a model of James or a map of who matters more than whom. People, games, reading, conversation and work were present in James's life before these repositories existed. Some of the experiences became questions, and some questions became code or mathematics. The visual doesn't say that one thing caused everything else.

James is part of the experiences he describes. He has a life outside the research. When his own experience is the thing being observed, that does not turn him into a character, a general law, or an explanation of everyone else.

## Places to enter

| Subject | Original records |
| --- | --- |
| **Language Referent** | [Research source](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md) · [Human Drift](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/HUMAN_DRIFT.md) |
| **Finite mathematics** | [Constructed examples](showcase/MATHEMATICS.md) · [Conjugacy case](docs/FINITE_STATE_CONJUGACY.md) |
| **Games and replay** | [ARC evidence](ARC_EVIDENCE.md) · [Native runs](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs) |
| **Workstation and software** | [Handoffs and verification](https://github.com/huntingthereferent/autobots-assemble/tree/main/systems/workspace) · [Project inventory](showcase/PROJECT_INVENTORY.md) |
| **World observations** | [External data with timestamps](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/LATEST.md) |

## What color does — and doesn't — mean

Cyan, magenta, violet and lime distinguish paths and subjects. A drawn connection indicates something James has considered or wants to examine; it does not establish causality, equivalence, or a shared mechanism. In particular, a relationship between human experiences is not automatically a formally defined A/B operation.

The [A/B overview](assets/observational/continuity.svg), [movement and correspondence legend](assets/observational/continuity-legend.svg), [earlier continuity atlas](assets/observational/continuity-loom.svg), and [observation/correction sequence](assets/observational/movement.svg) remain available as archived illustrations, but they are **not** displayed on the profile. The profile instead shows [finite A/B action order](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/finite-motion.svg) and [finite A/B convergence](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/convergence-motion.svg). The stated mathematical meaning belongs only to the defined models.

## A mathematical case within the work

For a *particular finite world* `i`, let its states be `S_i`, with defined operations

```text
A_i : S_i -> S_i
B_i : S_i -> S_i
```

For another world `j`, a map `H : S_i -> S_j` preserves these movements if, on the states under consideration,

```text
H(A_i(s)) = A_j(H(s))
H(B_i(s)) = B_j(H(s))
```

When both equations hold on the appropriate states, induction on the length of a word in `A` and `B` shows that the map preserves **every finite composition** of those operations. This is a precise, testable kind of continuity.

A different question asks whether order matters inside one world:

```text
A(B(s))  ?=  B(A(s))
```

For example, with `A(x)=x+1` and `B(x)=2x`, starting at `1` yields `A(B(1))=3` while `B(A(1))=4`. The two paths genuinely split. In the [finite experiments](showcase/MATHEMATICS.md), actual claims belong to their declared state spaces, implementations, tests and counterexamples.

**These equations describe specific defined models, not people or the whole visual.** Claims about actual systems belong to their own sources, tests and counterexamples.

## Historical visual draft and Internet observations

The [earlier A/B Continuity Atlas](assets/observational/continuity-loom.svg) remains a previous design attempt, not a literal representation of James or a verified relationship between those worlds. The [Internet map](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/internet-map.svg) is different: it records a bounded sample of public measurement probes and geography. Its [sources and limitations](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/README.md) must travel with the display; probe dots are not observed connections or traffic. The former world-data image is no longer shown on the profile.

[Return to profile](README.md) · [Visual provenance](VISUAL_PROVENANCE.md) · [Evidence](PROVENANCE.md)
