# Audit of the Simulation after the round-2 build steps (Nov 13, 2026)

Asked for by Duke in Chat on Nov 13, after S62 and before S68: audit the most recent additions to the Simulation and the general state of the project, and say what else could be added to close gaps or resolve limits. It follows the Nov 9 audit (`audits/2026-11-09-simulation-audit.md`) and checks how that audit's findings were closed.

Like the Nov 9 audit, this one was written by the same kind of AI system that built the engine and wrote that audit. It is not the independent economist's review the project still lacks. Finding 1 below is a mistake the Nov 9 audit made and did not catch.

## What was checked, and how

- compassionism-simulation at `3f8ae15` (S62 merged): `node harness.js validate` passes; `node harness.js unit` passes (328 tests, 0 failed); `node dev/tools/guard_test.js` passes (25 rows × 20 seeds × 483 outputs identical in all three environments).
- Read: both handoffs; PLAN.md's sections for S59-S71 and S63; the Limits sections of the S57, S58, S59 (both parts), S60, S61, S62, S66, S67 and S71 reports; MODEL_SPEC.md sections 2, 6.1, 6.10-6.12 and 12.5; the S54 levers report and its tables; the engine's financing block (`index.html`, the lines that set `need` and `U` for each `o.fin`).
- Run for this audit (analysis only, no engine change committed): the C2.2 design paid for by a flat contribution on wages (ledger D21), on the frozen row with the round-2 switches off, seeds 1-20 (Reference) and 1-10 (all three environments), 500 adults, 20 years. Tool: `audits/2026-11-13-financed-row-check.js` (usage in its header; `--gap` runs a temporary patched copy of the engine).

## Summary

The round-2 build is in good order. Every switch is off-identical, preregistered, built from opened sources, and piloted at 100 seeds, and its limits are written down. S67 reversed S58's own recommendation by a rule fixed in advance, and S66 and S71 published results that cut against earlier readings. Of the Nov 9 findings, 1 (all wealth is cash) and 2 (the price rule) are closed. Findings 3-5 wait on S68-S70, as planned.

The most important new problem:

1. **The financed row the Hub may now lead with is not financed (finding 1).** The C2.2 design paid for by a flat contribution on wages needs a contribution averaging 84% of wages. The rate sits at its 90% cap by year 20 in every seed. The 39-52% of the programme's cost the capped contribution does not raise is paid by no one in the engine's books: it is neither taxed nor counted as new money. Its "0.1 points of inflation a year" comes from that gap. Counted the way the engine already counts the progressive and land-value taxes' shortfalls, inflation is 22-35% a year. Basket poverty still falls by 8-18 points, but wealth poverty rises above the no-programme run (on the frozen engine's all-cash wealth).

The most useful additions, in order:

1. A financing identity for every financing reading, and the flat contribution's gap fixed behind a switch (in S68).
2. A government budget line and a financing frontier: inflation against contribution rate, for shares of the payout financed from 0 to 100% and for wider contribution bases (new step).
3. The participation margin and movement in and out of the labour force (new step). S60's validation fails on it, and it moves both inflation and any contribution's base.
4. Costs counted at the year's average price level, not its opening level (a reporting reading in S68).

## Findings

Severity: **A** blocks a published claim · **B** fix before the round-2 freeze (S63) · **C** worth doing later.

### 1. The C2.2 design paid for by a flat contribution has a hidden funding gap (A)

**What the engine does.** With `o.fin === 'tax'` and no `taxBase`, the contribution rate for each year is `min(tauMax, need / base)`, with `tauMax` 0.90 and the base being wages only. New money is then `U = extra + (o.taxBase ? max(0, need − tax) : 0)`. For the progressive and land-value taxes, whatever the capped tax does not raise becomes new money. For the flat contribution, the term is zero. The unpaid part goes into the reported `treas` key and nowhere else. MODEL_SPEC 12.5 describes the contribution only for the release row's price cuts, where the rate is 1.6-3.5% and the cap never binds.

**What it gives for the D21 row** (frozen row, 500 adults, 20 years; `audits/2026-11-13-financed-row-check.js`):

| Environment, seeds | Mean contribution, % of wages | Year-20 rate | Programme cost per adult-year | Raised by the contribution | Paid by no one | Inflation, engine as committed | Inflation, gap counted as new money |
|---|---|---|---|---|---|---|---|
| Reference, 1-20 | 83.8 | 90% in 20 of 20 seeds | $79,860 | n/a | n/a | 0.08% | n/a |
| Reference, 1-10 | 83.8 | 90% in 10 of 10 | $79,520 | $48,440 | $31,080 (39%) | 0.08% | 22.3% |
| Adverse, 1-10 | 83.9 | 90% in 10 of 10 | $77,830 | $36,990 | $40,840 (52%) | 0.11% | 34.6% |
| Stress, 1-10 | 83.5 | 90% in 10 of 10 | $66,460 | $35,790 | $30,670 (46%) | 0.11% | 30.4% |

Outcomes against the no-programme run on the same seeds (seeds 1-10; percentages of adults or adult-years; Adverse and Stress share one no-programme run):

| Environment | Basket poverty: none / financed as committed / gap as money | Wealth poverty at year 20: none / as committed / gap as money |
|---|---|---|
| Reference | 27.8 / 10.3 / 14.6 | 22.3 / 6.7 / 60.7 |
| Adverse | 40.0 / 11.0 / 22.0 | 32.5 / 9.1 / 94.3 |
| Stress | 40.0 / 15.0 / 31.5 | 32.5 / 15.3 / 95.5 |

Hours (key `hrs`) change by −17% to −29% in the financed rows, against −1% to −2% in the no-programme run.

**Why it matters.**
- D21 was answered on Nov 9: "Yes, and the Hub may lead with it beside the design's own financing." That answer rested on the S54 pilot's "0.1 points of inflation a year, basket and wealth poverty down 18-29 points". The Nov 9 audit (finding 6) recommended the row on the same figures and checked neither the rate nor the treasury.
- The root fact is plain. The C2.2 design pays out about $60,000 per adult a year in Reference, about 70% of what the no-programme economy's adults earn in wages ($84,000). No contribution on wages alone can pay for that under a 90% cap. S51 and S54 reached the same point by another route: no setting inside the design gets its inflation under about 21% a year.
- The gap-as-money reading is not a fix. It is the reading consistent with the engine's other taxes. Its wealth figures use the frozen engine's all-cash wealth, which S59 showed overstates erosion; with `rt` they would be smaller, and they were not run here.
- A rate of 84-90% on all wages is far outside the evidence the labour response rests on (Chetty's 0.33 comes from much smaller changes). Avoidance, informal work and shifting effort to conversion income, which is not in the contribution's base, are not modelled.

**Fix.**
- (a) In S68: an accounting identity for every financing reading (`source`, `tax` with and without `taxBase`, `hybrid`, `money`, `none`): the programme's payout equals taxes, plus new money, plus matched output, plus a stated outside or borrowed part, on every seed and year. `hybrid` has the same pattern and should be checked.
- (b) In S68: the flat contribution's gap put behind an `fx` part. Its options are the gap as new money (as for the other taxes), or as government borrowing (finding 2). This keeps the frozen batch reproducible.
- (c) S63 carries no financed row until (a) and (b) are in. The row is labelled with its rate and the share of cost each source pays.
- (d) Decision for Duke (D23): whether the Hub may still lead with the financed row once it is computed consistently.
- No published figure changes yet. The frozen batch did not carry this row (it came from the S54 pilot), so this touches D21 and the plans built on it, not a release.

### 2. There is no government budget, so deficits and gains go nowhere (B)

MODEL_SPEC section 2 places the government budget outside the model. Four results now lean on what that leaves out:
- The financed row's deficit (finding 1).
- The 30 cents of every dollar of household debt inflated away that S71 assigns to government, as a gain.
- The erosion of the government's own debt at 30-45% inflation.
- The cost of today's safety net (SNAP, EITC, CTC) under the programme's prices.

Nov 9's ranked improvement 8 (ECONOMIST-REVIEW.md row 13) proposed a budget line "later". Finding 1 makes it needed before the freeze, because it is the only way to state honestly what a financed design costs.

**Addition (new step S72, opus high, before S70 and S63):**
- A government account for every row: taxes, the contribution, transfers including today's safety net, the deficit, and the stock of public debt.
- Three named readings of how a deficit is met: new money, borrowing at a sourced real rate with interest paid from the account, and a higher rate cap.
- A financing frontier. The share of the payout financed by contribution (0, 25, 50, 75, 100%), times the base (wages; wages plus conversion proceeds; all money income), times the cap (0.5, 0.7, 0.9). For each cell: inflation, the rate and who pays it, basket and wealth poverty. Both designs, three environments, reduced seeds.
- D21's row becomes one point on a curve a policymaker can read: for example, what contribution keeps the C2.2 design's inflation under 5% a year.

### 3. Nobody stops working because of the programme, and labour status never changes (B)

- S60's validation fails on participation: 0.0 points in the engine against −4.2 in the US experiment (Vivalt et al. 2026). The engine puts the whole income effect on earnings within work.
- S61's adults outside the labour force keep their status for 20 years. Its report lists that as a limit (no sourced transition rates). The Nov 9 audit ranked it 6th.
- Both bear on the headline through the price rule. Fewer earners mean less income `Y` for the same new money, so more inflation under the Source's financing, and a smaller contribution base under any tax.

**Addition (new step S73, opus high, before S70):**
- Yearly transitions in and out of the labour force by age, sex and household type, from CPS matched months or SIPP, replacing fixed status.
- A programme effect on leaving work, taken from the income effect by one rule, so the elasticity used for every change in the return to work stays one. Validated against Vivalt et al.'s −4.2 points and hours −1 to −2 a week, as a check, not a target.
- Behind a switch, off identical. Unit tests; pilot at 100 seeds.
- Its participation reading joins S70's screen, as S70's section already asks ("the missing participation margin is listed as a structural limit to test"). Today there is nothing to screen.

### 4. Households shop at the year's opening prices while the programme's prices rise during the year (B)

- S67 found that under today's rule, run in quarters, prices end the year 12.6% above their opening level. Households still buy at opening prices, because the engine's year is not split.
- So real incomes under the programme are counted at prices lower than those households would meet during the year. No-programme prices hardly move (0% outside inflation in Reference).
- S67's finding that basket poverty does not depend on the price rule holds on the yearly step under both rules, so it does not cover this.
- The size of the effect on basket poverty is not measured. For households near the basket line it could be several points.

**Addition (in S68, reporting only):** basket poverty and the cost-of-living measure with each year's costs at the within-year average price level (`prAvg`, quarterly count), beside the published measure, for both designs and three environments. If the difference is material, S63 carries it as a reading on every basket-poverty headline.

### 5. S68's scope misses items earlier steps asked it to carry (B)

S68's section lists the spec, the plain-names table, the run-order test and pairwise tests. Its own list should also carry:
- The financing identity and the `fx` part of finding 1.
- From S59 and S71: the tail's neutrality and `cr`'s weighted totals rechecked at 10,000 adults (`cr` is the one rule that reads a weight).
- From S67: `q` paired with `rt` and `lf`.
- From S62: `po` with `pr`, `rt`, `wt`, `cl`, `bg`.
- From S60: `bg` with ageing.

S70's own parameter list also leaves out S62's and S71's readings and the financing reading; they appear only in those steps' notes. Writing them into S68's and S70's own sections stops a session that reads only its step's section from missing them.

### 6. Clarity: the Nov 9 points are still open (C)

- README.md still opens with "see how it does", calls the model agent-based and says a table sets the Hub's Year 7 targets (poverty under 2%, Gini 0.25-0.30) beside what the model reaches. Research rule 3 says no figure is a target; ledger issue I13 says the same.
- There is still no "start here" page. CHANGELOG.md is 416 KB.
- No step owns these. Suggested: S65 (release 2 and findings page) rewrites the README's first screen in two sentences on what the model finds on both sides, and removes the targets table.

### 7. Housekeeping (C)

- research-update HANDOFF.md lists D21 under "Decisions waiting". It was confirmed on Nov 9 and is archived in the ledger.
- Old session branches in research-update still need deleting (listed in the handoff).

## Status of the Nov 9 findings

| Nov 9 finding | Status now |
|---|---|
| 1. All wealth is cash | Closed by S59 (asset classes, tail, returns), S66 (erosion is 90-96% of the real-wealth gap) and S71 (creditor side). The release design's wealth-poverty effect turns from a harm to a reduction. It still depends on real assets keeping up with 30-45% inflation (half-indexing flips the sign in two environments) and on debt relief. |
| 2. The capacity price rule | Closed by S67: the response speed is not identified; the recommendation is today's rule as the main row. Year-20 wealth readings change sign with the rule; yearly averages do not. |
| 3. Round 2 not in the spec; no independent check | Open: S68, S69. |
| 4. Switches tested alone; state leaks | Open: S68. The `PDS` leak (found again in S60) is listed there. |
| 5. Seed intervals are not the uncertainty | Open: S70, S63. |
| 6. The financed row | Answered by D21, but see finding 1: the row was not what the figures said. |
| 7. Clarity | Not started (finding 6). |
| 8. Process | OSF registration and a fresh-session S13 are in the plan. This audit is again by the same kind of system. |

## Additions to the model, ranked

| # | Addition | Why it ranks here | Data | Size | Where |
|---|---|---|---|---|---|
| 1 | Financing identity for every reading; the flat contribution's gap behind an `fx` part | A published decision (D21) rests on an accounting gap | none | part of a session | S68 (amended) |
| 2 | Government budget line and the financing frontier | The only honest statement of what a financed design costs; the government side of S71 | CBO, Treasury (opened at build) | 1-2 sessions | new S72, before S70 |
| 3 | Participation margin and labour-force transitions | Validation fails; moves inflation and every tax base | CPS matched months or SIPP; Vivalt et al. 2026 | 1-2 sessions | new S73, before S70 |
| 4 | Costs at the within-year price level | Possible bias in favour of the programme in the most robust headline; cheap | none | small | S68 (reporting) |
| 5 | Adults 65 and over | They hold the most nominal savings and fixed incomes; the BU's scope for them | SCF, CPS, SSA | 1-2 sessions | after release 2 |
| 6 | Portfolio shifts and nominal rates at high inflation | The 0.46 pass-through is measured at 0-6% rates; real assets are never sold (S59 limits 3, 5) | World Bank deposit and lending rates for S67's 77 episodes | 1 session | after release 2, or a reading in S70 |
| 7 | Lenders' losses and new lending (bank equity, no new fixed-rate loans) | S71 spreads a loss several times banks' equity over shareholders with no other effect | FDIC, Financial Accounts | 1 session | later |

Not recommended now:
- A payer for bargained raises. Only needed for readings above 0.03, and the evidence's main reading is 0.
- An open economy and exchange rate.
- A firm and goods-market layer (as on Nov 9).
- Tuning the debt reading towards the SCF's 9.3% in debt. It is a check, and S61 left the gap open on purpose.

## What could not be checked

- Finding 1's tables come from the frozen row with the round-2 switches off, at 10-20 seeds. The S54 pilot's own row (its joining reading) was not rerun, though its published effects are close to these (basket poverty −18.5 against −17.5 here, Reference).
- The `hybrid` reading was not run.
- The gap-as-money reading is a temporary patch, not a design. Its wealth figures use all-cash wealth.
- The size of finding 4 is not measured.
- The engine's 9,137 lines were not read in full. The S60 and S62 code was read only where the reports point.
- Sources named for the new steps (CBO, CPS matched months, SIPP, FDIC, SSA) were not opened here. Each build step opens them first (research rule 3).
