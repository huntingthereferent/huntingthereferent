# From relation to execution to evidence

**A source-linked reading path for Hunting the Referent and Tracework** · October 27, 2026

[Research profile](../README.md) · [Research method](RESEARCH_METHOD.md) · [Mathematical index](../showcase/MATHEMATICS.md) · [Tracework implementation and scope](https://github.com/huntingthereferent/autobots-assemble/blob/main/TRACEWORK.md) · [Evidence register](../RESEARCH_REGISTER.md)

This guide makes the connection between a **declared relationship**, the **code that implements or tests it**, and the **returned witness** inspectable. It does **not** assert that all of the linked experiments implement one theorem or that any finite demonstration proves an account of human cognition.

Read each path in order: **question → defined boundary → implementation → observed return → counterexample/unknown → permissible next move**. The native source owns the outcome; Tracework records and supports continuity across the investigation.

## 1. Finite A/B convergence: a complete bounded example

**Question.** Can *different action histories* in one specified finite system reach the same state, with their steps independently checked?

**Model and admissible moves.** The [source `World.step`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py) uses states `(x, y, z)` in `(Z/3Z)^3`, starting at `(0, 0, 0)`, with `phi = (0, 1, 2)`. Its two actions are:

```text
A(x,y,z) = (x+1 mod 3, y, z)
B(x,y,z) = (x, y+x+1 mod 3, z+phi[y] mod 3)
```

These are the operators of this **particular finite model**, not a definition of James's language referent or a claim about ARC's real game controls.

**Execution and independent comparison.**

- [`World.apply`](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/math.py) applies each declared action in order.
- [`discover_convergence`](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/convergence.py) explores paths without preselecting a winning endpoint. On each step it compares `World.step` to [`_independent_step`](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/ab_relational_cluster.py), which does not call `World.step`. It replays both complete paths before returning a meeting state.
- [The machine-readable receipt, recorded at the pinned source revision](https://github.com/huntingthereferent/autobots-assemble/blob/702326a0d9c0dc8e9225b4cdd4d9a8c333b778f5/views/motion/convergence-receipt.json) records the returned paths, target, and search count. Its relevant fields are:

```json
{
  "schema": "finite-ab-convergence/v1",
  "left_word": "BBAA",
  "right_word": "ABABB",
  "target": [2, 2, 1],
  "initial": [0, 0, 0],
  "states_explored": 14
}
```

**Reproduce against the implementation repository**, from its root:

```sh
python -m unittest -v views.motion.test_convergence
python - <<'PY'
from work.arc_like_maze.math import World
from views.motion.convergence import discover_convergence

world = World(3, (0, 1, 2))
receipt = discover_convergence()
assert "status" not in receipt  # a real match, not OPEN
assert world.apply(receipt["left_word"]) == tuple(receipt["target"])
assert world.apply(receipt["right_word"]) == tuple(receipt["target"])
print(receipt)
PY
```

This command is a **reader-executable check**, not a claim that this profile documentation ran that command today. If a step disagrees with its independent verifier, the search raises an error; if no matching paths are found within the bound, it returns `OPEN` and the renderer refuses to draw a joined relation. The [source visual](https://github.com/huntingthereferent/autobots-assemble/blob/main/views/motion/README.md) is a *read-only rendering* of the witness, not another worker or an external-world proof.

**What survives:** the declared finite state/action semantics, independently compared transitions, and two different action histories reaching a shared endpoint. **Not established:** convergence in all finite systems; identity of the two histories; an ARC win; or universal continuity across domains.

## 2. A separate geometric construction: growing a periodic projection

**Question.** Does a specified scaling map preserve the *declared periodic coordinate relation* when a finite world grows?

The [language-neutral shape contract](https://github.com/huntingthereferent/autobots-assemble/blob/main/language/SHAPE_CONTRACT.md) introduces the periodic family `W_N = Z_N × Z_N` and the embedding `E_k(x,y) = (kx,ky) mod kN` for integer `k >= 2`. It proposes adapting finite resolution to the represented relationships. That is a design rule and bounded testable construction, not a proof about every representation.

The [actual Python implementation](https://github.com/huntingthereferent/autobots-assemble/blob/main/work/arc_like_maze/toroidal_projection.py) computes the scaled `side` and coordinates in `ToroidalProjection.grow` and checks coordinate identities in `validate_growth`. For movement, a one-cell shift at resolution `N` corresponds to a `k`-cell shift at resolution `kN`:

```sh
python - <<'PY'
from work.arc_like_maze.toroidal_projection import ToroidalProjection

p = ToroidalProjection.from_paths(("source/a", "source/b"), side=4)
grown = p.grow(2)
assert p.validate_growth(grown, 2)
assert p.move("source/a", (1, 0)).grow(2).positions == (
    grown.move("source/a", (2, 0)).positions
)
print(p.positions, grown.positions)
PY
```

**What survives:** source path identifiers and coordinates under the explicitly checked scaling, plus this matched movement example. **What does not follow:** that geometric proximity indicates semantic relatedness, that a projection collision proves identical objects, or that the scaling implements the language referent. This construction is **not** used as an explanation for the NIH source-data counts below.

## 3. Real-data referent continuity: NIH/AACT is a different native boundary

**Question.** Which study identifiers occur in both independently authenticated deposited AACT exports, and which paired `overall_status` strings differ?

| Stage | Actual source or operation | Claim it supports |
| --- | --- | --- |
| Source objects | [Two original archives, provenance, owner/deposit dates and hashes](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) | Two deposited datasets were verified as their respective original artifacts; their underlying observation order is not established by deposit date. |
| Identity admission | [`scan_verified_tables` in the comparison source](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/nih_p2_historical_status_difference_search.py) | Only exact `nct_id` equality joins rows; duplicate or malformed IDs fail the scan. |
| Value comparison | [`normalize_status` and the paired-record scan](https://github.com/huntingthereferent/autobots-assemble/blob/main/systems/workspace/nih_p2_historical_status_difference_search.py) | Case and outer whitespace differences are separated from different normalized status strings; original spellings and recorded dates remain in selected anchors. |
| Negative controls | [Fixture tests](https://github.com/huntingthereferent/autobots-assemble/blob/main/network/tests/test_nih_p2_historical_status_difference_search.py) | Invalid data must fail; fixtures do not independently establish real archive totals. |
| Native result | [Pinned source report and evidence limitations](https://github.com/huntingthereferent/autobots-assemble/blob/7916709e16e14cb1222639f385746abc882effe1/systems/workspace/NIH_P2_STATUS_DIFFERENCE_SEARCH.md) | **432,597 shared NCT IDs**, **1,345 differing normalized status fields** across these two files. |

**Reproduction boundary.** The source report specifies a network-enabled full-source scan and separately describes fixture tests. A reader running only unit fixtures has *not* reproduced the archive observations. An exact source-ID join is not a consequence of the torus example or evidence that `referent_traversal.py` computed these counts.

**Preserved counterexample / unresolved edge.** The earlier selected two study IDs both showed `Completed` in both files. The wider scan uncovered differences but also evidence that the later-published deposit may contain earlier underlying source rows. Therefore the differences are **paired source-field discrepancies**, not proven chronological status transitions or clinical changes. The original underlying extraction-date ordering remains unresolved.

## 4. Native ARC movement: failure is evidence, not a successful demonstration

**Question.** What actually happened when actions were sent to the original ARC/SP80 SDK?

The [ARC evidence record](../ARC_EVIDENCE.md) links the domain-specific source, native runs, and known limits. Two entries reached official **level 4/6**. In a later **52-reset** level-4 experiment, the [native workflow witness](https://github.com/huntingthereferent/autobots-assemble/actions/runs/39636174534) did **not** reach level 5 or WIN. A simulated trajectory, visual approximation, or successful unit test cannot promote that return to a native success.

The useful chain is: **last native state → admitted action → actual SDK return → observed discrepancy → next bounded correction (if one is made) → new native return**. A failed movement must remain inspectable; it is not deleted because a subsequent hypothesis looks better. No further trial is claimed here without its own native evidence.

## 5. How Tracework can carry a stopped relation without silently repairing it

The [referent traversal runtime](https://github.com/huntingthereferent/autobots-assemble/blob/main/runtime/referent_traversal.py) defines a `ReferentFrame` (referent, direction, current record, what survives, edge, walls, provenance) and a `ReferentMove` (one of `MOVE`, `WALL`, `UNKNOWN`, `PARTIAL`, with evidence and changed relationships). Its transition helpers are a more accurate implementation anchor than describing the whole method as `if/else` checks or CI blockers:

- `next_frame` admits an actual `MOVE` and carries its surviving relationships and provenance forward.
- `wall_frame` makes the stopped relationship available for a regrounding pass, carrying the reached observation and changed relationships.
- `failed_reground_frame` and `failed_swallow_frame` append the failed attempt and its evidence rather than redefining a wall as solved.
- `swallow_frame` makes outward source search possible *without* treating discovery as proof.

These are **specific implemented structures**, not proof that every ARC runner uses this class or that every unresolved attempt automatically selects a correct next action. A/B corrective movement is meaningful when **actual observed differences inform the next permitted test**; a failure alone does not guarantee improvement.

## 6. Vocabulary bridge: operational correspondences, not replacements

| Research language | What a developer can inspect | Boundary |
| --- | --- | --- |
| **Mismatch-driven attention / correction** | Proposed and native-returned observations compared, with differences retained; an assertion or CI gate may enforce a narrower check. | No CI assertion alone defines the broader cognitive process. |
| **Preserving what I mean as it moves** | `ReferentFrame`, survival/change fields, original source identity, provenance, and re-entry under a known edge. | Not synonymous with copying the same object state or identifier. |
| **Regrounding / continuation** | `wall_frame`, failed-attempt records, explicit evidence paths, next permitted move. | An unresolved wall remains unresolved until another witness supports movement. |
| **Truth-telling / parrhesia** | A software design analogue is retaining negative results, origin, and limits, and refusing unjustified promotion to success. | The ethical and personal practice is not reducible to a log-retention policy. |
| **Finite A/B operators** | `World.step`, replay, the independent step verifier, and bounded search receipts. | Not a complete formalization of the language referent, person, or human cognition. |
| **Source-backed comparison** | Original hashes, source IDs, admission/normalization rules, native witness, and explicitly unresolved fields. | A source digest authenticates bytes under its contract; it does not prove an inferred interpretation. |

## 7. Evidence admission checklist

For any new connection presented as **mathematics → code → result**, require:

1. **Same question:** state exactly which defined relation the implementation computes; don't reuse the same word for unrelated relations.
2. **Same source boundary:** link to the code revision, input, native environment or archived original that actually supplied the return.
3. **Executable transition:** show the method/function and admitted parameters, not merely a nearby source file.
4. **Check independent of presentation:** retain a comparator, alternative replay, source-owned test or native return; be specific about what is independent.
5. **Failure and scope:** retain failed paths, unknowns, contradictory returns, bounds, and external-verification status.
6. **Next movement:** identify what evidence would settle the open edge rather than turning an unresolved claim into a polished conclusion.

See the [research method](RESEARCH_METHOD.md) for the underlying admission procedure and the [research register](../RESEARCH_REGISTER.md) for independently scoped projects and negative controls. **The reader should be able to follow one relation without being asked to assume another.**
