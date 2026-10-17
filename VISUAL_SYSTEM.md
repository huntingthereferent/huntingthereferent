# A/B Continuity Atlas

[← Profile](README.md) · [Visual provenance](VISUAL_PROVENANCE.md) · [Research](RESEARCH.md)

[![The Continuity Atlas](assets/observational/continuity-loom.svg)](assets/observational/continuity-loom.svg)

**[Open the full-size artwork](assets/observational/continuity-loom.svg)** · [Source and evidence index](PROVENANCE.md)

The repository used to display separate visual summaries. This atlas gives those parts a shared *place* without pretending they have identical evidence or identical mathematical structure.

**James is not where the movement branches from.** The weave runs into the image from before James, crosses his present position, and continues past it. The marker says **JAMES · HERE**: his position as a living observer, builder, participant and corrector. The six research regions are different areas of his work, not six people and not branches growing out of him.

**People are throughout the image.** The human traces already extend across the same field, and the cluster labeled **HUMANS** is made of many individual points. James's stated direction is for humans, not toward a hypothetical single human or a universe occupied by James alone. The picture doesn't claim one person caused the others or that they share a proved physical mechanism.

The movement is drawn as an ongoing braided field, **not a genealogy or causal tree**. The colored regions are entrances, not containers:

| Region | Follow it |
| --- | --- |
| **Writing** | [Conversations and corrections](writing/README.md), [origin](writing/ORIGIN.md) |
| **Games** | [Interactive evidence](ARC_EVIDENCE.md), [native runs](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs) |
| **Mathematics** | [Finite-state investigations](showcase/MATHEMATICS.md), [conjugacy case](docs/FINITE_STATE_CONJUGACY.md) |
| **Workstation** | [Worker system](https://github.com/huntingthereferent/autobots-assemble/tree/main/systems/workspace), [handoff contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/handoff/CONTINUOUS_HANDOFF.md) |
| **World observation** | [Read-only public data view](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/LATEST.md) |
| **Provenance** | [Sources, tests, and limits](PROVENANCE.md), [visual evidence guide](VISUAL_PROVENANCE.md) |

The outer world-data marks depict *source lanes*, not any claimed common cause. Seismology is one possible observed subject, not the center or identity of the repo. The existing public-data monitor is linked above; the artwork does **not** claim that a new Prometheus or Grafana deployment has been built.

## The movement key

[![A/B atlas movement legend](assets/observational/continuity-legend.svg)](assets/observational/continuity-legend.svg)

- **Cyan and magenta** distinguish A and B movement *inside a model in which those operations are actually defined*. In other contexts they are recurring visual language for examining movement; they are not automatically mathematical functions on people, prose, or public data.
- **Dotted gold** means a correspondence worth tracing. It is **not** an assertion that the domains are equivalent.
- **Diverging endpoints** mean two paths produced different results **when the specific model and starting state have been stated**. A near-miss drawn artistically is not itself a proof.
- **Fine orbital and connecting threads** make the atlas navigable; their presence is not an evidence or causality claim.
- **Incoming source paths** keep their own origins and timestamps. Data from GitHub or a public observation feed should remain separately attributable.

## Mathematics behind one part of the image

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

**The atlas illustrates these questions. It does not prove that any two arbitrary regions satisfy the equations.** Research findings are linked to their own sources.

## Why it is here

The same inquiry can pass through a conversation, a game, a proof attempt, a workstation run, or a source-linked public measurement. Sometimes the connection holds. Sometimes the language makes it look like it holds, until another perspective or a test shows what was missing.

The artwork leaves the different layers of James's work visually connected while surrounding them with other human presences. James isn't the origin of the movement, and humans aren't a future question mark. The repository keeps the evidence **epistemically separate** so the visual doesn't rewrite what actually happened.

[Return to James's profile](README.md) · [Explore the recorded paths](VISUAL_PROVENANCE.md)
