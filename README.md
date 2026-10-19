# Hi, I'm James.

I like being with my family, being outside, playing games, and learning what other people are interested in. I can spend a long time watching how someone does something, especially when they really care about it. I like getting another perspective. Sometimes that's a conversation; sometimes it's reading something someone wrote or playing alongside them.

## The Human Wall

*How our sense of scale shapes the way we solve problems.*

I've spent a lot of time trying to understand how I solve problems, including what happens when I misunderstand something, how I correct myself, and how easily an explanation can move away from the thing I was originally looking at.

I didn't start by constructing a theory about other people. I started by observing myself. I wanted to know what I was actually doing while I was thinking, not just how I described it afterward. That meant paying attention to mistakes, revisiting my own assumptions, and sometimes finding that the problem I was trying to solve wasn't the problem in front of me anymore.

One thing I keep returning to is how much our sense of scale influences the way we approach problems.

We grow up learning about an unimaginably large universe. We're introduced to infinity, enormous distances, complexity, and things we may never fully understand. It's natural to look at something that large and expect the explanation to be equally enormous. I think we carry some of that expectation into ordinary problem-solving.

We consider possibilities, then possibilities within those possibilities. We anticipate mistakes, construct explanations, correct those explanations, and sometimes build entire systems around things that haven't happened. Much of this comes from trying to understand something properly and not wanting to be wrong. I recognize that behavior because I've observed it in myself.

But mathematics offers an interesting distinction: **the complexity of what a system produces doesn't necessarily tell us how complicated its starting conditions must be.**

A small finite set of relationships can produce complicated patterns through repetition and interaction. A process can continue without needing an entirely new foundational rule for every new result. This doesn't tell us whether the physical universe is finite or infinite. It does give us another way to approach a problem.

Instead of beginning with every possibility, I can begin with what's present.

I can observe a state, make a movement, compare the result, and follow the relationships that continue. If something changes unexpectedly, I can investigate that difference. If a description fails, I can correct what failed without discarding everything else or inventing additional explanations in advance.

This is where A/B comes into my work.

I'm interested in what changes between states, what remains related, and whether those relationships can be preserved through further movement. A/B gives me a way to construct, compare, and investigate those movements rather than relying entirely on my interpretation of them.

The mathematics makes parts of that investigation executable. For example, I've been experimenting with deliberately constrained movement and oscillation inside small finite systems, allowing movements to interact and observing the structures that result. We started by trying nine anchors and are currently working with forty-eight. I don't know whether forty-eight is the smallest useful set. That's something to investigate through the construction, not a number I need to defend in advance.

What interests me is how much complexity can arise from simple relationships, and how far those relationships can be followed before they require correction.

## Why I use harnesses

A large part of this work has involved learning to preserve continuity.

When I'm investigating something, I don't want to stop every few steps and reconstruct the entire history of how I arrived there. I want the observations, attempted movements, failures, corrections, and successful tests to remain accessible while the investigation continues.

That's why I've become so interested in building harnesses.

I use software and AI to help retain that continuity, construct experiments, compare results, and independently check parts of the work. They help me keep moving without substituting an explanation for an observation.

The same principle matters when I'm looking at my own reasoning. I want to be able to recognize when something I've said no longer matches what I've observed, correct it, and continue without pretending the earlier movement never happened.

I take that responsibility seriously because the things we describe can influence what other people go on to build, believe, or investigate.

## Where this leads

The broader question for me is about human problem-solving.

We have an extraordinary ability to construct descriptions, abstractions, and increasingly complex systems. But those descriptions still have to meet the relationships of whatever we're working with.

If we keep extending explanations without returning to what supports them, errors can accumulate. Eventually, those errors can affect the systems built upon them. I think regrounding—returning to the actual relationships and correcting what no longer fits—is an important part of keeping those systems working.

I don't think that requires everyone to use the same language, mathematical construction, or method. Different approaches can arrive at the same observable constraints.

I'm interested in whether we can become better at recognizing those constraints without first trying to account for every imaginable possibility.

That's what connects my interest in language, mathematics, software, human behavior, and the way people understand one another. The subjects look different, but I keep encountering the same practical question:

**What is actually here, what changes when something moves, and what can I carry forward without losing the relationship?**

The research grew out of questions I've had for a long time. Some of those questions now have source code, mathematical constructions, experiments, and records attached to them. Others are still questions.

I'm continuing to work through them.

[![Research](https://img.shields.io/badge/RESEARCH-SOURCES_%26_TESTS-080e19?style=flat-square&labelColor=080e19&color=477765)](https://github.com/huntingthereferent/autobots-assemble)
[![Mathematics](https://img.shields.io/badge/MATH-FINITE_MODELS-080e19?style=flat-square&labelColor=080e19&color=536C91)](showcase/MATHEMATICS.md)
[![Writing](https://img.shields.io/badge/WRITING-ORIGINAL_RECORDS-080e19?style=flat-square&labelColor=080e19&color=775C78)](writing/README.md)
[![Provenance](https://img.shields.io/badge/METHOD-AI_ASSISTED-080e19?style=flat-square&labelColor=080e19&color=856840)](PROVENANCE.md)

**Explore:** [Mathematics](#mathematics-that-actually-moves) · [Language](#observation-language-and-corrections) · [Workstation](#workstation) · [Public observations](#public-internet-observations) · [Writing](#writing-and-the-people-in-it)

[Current work](https://huntingthereferent.github.io/autobots-assemble/live/) · [Research source](https://github.com/huntingthereferent/autobots-assemble) · [Writing archive](writing/README.md) · [Projects](showcase/PROJECT_INVENTORY.md)

---

## Before the repositories

Before I had repositories, I was the kid spending hours looking through the grass for little animals, collecting diaries, and building a GeoCities page for graffiti from around the world. Later I spent years around Quake III and World of Warcraft, watching other players, learning the games, and meeting people I wanted to keep playing with.

Those weren't research projects. That's just what I was doing.

I still like ordinary life. I haven't stopped being the person who enjoys his family or who wants to see what another person is doing. The subjects have expanded, and now some of the questions have source code, proofs, experiments, and records attached to them.

[**Childhood and the Early Internet →**](writing/CHILDHOOD.md) · [**World of Warcraft and Reckful →**](writing/CHILDHOOD_PART_TWO.md) · [**Origin of the investigation →**](writing/ORIGIN.md)

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

A job and a research question begin the same way: with something to investigate. Follow what was attempted, what changed, what could be verified, which walls remain, and what continues. The work includes finite mathematics, ARC experiments, CP checkpoint records, W12/W13 worlds, language corrections, software, and tests—not a collection of income-opportunity scorecards.

The workstation presents source-owned mathematical moves, recorded research boundaries, original document references and native execution attempts in **one evidence view**. Its technical execution controls remain available under Advanced. A documented wall remains documented; an independently witnessed execution retains its stronger evidence status. Neither is invented or erased to fit the display.

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

[**Origin of the Investigation**](writing/ORIGIN.md) · [**Childhood**](writing/CHILDHOOD.md) · [**World of Warcraft and Reckful**](writing/CHILDHOOD_PART_TWO.md) · [**Language and Observation**](writing/LANGUAGE_AND_OBSERVATION.md) · [**Watching What Continues**](writing/WATCHING_WHAT_CONTINUES_2026-10-17.md)

[**Read all writing →**](writing/README.md) · [**Original quotations →**](writing/LANGUAGE_AND_OBSERVATION_QUOTES.md)

---

<sub>The motion comes from a source-owned Python renderer and loops in GitHub-compatible SVG as you scroll. It is not scroll-position-controlled or a live runtime feed. [Rendering and evidence boundaries →](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md). Independent, human-directed inquiry with AI-assisted coding and writing.</sub>
