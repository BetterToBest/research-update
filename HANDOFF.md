# Handoff (Nov 2, 2026): S52 partly done, the outside supply shock (pilot dispatched)

## Step status
S52 is **partly done**. The reading, the engine switch, the calibration and the preregistration have landed, and the 50-seed pilot is running on Actions. What remains is the pilot report and the list for S47 (next session).

## What shipped
- compassionism-simulation [#64](https://github.com/BetterToBest/compassionism-simulation/pull/64), merged `98b6100`. The outside supply shock, preset key `sx`, off by default: guard test identical, lineage linked, 4 unit tests. Also the reading for Duke (`dev/reports/s52-supply-shock-reading.md`), the calibration (`sources/s52_energy_shock.py`, US CPI 1967-2024 in `sources/energy/`), the choices (`dev/DECISIONS.md`, S52) and the preregistered analysis (`dev/tools/s52_shock.py`).
- compassionism-sim-results [#12](https://github.com/BetterToBest/compassionism-sim-results/pull/12), merged `aee7d7c`: `runner/jobs/shock.js`, study O, 70 rows per environment (`--check` passes).
- research-update [#37](https://github.com/BetterToBest/research-update/pull/37), merged `efb4bcf`: `prereg/2026-11-supply-shock-addendum.md` (study O), study programme Amendment 6, and PLAN.md (S52 partly done; study O added to S47's list).

## What the design reading says (before any run)
- PTF removes the markup part of a price rise and pays the real-cost part in dollars, except the part it sources locally. Transport is outside PTF.
- PTH removes the rent markup, and an energy shock does not move rents. So PTH protects against this shock only through PTF membership.
- The BU absorbs price rises for participants while it covers their basics. Own cost is money cost, so the groups keep the BU's protection apart from PTF's.
- Main shock: real energy price up 32.8% over two years from year 5, with 88% kept afterwards. The market basket rises about 2-3%.

## In flight
- Study `s52-shock` on Actions: engine `98b61000697078619b496b1cca0f3bf495de73b2`, seeds 1-50, job `shock.js --env=all --procs=4`, 10 shards. Run: https://github.com/BetterToBest/compassionism-sim-results/actions/runs/41384997243 (dispatched 03:47 UTC, started). Results land in compassionism-sim-results `s52-shock-98b6100/`; `DONE` appears there when every shard is in.

## Decisions waiting
- None new. D12 and D13 are confirmed in the ledger: test every lever first (S54); "no harm first, then lowest basket poverty, inflation under 5%" is S54's selection rule.

## Next step
**S52 again**: check `DONE`, run `python3 dev/tools/s52_shock.py <folder> --out dev/reports/s52-supply-shock-tables.md`, then write the plain-words report `dev/reports/s52-supply-shock.md` (labelled pilot; decision rules 1-6) and the list for S47. Then S53, S54 and the S47 freeze.

## Pitfalls
- `pgrep -f "harness.js testbed"` matches the waiting shell's own command line, so a wait loop on it never ends. Watch the lineage tool's output file instead.
- The shock is a preset key, not a row option. A study's `envP.sx` must equal its rows' shock path, because household rows take their supply path from `envP`. `shock.js` runs each path as its own study.
- Unshocked rows use a shock of size 0. It changes no figure (unit test), and it is what writes the `sx*` measures the pairing needs.
- A 2-seed code test on the session machine suggested PTF's markup removal saves PTF members only a few points of the shock, and the BU much more. That is a code check, not a result. Do not quote it.
- Use the `Co-Authored-By: Claude <noreply@anthropic.com>` trailer only. The two stray branches named in the last handoff are still there for Duke to delete.
