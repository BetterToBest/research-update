# Handoff (Oct 30, 2026): S34 the no-programme baseline against outside data

## Step status
S34 **done**. The released no-programme run (v5.6, with today's safety net) was compared with CPS ASEC 2026, SCF 2025 and 2022, BLS 2025 and PolicyEngine-US, under a preregistration committed before any run (`prereg/s34-baseline-realism.md`, two dated amendments).

## What shipped
- compassionism-simulation #49 `claude/s34-baseline-realism`: `dev/reports/baseline-realism.md` (plain words, gap table), `baseline-realism-tables.md`, tools, `sources/baseline_realism_us.py`, `CFG.CPS_EARN` behind the existing wage reading (off by default; guard identical, lineage link bc0422920f8c), DECISIONS entries. Merge state: see "In flight".
- compassionism-sim-results #3 (merged, 292c166): `s34-baseline-realism-e8f8a77`, with run.txt, SHA256SUMS, DONE.
- research-update: prereg file; PLAN.md marks S34 done and adds Q6 (the yardstick choice) to S32.

## Findings that change later steps
- **Safety net:** the engine matches PolicyEngine-US for six households (within $10; one $138 CTC difference from the missing child and dependent care credit).
- **Wages:** the model's wage scale came from the median personal income of everyone 15+ ($42,220); every model adult is 25-64 and works full time. Median earnings $39,200 against $60,000. With CPS earnings (`lt: {s: 'all', m: 'all'}`), no-programme basket poverty falls from 49.2% to 27.1% and too little wealth from 32.7% to 20.3%. S32 must preregister both yardsticks and fix which one the headline uses before any result (Q6).
- **Scope:** nobody in the model is out of the labour force (US: 19% of adults 25-64 have no earnings). For S24: the Hub should say "working adults and their families".
- **Open:** household debt drifts from 15.5% to 33.4% in 20 years (SCF 9.3%); this is the spending rule, not ageing. For S32/S47.

## In flight
Nothing. If #49's checks were not green at session end, it stays open: read its CI first.

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped.

## Next step
**S33** (study runner on GitHub Actions, runtime benchmarks), sonnet, high: next in the Order table, and it waits on nothing. S32 needs S33 and S34. The chain is paused (`AUTOCHAIN.md` off), so Duke starts it by hand.

## Pitfalls
- The v5.6 release panel already has today's safety net in every run (`--snab --slope`). "No programme" means that run, not `relMainCfgs(PR)[0]` alone.
- After any engine edit, run `python3 dev/tools/sync_earlier.py`, or domtest fails (functions drift between pages).
- A `node_modules` symlink in a worktree makes the run manifest dirty. Run studies from a clean worktree without it.
- `pkill -f <pattern>` killed the session's own shell again. Kill by PID.
- The safety-net check needs `snBenAt` (harness export), because `SNET` is internal to the harness.
- The outside microdata (CPS 139 MB zip) is not in any repository. `sources/baseline_realism_us.py` documents the URLs.
- Commit trailers: use `Co-Authored-By: Claude <noreply@anthropic.com>` (no model names).
