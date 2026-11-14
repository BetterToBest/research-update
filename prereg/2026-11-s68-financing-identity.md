# Preregistration: the financing identity, the flat contribution's funding gap, and costs at the within-year price level (S68, items 5 and 6)

Committed Nov 14, 2026 by S68, before the engine change and before any run. Engine: compassionism-simulation at commit `3f8ae15` (main, S62 merged). The changes land on branch `claude/s68-financing-identity`, off by default (guard test identical). The engine commit of the pilot is recorded in an amendment before the pilot runs.

## Why
The Nov 13 audit (`audits/2026-11-13-simulation-audit.md`, finding 1) found that the C2.2 design paid for by a flat contribution on wages (ledger D21) needs a contribution averaging 84% of wages, that the rate sits at its 90% cap by year 20 in every seed, and that the 39-52% of the programme's cost the capped contribution does not raise is paid by no one in the engine's books. The progressive and land-value taxes count that shortfall as new money; the flat contribution, and the taxed part of the `hybrid` and `source` readings, count it nowhere. Finding 4: under today's price rule, run in quarters, prices average about 12.6% above the year's opening level during the year (S67), while households are charged opening prices.

## What the engine does today (read before this file; not a result of any run)
In `tbRunCore` (`index.html`), each year: `need` is what the contribution is meant to pay (every programme dollar at face value under `tax`; the transfers and price cuts but not the conversions under `hybrid` and `source`); `C.tax` is what the contribution raised at last year's rate; `U` is the new money the price module receives.
- `tax` with `taxBase` 'prog' or 'land': `U = extra + max(0, need − tax)`.
- `tax` flat (no `taxBase`): `U = extra`. Whatever `need − tax` is left goes into the reported `treas` only.
- `hybrid`: `U = (1 − a)(conv − convM) + extra`; the transfers' `need − tax` goes nowhere.
- `source`: `U = bkU + extra` (new money for BU and conversions less the output that backs them); the transfers' `need − tax` goes nowhere.
- `money`: every programme dollar not matched by output is new money (`aT`, `a`, `eP`).
- `none`: transfers and price cuts unfinanced by design (the sessions 2-5 rule).
`extra` (the floor's unmatched part and the wage bonus) is new money in every reading and is not part of `need`.

## What is built
1. **The financing identity (an accounting check, `ACCT` id `fin`; no figure depends on it).** Each year, for every reading, the programme's payout at face value under that reading's timing equals taxes raised + new money for the payout (`U − extra`) + output that matches or backs it + the stated unpaid part (the gap, `max(0, need − tax)` where a contribution pays `need`, and the transfers and price cuts under `none`) − the surplus (`max(0, tax − need)`, raised beyond the payout). Tolerance as for the other identities (1e-9, relative). Its purpose is that every dollar has a named payer; a non-zero gap is not a failure of the identity, it is a stated line the row must print.
2. **An `fx` part `fin` (row option `fx: {fin: ...}`; not part of `fx: true`, so the frozen batch is unchanged).**
   - `'report'`: no change to any figure; adds the keys below.
   - `'money'`: the gap, where a capped contribution pays `need` (flat `tax`, `hybrid`, `source`), is new money, as for `taxBase` 'prog' and 'land'. `none` and `money` are unchanged (their definitions); `taxBase` rows are unchanged (they already do this).
   - `'debt'`: reserved for S72 (government borrowing at a sourced rate); the engine refuses it until then.
   - Keys (only with `fx.fin`): `finPay` (payout, per adult-year, year-0 dollars), `finTax`, `finMoney` (`U − extra`), `finMatch`, `finGap` (unpaid, before `fx.fin` acts), `finSur`, `finGapM` (the part of the gap made new money), `finGapSh` (gap over payout, %), `finCapYrs` (years at the rate cap).
3. **Costs at the within-year price level (study option `wy`, reporting only).** Each adult-year's cost of living times the year's within-year average price level over its opening level (`exp(avg)`, the record behind `prAvg`; 1 when the year is not split), basket poverty and its depth recounted: keys `wyF0PY`, `wyF1PY`, `wyF2PY` beside `fgt0PY`, `fgt1PY`, `fgt2PY`, and `wyAvg`. Read on the quarterly count of today's rule (S67: `pr: {q: 4, k: 1, a: 0, r: 0, h: 0, rs: false}`, which gives today's year-end prices and results in every key). Claude's reading: incomes are paid through the year in the year's nominal dollars and wages are indexed once a year, so the cost is the part that moves; the general level stands for every item (a modelling assumption; the sectors' own levels are not used).
4. **Per-run reset of module state (S68 item 2).** `PDS` and any other module-level record that a row can inherit from the previous row are reset at the start of each run; a run-order test (a no-programme row run after a programme row equals the same row run first, every key) becomes a unit test.

## Tests (unit suite; before the pilot)
- Off identical: guard test (25 rows × 20 seeds × every output, three environments); `fx: {fin: 'report'}` identical to off in every existing key; `wy` identical to off in every existing key.
- The `fin` identity holds (no failure) for `source`, `tax` flat, `tax` with `taxBase` 'prog' and 'land', `hybrid`, `money`, `none`, with and without `fx.fin 'money'`, on the release row and the C2.2 design, 2 seeds, Reference.
- With `fx.fin 'money'`, `finGap − finGapM` is 0 for flat `tax`, `hybrid` and `source`; `taxBase` and `money` rows are identical to `fx.fin 'report'`.
- `wy` with the year unsplit gives `wyF0PY = fgt0PY`.
- Run order: every key of a no-programme row equals itself whatever row ran before it.

## Pilot (session machine, free)
Seeds 1-100, 500 adults, 20 years, Reference, Adverse and Stress, CPS earnings (`lt: {s: 'all', m: 'all'}`), today's safety net, round-2 switches off (as the audit's check script):
- (A) Financing: no programme; the release design (Source); C2.2 paid by the Source; C2.2 with the flat contribution, `fx.fin` 'report' and 'money'; C2.2 with `hybrid`, 'report' and 'money'. Outcomes: `finGapSh`, `tauMean`, `finCapYrs`, `endoAnn` (programme inflation), `fgt0PY` (basket poverty), `pov` (wealth poverty, year 20, all-cash wealth), `hrs`; paired differences with 95% intervals.
- (B) Within-year costs: no programme; the release design; C2.2 (Source); on the quarterly count. Outcomes: `fgt0PY`, `wyF0PY`, their difference against the no-programme run, `wyAvg`.

## Decision rules (fixed now)
- (A) No row is carried by S63 under the flat contribution or `hybrid` without `fx.fin` set; S63 decides between 'money' and S72's 'debt' with S72's frontier in hand (D23 stands as filed: the Hub does not lead with the financed row until then). The release design and C2.2 under the Source are carried unchanged if their `finGap` is below 0.5% of payout in every environment; otherwise `fx.fin 'money'` applies to them in S63's main row too.
- (B) If the within-year reading moves the programme's effect on basket poverty (against the no-programme run) by 1 point or more in any design and environment, S63 carries `wy` beside every basket-poverty headline; below that, it is reported here and in MODEL_SPEC as a stated limit with its size.
- Every outcome above is published (compassionism-sim-results and the report), whatever its direction.

## Limits stated in advance
- Wealth poverty under the gap-as-money reading uses the frozen engine's all-cash wealth (S59 showed it overstates erosion); `rt` is not run here.
- The contribution's labour response is the engine's one elasticity (Chetty's 0.33), far outside the changes it was measured on at rates of 84-90%; avoidance and informal work are not modelled.
- `wy` does not split the engine's year: spending, saving and wealth are still at opening prices.
