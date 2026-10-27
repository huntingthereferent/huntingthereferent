# ARC Research — source and evidence index

*Scope: original ARC-AGI-3 game observations and distinct ARC-like finite mathematical constructions. Historical source transfer October 10; source-pinned native SP80 frontier reviewed October 21, 2026.*

This index links to **actual public code and test entry points**, then states which reported game outcomes do and do not have corresponding public execution data. Source code, a passing test, a recorded score, and a reproducible winning trajectory are different types of evidence.

## October 21 native SP80 — level 4 of 6 (2/50), not WIN

**Latest source-pinned reviewed frontier (October 21):** the original SDK returned official `levels_completed=4`, `NOT_FINISHED` for **2 of 50 independent native resets** in the source-frozen level-3→4 entry experiment. The [native GitHub Actions run](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39616395169) generated an original SDK result JSON and native frame-stack NPZ; the [pinned source program](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/arc3/native_sp80_stage3_right_catcher_edge.py) defines that bounded test. This is **two observed official level-4 returns**, not a complete six-level win or a universal solver.

A separate [52-reset native level-4 follow-up](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534) returned **52/52 at level 4**, with **0 official level-5 or WIN advances** under those tested actions. The [pinned follow-up program](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/work/arc3/native_sp80_stage4_clean_lateral_top.py) inspects source frames; apparent cup or border movement is not itself an official level transition.

**Evidence retention warning (checked October 27, 2026):** the downloadable original JSON/NPZ artifacts associated with both cited native runs report **November 4, 2026 expiration**. GitHub Actions run pages and logs are not durable substitutes for those artifact bytes. Preserve exact original artifact packages with verified hashes in a source-owned archive before expiry; their availability at the run URL is time-limited.

## October 20 historical SP80 — level 3 of 6

**On October 20, the public original ARC-AGI-3 SP80 game had an independently reproduced `levels_completed=3` result.** This supersedes the earlier statement that the source-native investigation had only entered level 2. The earlier source-negative level-2 tests remain genuine negative tests for their particular control words; they should not be erased.

- [Original SDK finite-screen candidate experiment](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39462922216): 32 authentic independent original-game resets, with **two actual level-3 advances**, one from each independently verified earlier stage-1 witness. The successful stage-2 native word was `6@12,21 4 6@44,29 3 3 6@12,33 3 3 6@40,41 4 5`; the screen-flow proxy was **only a proposal**, not a recovered engine rule.
- [Independent stage-3 native entry and screen map](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39463571663): two fresh original game resets reproduced `levels_completed=3`, `NOT_FINISHED`, with identical entered stage-3 source screens. [Read the executable source](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc3/native_sp80_stage3_entry_source_map.py).
- [Native level-3 feedback controls](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39471887855): 32 authentic stage-3 trials, **32 ended level 3, zero level-4 or WIN** under the tested actions. [Inspectable program and its exact result criteria](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc3/native_sp80_stage3_native_feedback.py).

These October 20 experiments establish **bounded original-SDK 3/6 progression**, but **did not themselves produce level 4**. That particular negative result is not a claim about later source-frozen experiments. The October 21 source run above independently establishes two official level-4 entries, but **not a six-level WIN, a universal game-solving algorithm, or a proven correspondence between the constructed F3 mathematics and the native game**. Actual source game level outcomes, original frame returns and negative controls take priority over captions or inferred puzzle physics.

[Current source-pinned research register](RESEARCH_REGISTER.md) · [Native ARC lane](https://github.com/huntingthereferent/autobots-assemble/tree/main/work/arc3) · [Original W12/legacy native route records](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs)

## 01 / Native ARC-AGI-3 — actual software

| Artifact | Source | What a reader can inspect |
| :--- | :--- | :--- |
| Official game interface and environments | [ARC Prize / ARC-AGI Toolkit](https://github.com/arcprize/ARC-AGI) | External native SDK and game interface; **not** James's solver or scorecard. |
| Native frame observer | [`runtime/arc_native_observer.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/arc_native_observer.py) | Captures before/after 64×64 native SDK frames, action metadata, selected-state differences, and SHA-256 frame locators. Read-only: it does **not** choose or execute game actions. |
| Execution/evidence comparison | [`runtime/observed_evaluator.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/observed_evaluator.py) | Reconciles observed native transitions with the existing action/handoff lineage. Not a game-solving policy. |
| Integration tests | [`network/tests/test_arc_native_observer.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_native_observer.py) | Synthetic frame tests and a separately **opt-in** test that invokes an actual FT09 SDK step and passes its observation through the evaluator. One native step is not a completed game. |

**Public test command** (from the `language-network` repository root):

```bash
python -m unittest network.tests.test_arc_native_observer -v
```

The real-SDK FT09 case is skipped unless `CONTINUITY_ARC_NATIVE_TESTS=1` is set and the native ARC dependencies and environment are available. With those prerequisites, its individual test entry is:

```bash
CONTINUITY_ARC_NATIVE_TESTS=1 python -m unittest network.tests.test_arc_native_observer.ARCNativeProviderIntegrationTests.test_actual_ft09_sdk_step_to_service_lineage -v
```

These commands identify inspectable test entry points; the current profile repository does **not** contain a saved successful run of the optional real-SDK test.

## 02 / Native saved routes — actual transferred data and replay code

On October 10, 2026 the uploaded `arc3.rar` supplied game-specific saved action routes. Selected inputs were copied into a versioned [native ARC replay research directory](https://github.com/huntingthereferent/autobots-assemble/tree/main/research/arc_native_runs). The files below are **normalized exports of real archived action data**, with original-source references and hashes, not simulated win traces.

| Game | Saved action data | Actual executable replay | Reported local completion | Method/boundary |
| :--- | :--- | :--- | :--- | :--- |
| **FT09** | [75 coordinate clicks in six stages](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/ft09_route.json) | [Native SDK replay](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/replay_saved_paths.py) | **6/6 · 75 actions · score 100** | Source-assisted route; original local report also describes separate visual-agent experiments, not reproduced by this replay file. |
| **LS20** | [309 actions in seven stages](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/ls20_route.json) | [Native SDK replay](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/replay_saved_paths.py) | **7/7 · 309 actions · score 100** | Saved reference-assisted route; not independent first-contact discovery. |
| **SK48** | [280 actions in eight stages](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/sk48_route.json) | [Native SDK replay](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/replay_saved_paths.py) | **8/8 · 280 actions · score 100** | Archived saved-route script uses engine-private state to select ACTION6 coordinates; this is not a public-observation-only policy. |

[Reproduction instructions, original input hashes, and caveats](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/README.md) · [Detailed local case notes](SELECTED_WORK.md#01--interactive-environments) · [Claim and witness ledger](PROVENANCE.md#arc-native-game-experiments).

These newly published **action sequences** are a stronger artifact than narrative completion claims. They are not full per-step observations, independently re-executed scorecards, or the original autonomous policy source. The replay program has not been executed against the native SDK in this transfer environment.

## 03 / ARC-like finite-field mathematical research — public solvers and tests

This is a separate investigation of **constructed finite-state two-generator transformation systems**, not execution of ARC-AGI-3 native games.

| Mathematical artifact | Executable source | Tests or contract |
| :--- | :--- | :--- |
| Finite-field state-transition construction | [`math.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py) | [Finite transformation tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_like_inverse_ab.py) |
| Rooted relational alignment and finite closure | [`alignment.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/alignment.py) | [Alignment tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_like_alignment.py) |
| Bounded inverse construction | [`engine_one.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/engine_one.py) | [Engine 1 contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/ENGINE_ONE.md) · [tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_like_engine_one.py) |
| B-action continuation / witness verification | [`cyclic_action_engine.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/cyclic_action_engine.py) | [Cyclic Action Engine contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/CYCLIC_ACTION_ENGINE.md) · [tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_like_cyclic_action_engine.py) |
| Constructed-engine continuation and re-entry | [`cyclic_action_continuation.py`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/cyclic_action_continuation.py) | [Continuation contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/CYCLIC_ACTION_CONTINUATION.md) · [tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_arc_like_cyclic_action_continuation.py) |

The implementation and tests are visible; no statement here upgrades finite-field constructions into an ARC-AGI-3 game solver. Local/CI execution status must be checked separately before claiming a particular test result.

## 04 / Remaining evidence for independent game reproduction

The archive also contains additional experimental policies, alternate replays, local reports, and internal-state probes. Those have **not** all been uploaded into the public repositories. To establish reproducible solver results, the next evidence package still needs:

1. The original game-specific **policy/solver implementations**, exact versions, and dependencies; not only the saved successful routes.
2. Native SDK/environment version, reset rules, supported controls, and permitted observations.
3. Stepwise before/action/after observations or stable hashes tied to the particular run and policy.
4. Native complete-game states, scorecard outputs, and actual validation logs after fresh execution.
5. Separate result labels for source-assisted, reference replay, public-frame policy, and autonomous first-contact tests.

The [original FT09 visible-frame causal policy](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/ft09_visible_causal_agent.py) is now published as source with its machine-specific vendor import path removed. Its executed outcomes are reported locally; a fresh verified native run has not been captured by this transfer.

The [autonomous cyclic-agent trial outcomes](https://github.com/huntingthereferent/autobots-assemble/blob/main/research/arc_native_runs/AUTONOMOUS_TRIALS.md) also include unsuccessful native runs. A winning saved replay and a failed autonomous attempt are **different experiments** and must stay separately attributable.

**Current status:** actual saved routes and replay interface **PUBLIC**; public mathematical solvers and observer **PUBLIC**; full original game-specific development policies, per-step traces and fresh externally replicated results **INCOMPLETE**.

[Back to profile](README.md) · [Selected work](SELECTED_WORK.md) · [Provenance](PROVENANCE.md)
