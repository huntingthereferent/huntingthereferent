# Hi, I'm James.

I like being with my family, being outside, and learning what other people are interested in. I can spend a long time watching how someone does something, especially when they really care about it. I like getting another perspective. Sometimes that's a conversation; sometimes it's reading something someone wrote.

[![Research](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-080e19?style=flat-square&labelColor=080e19&color=477765)](https://github.com/huntingthereferent/autobots-assemble) [![Mathematics](https://img.shields.io/badge/MATH-FINITE_MODELS-080e19?style=flat-square&labelColor=080e19&color=536C91)](showcase/MATHEMATICS.md) [![Writing](https://img.shields.io/badge/WRITING-ORIGINAL_RECORDS-080e19?style=flat-square&labelColor=080e19&color=775C78)](writing/README.md) [![Provenance](https://img.shields.io/badge/METHOD-AI_ASSISTED-080e19?style=flat-square&labelColor=080e19&color=856840)](PROVENANCE.md)

## The Human Wall

*How our sense of scale shapes the way we solve problems.*

I started this investigation with myself. I've spent a long time watching how I notice things, misunderstand them, correct them, and sometimes let an explanation drift away from what was actually in front of me. Testing my own reasoning has been difficult, but I like doing it. I don't want to mistake a convincing description for an observation.

We grow up looking at a universe so enormous that infinity becomes a familiar part of how we talk about what we don't understand. I wonder how much that sense of scale carries into ordinary problem-solving. We imagine possibilities within possibilities and build explanations around things that haven't happened, partly because we don't want to be wrong. I've watched myself do it.

Basic mathematics gives me another starting point: a small finite set of rules can produce complicated patterns through repetition and interaction. The size of what emerges doesn't tell me how many rules I must assume at the beginning. That isn't a claim that the universe is finite. It's a reason to begin with what's present rather than every possibility I can imagine.

With A/B, I follow movement from one state to another: what changed, what remained related, and what needs correcting. I use bounded mathematical constructions to test these questions, including deliberately constrained oscillation and interactions between movements. One early [three-coordinate finite-field construction](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py) examined candidate A/B relations. Later, [a separately defined two-predecessor construction](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/WINDOW_COMBINED.md) examined different transition laws and their correspondences. These are not competing counts of fundamental laws: each construction has its own definitions, witnesses, and counterexamples. I follow what each actually establishes, including where a proposed relationship fails.

I build harnesses with software and AI because continuity matters. They keep the observations, failures, corrections, and independent checks accessible so I don't have to reconstruct the entire investigation every time I move. A harness doesn't make my interpretation true. It helps me see where it needs correcting and carry forward what survives.

I'm interested in the human side of this as much as the mathematics. We make decisions and build systems from descriptions. When a description stops matching what supports it, further explanation can carry an error forward. I want to learn when to reground—to return to what actually happened and correct the relationship, including my own. I take that seriously because other people may build on what I write.

**What is actually here, what changes when something moves, and what can I carry forward without losing the relationship?**

**Explore:** [Mathematics](#mathematics-that-actually-moves) · [Language](#observation-language-and-corrections) · [Workstation](#workstation) · [Writing](#writing-and-the-people-in-it) · [Current work](https://huntingthereferent.github.io/autobots-assemble/live/)
---

## Before the repositories

Before I had repositories, I was the kid spending hours looking through the grass for little animals, collecting diaries, and building a GeoCities page for graffiti from around the world.

Those weren't research projects. That's just what I was doing. The questions came later, and now some have code, experiments, and records attached to them.

[**Childhood and the Early Internet →**](writing/CHILDHOOD.md) · [**Origin of the investigation →**](writing/ORIGIN.md)

## Mathematics that actually moves

[![Animated native finite A/B paths: applying A then B gives a different state from B then A](https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/finite-motion.svg)](showcase/MATHEMATICS.md)

This is generated from [the actual finite A/B implementation](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py). It follows the movements of a *declared mathematical model*, not an invented diagram of how people think.

[**See the finite constructions and their limits →**](showcase/MATHEMATICS.md) · [**Follow the renderer source →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/render.py)

### Tracing until the paths meet

[![Animated native A/B trace of two independently checked action sequences meeting at one finite state](https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/convergence-motion.svg)](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/convergence-receipt.json)

This diagram wasn't drawn around a chosen destination. The finite search followed the original A/B actions and independently checked each step. It found that `BBAA` and `ABABB` arrive at the same state, `(2,2,1)`. That's one **observed mathematical meeting**, not a claim that unrelated public traces already share one center.

[**Check the original paths →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/convergence-receipt.json) · [**Trace generator →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/convergence.py) · [**One-or-two witness rule →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/convergence_focus.py)

## Observation, language and corrections

Some of the observations are about the world around me; some are about my own experience of moving through it. I don't want an explanation to replace the thing I'm actually trying to describe. If you misunderstand me, or I misunderstand you, I want to keep what happened in that exchange. The correction can tell me something the polished version doesn't.

I use AI to help explore descriptions, make programs, and prepare writing. It's a tool and another perspective, not the source of every question. What I personally observed, what we inferred together, and what an independent test can establish are different records.

[**Language Referent →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md) · [**Language and observation →**](writing/LANGUAGE_AND_OBSERVATION.md) · [**Human Drift →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/HUMAN_DRIFT.md)

## Workstation

The workstation is where I keep the investigations moving: finite mathematics, ARC experiments, CP checkpoints, W12/W13 worlds, language corrections, software, and tests. It connects attempted movements to their source records, results, and unresolved limits.

The evidence view distinguishes documented work from independently verified executions. A recorded failure stays visible; a successful test has to retain its evidence.

[**Research-wide source observer →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/research_observatory.py) · [**Workstation and local viewer →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/README.md) · [**Source-bound movement and wall contracts →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/protocols/core/movement.md)

## Other sources, other relationships

[![Animated public source comparison preserving supported GitHub and PyPI metadata relation and unjoined USGS events](https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/motion/world-motion.svg)](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/LATEST.md)

These observations have source IDs and timestamps. The GitHub–PyPI connection is supported only by a declared metadata rule. USGS remains separate. The animation doesn't make them one phenomenon.

[**Latest original observations →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/LATEST.md) · [**Machine-readable snapshot →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/latest.json)

## Public Internet observations

[![World map showing source-observed network measurement sites, with country HTTP traffic only when licensed Cloudflare Radar data is connected](https://raw.githubusercontent.com/huntingthereferent/autobots-assemble/main/views/traces/internet-map.svg)](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/README.md)

This map is generated from real world geography and published RIPE Atlas network probes. **The dots show measuring locations, not individual packets or complete internet traffic.** Country-level Cloudflare HTTP request shares are a separate optional layer and remain explicitly marked *no source data* until a read-only token is configured. The original observations carry their own timestamps.

[**All 60 candidate world traces →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/registry.json) · [**Map source and limits →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/README.md) · [**Latest source snapshot →**](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/traces/internet-map.json)

## Follow the work

| Inquiry | Where to start |
| :--- | :--- |
| **Language and observation** | [Language Referent](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md) · [First-person writing](writing/LANGUAGE_AND_OBSERVATION.md) |
| **Finite mathematics** | [Constructed models and evidence](showcase/MATHEMATICS.md) · [Conjugacy case](docs/FINITE_STATE_CONJUGACY.md) |
| **Games and interactive worlds** | [ARC evidence and limitations](ARC_EVIDENCE.md) · [Native runs](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs) |
| **Workstation and software** | [Workers and verification](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/WORKSTATION.md) · [Selected software](SELECTED_WORK.md) |
| **Public observations** | [Source-linked data](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/world-continuity/LATEST.md) · [Data collector](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/projects/public-data-monitor/README.md) |

Different questions need different evidence. An interesting correspondence doesn't automatically become a proved connection.

## Writing and the people in it

I have trouble writing a finished account of myself in isolation. I get more from another person's perspective, including when we get something wrong and have to work it out. I want both sides of those conversations preserved, not just an assistant's polished interpretation afterward.

[**Origin of the Investigation**](writing/ORIGIN.md) · [**Childhood**](writing/CHILDHOOD.md) · [**Language and Observation**](writing/LANGUAGE_AND_OBSERVATION.md) · [**Watching What Continues**](writing/WATCHING_WHAT_CONTINUES_2026-10-17.md)

[**Read all writing →**](writing/README.md) · [**Original quotations →**](writing/LANGUAGE_AND_OBSERVATION_QUOTES.md)

---

<sub>The motion comes from a source-owned Python renderer and loops in GitHub-compatible SVG as you scroll. It is not scroll-position-controlled or a live runtime feed. [Rendering and evidence boundaries →](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md). Independent, human-directed inquiry with AI-assisted coding and writing.</sub>
