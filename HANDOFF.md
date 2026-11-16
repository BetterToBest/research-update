# Handoff (Nov 16, 2026): S24 part 3 (held engine statements landed)

## Step status
**S24 is partly done.** Landed: C23-C30, C01-C22, and now the four held items (C08, C09, C11, C13) and the AI files' `features` list. **Remains** below.

## What shipped
- research-hub [PR 20](https://github.com/BetterToBest/research-hub/pull/20) (merged, 141b2ec): C08, C09, C11, C13 on `index.html` and `research-summary.html`, log entries in `corrections.html`. Each was checked against simulation v5.9.1 (engine c890ba3):
  - C08: the shipped engine gates θ on the SZH zone-coherence slider; the harness has an off-by-default `THETA_GATE='density'` switch for the restudy. Text says both.
  - C09: engine gives γ 0.20 to CCO participants from enrollment, 0.12 to others (`index.html` line 2770). Package text is right.
  - C11: 0.025 is an engine input (`FBS_EDC_RESIDUAL_PTH`); 0.62 is the paper's profile, not a measured baseline. Package text is right.
  - C13: engine credits $990 (BU x 990/1200); $2.75 stays labelled an assumption differing from ε_food 2.64. Package text is right.
- bettertobest.github.io [PR 5](https://github.com/BetterToBest/bettertobest.github.io/pull/5) (merged, 6b648b7): C17 `features` list (validation suite is six checks; "13-source" count dropped, not re-verified).
- Neither repository has checks. Ledger written (D29 resolved, log, left); `ledger-sync/` emptied.

## Remains for S24
- Paper bodies: C23, C26, C24, C27, BLEI worked examples (the $2.75 / 0.625 figures may also sit in the BLEI paper); S29's items (`audits/corrections-additions.md`); S30's actions; regenerate `data/claims.csv` (`tools/class_claims.py`); rebuild PDFs for any paper changed.
- The package's ledger CSVs were offered by Duke; not needed yet.

## Decisions waiting
None. (The held-items question was answered by checking, so it was not added.)

## Next step
S24 again (sonnet, medium): paper bodies first, then S29/S30 items and claims.csv.

## Pitfalls
- Clone research-hub and the root site one at a time (proxy cap); both are shallow.
- `/v1/` stays frozen.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
