# Research

I usually begin with something I can observe but cannot yet describe accurately. I follow it through examples, conversation, mathematics, software, and tests until I can see which relationships hold and which ones I misunderstood.

The wording can change along the way. So can the tools and the problem I thought I was working on. That does not mean every new description is a different investigation, or that everything I encounter belongs to one theory.

## Following the relationship

A single observation can be useful without being a complete explanation. What matters next is what happens when something changes: which relationships survive, which depend on the original conditions, and which were only assumptions.

Sometimes I find the right words after working through several examples. Sometimes a program or mathematical model makes a distinction clear that I could not express in conversation. Sometimes a failed test shows that I was following the wrong relationship.

I keep those corrections. Losing an explanation is not the same as losing everything learned while testing it.

This is also why I do not want a convenient representation to take the place of the thing being studied. A frame, a summary, a state label, a hash, or a diagram can expose something useful. Each leaves something out.

## From observation to something testable

Different subjects demand different evidence.

- In an interactive environment, I can record what was visible, what action was permitted, and what the environment actually returned.
- In software, I can compare source, execution, resulting state, failures, and what the tests really exercised.
- In mathematics, I have to name the domain and operations before a proof or counterexample means anything.
- In language and communication, I can preserve what was said, what was understood, what was corrected, and what remains uncertain. That is not automatically a formal proof.

I can carry a useful way of looking between these subjects without declaring their structures identical. A relationship that works in one setting has to earn its place in another.

## Work that grew from this

| Area | What I am examining | Where to inspect it |
| --- | --- | --- |
| **Language and observation** | How a continuing referent can be described, misunderstood, corrected, and followed across different expressions | [Language referent](https://github.com/huntingthereferent/autobots-assemble/blob/main/LANGUAGE_REFERENT.md) · [Human Drift](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/HUMAN_DRIFT.md) |
| **Finite mathematics** | Defined transformations, correspondence, cycle structure, and what limited observations can or cannot distinguish | [Mathematical constructions](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/arc_like_maze) · [Conjugacy case](docs/FINITE_STATE_CONJUGACY.md) |
| **Interactive environments** | Recovering usable rules through native observations, actions, discrepancies, and replay | [ARC evidence](ARC_EVIDENCE.md) · [Saved routes and replay](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs) |
| **Processes and handoffs** | Carrying source identity, state, and verification across workers or unlike systems without silently inventing a completed action | [Process Workstation](https://github.com/huntingthereferent/autobots-assemble/tree/main/systems/workspace) · [Selected cases](SELECTED_WORK.md) |
| **Software construction** | Whether a working chain of components preserves its inputs, errors, and outputs all the way through | [Project inventory](showcase/PROJECT_INVENTORY.md) |

These are different investigations with different limits. The links lead to implementations, dated observations, case records, and, where available, tests. They do not all establish the same kind of result.

## Evidence and unfinished work

I distinguish an idea from a model, a model from a working implementation, a local test from independent verification, and a reported result from one that another person can reproduce.

An unsuccessful run can narrow what is possible. An incomplete test leaves something unknown. A checkpoint can preserve where the work stopped without claiming that the larger question is settled.

For any concrete result, the important record is what was used, what actually happened, how the outcome was checked, and where the evidence stops. The goal is to make it possible to return to the work without replacing it with a polished story.

The research is ongoing. A particular test or construction may reach a finished boundary while the relationship that led to it remains open to further observation.

[Selected investigations](SELECTED_WORK.md) · [Evidence and provenance](PROVENANCE.md) · [Operational research notes](docs/RESEARCH_METHOD.md) · [Back to profile](README.md)
