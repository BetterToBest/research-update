# Handoff (Nov 8, 2026): S55 part 2, the growth rule and the preregistration (pilot running)

## Step status
S55 is **partly done**. Parts 1 and 2 (sub-steps 1-4) are done: the switch `PTF_ACCESS`, the growth rule, the addendum and amendments, and a pilot at seeds 1-50, now running. Remaining: part 3 (sub-steps 5 and 6). Check the pilot, size the shards, dispatch the 500-seed jobs, then write the report. Nothing is a result yet.

## What shipped
- compassionism-simulation [PR 82](https://github.com/BetterToBest/compassionism-simulation/pull/82), merged `0c93593` (checks and guard green). It adds the growth rule under `'open'`, with defaults `{grow: true, cap: 'own', ops: 'hub', dem: 0.49}`:
  - **Capacity:** the PTFs' own capital, c = c0 + capital per adult ÷ $18,862 (d101). The d137 borrowing still serves membership only.
  - **Operations:** the BLEI paper sets PTF prices at cost, so this limit never binds. With outside running costs (step 5 margins), sales cover 65%/47% of costs and the share stays at its start.
  - **Demand:** a labelled ceiling of 0.49 (S Group's 49.0% of Finland's grocery sales, 2025, PTY/NielsenIQ), swept at 0.25, 0.75 and 1.
  - New keys `paCap`, `paOps`, `paDem`, `paCv`, and the paths `paS*` and `paC*`. Records: `dev/DECISIONS.md` (S55 part 2) and `dev/reports/s55-ptf-growth.md`.
- compassionism-sim-results [PR 21](https://github.com/BetterToBest/compassionism-sim-results/pull/21), merged `30e0b21`: `program.js` studies T, U, U10, V, V10, VJ, W, W10, Y. Its `--check` confirms every open row is a frozen row with `pa` added.
- research-update PR 65: `prereg/2026-11-ptf-access-addendum.md` (Q24-Q28; headline Reference, 10,000 adults, 20 years, C2.2). Also study programme Amendment 11, layer addendum Amendment 2, run manifest Amendment 6 (jobs, about 108 runner-hours), and PLAN.md.

## Checks
- Guard test identical (25 rows × 20 seeds × 483 outputs, three environments). Lineage link 8bb948abed0e → 68b5d6170719, all six panels unchanged.
- `validate`, `unit` (257) and `domtest` (153) pass. `unsourced_check`, `study_data --check` and `glossary --check` pass.
- Smoke run: T's members-only rows equal `prog-a-ce8d030` for seed 1 on all 55 kept measures.

## In flight (GitHub Actions, workflow run-study, engine `0c93593e1ea502555387e42215b79f290a60f127`, seeds 1-50, 500 adults, 20 years, 1 shard each)
- [Run 81](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42451976202) `pilot55-t` (with `--members`); [82](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42451978934) `pilot55-u`; [83](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42451981351) `pilot55-v`; [84](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42451983498) `pilot55-w`; [85](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42451985431) `pilot55-y`.
- Results land in `pilot55-<t|u|v|w|y>-0c93593/` with `DONE` when in. First check: T's members rows (`*.cps.main`) must equal `prog-a-ce8d030`'s for seeds 1-50 on every kept measure.

## Decisions waiting
- None new.

## Next step
**S5** (participation threshold; sonnet, medium) is next in the Order table. **S55 part 3** (opus, xhigh) can start once the pilots are `DONE`: check them, set shards from their timings (manifest Amendment 6), dispatch the nine 500-seed jobs, then report. S39 can also start. S7 waits on S5 and S55.

## Pitfalls
- `earlier-engine.html` carries the page's script. Run `python3 dev/tools/sync_earlier.py` after any engine edit, or domtest fails on drift.
- A `PA` object built by hand in a test now needs the growth defaults (`Object.assign({}, PA_DEFAULTS, ...)`).
- The reporting hook is called twice for year 0. Count years by index, not by calls.
- The worker restarted twice this session. Long local runs (lineage, about 15 minutes) survived on disk, but check `git status` after a restart.
