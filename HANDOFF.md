# Handoff (Nov 16, 2026): S24 part 9 (derivation items, printed code)

## Step status
**S24 is mostly done.** Parts 1-9 landed. **Remains** below (small).

## What shipped
- Earlier parts: see PLAN.md's S24 note (Hub PRs 18-26, root site PRs 3-5).
- Part 9: research-hub [PR 27](https://github.com/BetterToBest/research-hub/pull/27) (merged, 512bc57; the repository has no checks). Of the 23 derivation and table items, 12 were already fixed by earlier parts or S46 (A04, A06, B013, B019, B023, B032, B035, B067, B070, B072, B076, B108). The rest are now corrected or labelled: B002 (elasticity column recomputed from the table's own values and marked illustrative), B007/B034 (merchant-multiplier example), B008, B010, B012, B030, B038, B045, B060, B079. S30 actions: "10,000 iterations" described as a design never run; Appendix A code marked illustrative pseudo-code, not run; BLEI Month 12 and 60 state the $232 a month saving they need (Month 60 now about 1,270 days, not 1,328); real estate $168,000-336,000 vs $70,000 flagged as unreconciled; Draft Act section 102 gains the child allowance. Six PDFs rebuilt, class_claims rerun (11,172 figures, 3,022 no basis), corrections log entry added.
- Ledger written (log only).

## Remains for S24
- Draft Act section 102: done. Duke (Nov 16): opt-in or opt-out is a policymakers' choice, and the amount follows the cost of basics, adjusted yearly. Act and transfer-design paper now say so (Hub PR 28). The yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- PTH financing section 8 has no figures, so nothing was changed there; the handoff item likely meant section 9 (done).
- Check `data/optimal-parameters.json` is fully labelled per S30's table (its provenance note exists; per-value labels do not).
- The simulation page's `CFG.TARGET_*` constants (S40 or the next engine release). Simulation figures wait for S65 (D18).
- After any edit rebuild the PDFs (the roadmap page has none) and rerun `tools/class_claims.py`.

## Decisions waiting
None. (D8 is the C2.2 coverage design choice, not this question; the earlier handoff cited it wrongly.)

## Next step
S24 can be closed after the parameter-file labels; otherwise the next startable step in PLAN.md's Order table.

## Pitfalls
- Clone research-hub one at a time (proxy cap); it is shallow.
- `/v1/` stays frozen.
- The GitHub plugin server failed to connect; the `mcp__github__*` tools worked.
- Many audit rows were stale; grep the page before editing.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
