# Handoff (Nov 16, 2026): S24 part 10, step closed

## Step status
**S24 is done.** Parts 1-10 landed. Only the simulation page's `CFG.TARGET_*` constants remain; they go with the next engine release (S40 follow-up or later), and simulation figures wait for S65 (D18).

## What shipped
- Earlier parts: PLAN.md's S24 note (Hub PRs 18-28, root site PRs 3-5).
- Part 10: research-hub [PR 29](https://github.com/BetterToBest/research-hub/pull/29) (merged, 6a03ede; the repository has no checks). Every parameter group in `data/optimal-parameters.json` now has a `basis` entry following S30's table (design parameter, assumption labelled optimal, result stored as a parameter, the $82,000 target, validation claims, package metadata). No value changed. Corrections log entry added. `tools/class_claims.py` rerun (11,173 figures, 3,022 no basis); no PDF changes were needed.
- Ledger written.

## Decisions waiting
None.

## Next step
S41 (site and wiki design refresh, sonnet, high; its dependency S40 is done).

## Pitfalls
- Clone research-hub one at a time (proxy cap); it is shallow.
- `/v1/` stays frozen.
- The GitHub plugin server failed to connect; the `mcp__github__*` tools worked.
- The Draft Act's yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
