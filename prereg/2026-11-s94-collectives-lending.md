# Preregistration: the Creative Collectives' lending to start-ups where banks will not lend, and charters of public operators

Committed Nov 20, 2026 by S94 (part 1), before any build or run. Engine: compassionism-simulation at commit `3835242968d6a11d4d8070c9b2d4a249d5a11649` (main, after the frozen-model wording correction). The switch is built on branch `claude/s94-collectives-lending`. Its commit is recorded in an amendment before the first study run.

Claude's reading of the design: compassionism-simulation `dev/reports/s94-collectives-lending-reading.md`. Values: `sources/s94_lending.py` (all sources opened Nov 20, 2026). Duke's words: ledger step S94, Nov 17 and Nov 19.

## Why
Duke (Nov 17): the Creative Collectives can lend to or support start-ups where banks will not. Duke (Nov 19): small essential providers get help with premises, logistics and set-up costs; large utility and transport projects are financed by municipal bonds and public debt, and public operators could move to Collective charters. The study of output per hour lists this as a limit. The Hub's papers give the Collectives no lending role (reading, section 2), so this models Duke's statement as an addition to the design.

In the main row (open access) the community businesses' (PTF) share of essential sales grows only as far as owned capital allows (capacity c = c0 + reinvestment per adult / K, K = $18,862). A two-seed check of the main row (no outcome read) shows the limit binding in 21-32% of adult-years under Reference and Adverse, and in 100% under Stress in the opt-in design (the share is 12.9% at year 5 and 34.0% at year 19).

## Questions
- Q1. With a Collectives' fund for premises, equipment and set-up costs, how much faster does the PTF share grow, and what does that do to the four primary outcomes against the main row, by environment, design and horizon?
- Q2. What does the fund cost net of repayments and write-offs (per adult a year), and per point of basket poverty reduced?
- Q3. How much do the answers depend on the pace limit, failures, and the mix of loans and grants?
- Q4. Do charters of public utilities (the customers of public operators get the community-business utility price) change any primary outcome, and at what added subsidy?
- Q5. Do the fund and charters interact (their joint effect against the sum of the two)?

## The switch (`cl`, row option; off is the engine as it is)
Acts only in the programme run, and only with open access and growth (`pa: 'open'`). It is refused otherwise, and refused with `PTF_ACCESS` fixed shares. The no-programme run does not read it.

**A. The fund** (`fund`, main true). Each year from year 1, after reinvestment's capacity c_own is known and before any test reads a share:
1. Wanted growth: the room the demand ceiling and the operations limit leave, Δ* = max(0, s_want − c), on the population's share, as the growth rule computes it now.
2. Funded capacity this year: f_t = min(Δ*, pace − (`paceOn` 'total' ? the year's growth of c_own : 0)), floored at 0. Main pace **0.0296** (2.96 points of the sectors' capacity a year: jobs created by new establishments over all jobs, Census BDS 2014-2023, utilities, retail, and accommodation and food services, weighted by BEA 2025 net stock 0.835/0.075/0.089). `paceOn` main 'lent' (the pace limits the fund's additions only).
3. Outlay: f_t × K per adult, in year-0 dollars revalued with the price level. A share `grant` (main **0.1419**, Pennsylvania's Fresh Food Financing Initiative, $12.1m of grants in $85.3m approved) is a grant. The rest is a loan. The whole outlay is programme cost in the year paid. It is counted as matched output, like reinvestment (it buys premises and equipment), and that is stated in the report.
4. Repayment on the outstanding loan balance: each year at depreciation plus real interest (`PROD_CAP_DEP` 4.528% + `PROD_CAP_INT` 3.668%), from the PTFs' premium before the split, as the membership borrowing charge is paid (a shortfall carries). Interest received lowers programme cost. The depreciation part is the loan's replacement capital and keeps the balance constant in real terms (no principal is repaid: the model's perpetual-capital convention for borrowed capacity, stated).
5. Failures: each funded cohort (one per year) loses a share h_k of its remaining capacity in its k-th year. Main `haz` **'young'**: capital-weighted BDS exit rates of young firms' establishments, 2014-2023 (0.2238, 0.1323, 0.1410, 0.1249, 0.1036, then 0.0843 for years 6-10, 0.0674 for 11-15, 0.0583 for 16-20, 0.0504 for 21-25, 0.0440 after; 45.4% survive five years). Lost capacity leaves c, and its unpaid loan balance is written off (programme cost; no recovery, the cautious reading). Where c falls below the population's share, every zone's share is scaled down in proportion (the one place the share can fall). No random draw: hazards act on capacity shares deterministically.
6. Capacity for sales: c = min(1, c_own + Σ cohorts' remaining funded capacity).

**B. Charters** (`ch`, main **0**: off in the fund rows). The utility part of each adult's PTF price cut reads the share max(s_zone, ch) instead of s_zone. The food part is unchanged. Chartered capacity needs no capital (the operator's own, financed by its existing bonds), and its running-cost gap is paid by the Source as under `po` (utilities' full cost 0.814). The density tests read s, not the chartered share. Charter readings: ch 1/7 (**0.1429**, public power's share of electricity customers, APPA), and 1/3 and 2/3 (design parameters, swept).

Reported keys (programme run): `clOut` (outlay per adult a year, year-0 $), `clGrant`, `clInt` (interest received), `clOff` (write-offs), `clNet` (outlay + write-offs − interest), `clCap` (funded capacity share at years 5, 10, 19, 39), `clFail` (capacity lost, cumulative), `clBind` (share of adult-years where the pace limit bound), `chSub` (added subsidy from charters).

## Design
Every row is the main row as the output-per-hour study's job builds it (`s85.js` block A's `off` rows: `r2MainRow` with `sp.vAt: 'sale'`, which that study's check 1 ties to `s90-sale-*-b8ccd8d`), with `o.sec` on so savings is read, in two designs: full coverage and opt-in. One shared no-programme run per environment and horizon (the switch does not act in it; check 2).

| Block | Rows (each in both designs) | Count |
|---|---|---|
| M. Main row | `cl` absent | 1 |
| A. The fund | main; pace × 0.5; pace × 2; no pace limit; `paceOn` 'total'; `haz` 'mature' (0.0440 every year); `haz` none; `grant` 0 (all loans); `grant` 1 (all grants) | 9 |
| B. Charters | ch ∈ {1/7, 1/3, 2/3}, no fund | 3 |
| C. Together | fund main + ch 1/7 | 1 |
| D. Check | `cl` {fund false, ch 0} (must equal M in every key) | 1 |

15 rows × 2 designs + 1 no-programme run = **31 rows** per environment and horizon. Environments Reference, Adverse, Stress; horizons 20 years (primary) and 40; seeds 1-500, paired; 500 adults. Six results folders `s94-<env>-<years>-<engine 7>` in compassionism-sim-results, run on GitHub Actions in 20 pieces of 25 seeds (free; the money rule is not reached).

## Outcomes
**Primary** (as in the output-per-hour study): 1. basket poverty (`fgt0PY`); 2. wealth poverty, yearly average (`ppovA`) and last year (`pov`); 3. median real wealth, weighted (`wtMedE`) and unweighted (`medWealthReal`); 4. savings (`secM3A`, the share of adult-years whose liquid savings cover under three months of need).

**The contrast** for blocks A-C: row − M, paired by seed, per design (equivalently, the change in the programme's effect, since the no-programme run is shared). Also each row's programme effect against the no-programme run.

**Secondary:** the PTF share and capacity paths (`paS*`, `paC*`, `paCap`, `clCap`); the fund's keys above; programme cost (`cost`) and the subsidy (`poSub`, `chSub`); programme inflation (`endoAnn`) and the price level at the last year; below 30 days of basic living (`bNAPy`); poverty severity (`fgt2PY`); outcomes by fifth of starting wealth; Q2's cost per point (net cost change over basket-poverty change, reported only where the poverty change's interval excludes zero).

Every gain is confirmed on basket poverty and wealth poverty, not on severity alone.

## Analysis
- Paired differences over seeds, 95% paired-bootstrap intervals (10,000 replicates, seeds resampled).
- Holm across the six primary measures within each block row, environment, horizon and design for any statement that a row "changes" an outcome. Unadjusted intervals are published beside them.
- Q5: interaction = (C − M) − (A main − M) − (B 1/7 − M), with its interval. Claimed only where the interval excludes zero (research rule 4).

## Checks (before any table is read; each must pass)
1. Off = identical: the guard test (release panels, seeds 1-20, three environments); full-output diffs with `cl` absent.
2. On at zero = identical: row D equals M in every key; the no-programme run is identical with and without `cl` in the programme row.
3. Pace: f_t ≤ pace (or pace − the growth of c_own under 'total') in every year, within 1e-12; f_t = 0 where capacity does not bind.
4. Fund accounts: every year, Σ outlays − Σ write-offs = outstanding funded capital × K (year-0 $) within 1e-9 relative; interest = (DEP + INT) × loan balance; write-offs equal lost capacity × K × the loan share.
5. Failures: with `haz` 'young', the share of a cohort surviving five years equals 0.454 within 1e-3 (unit test on one cohort).
6. Charters: with ch 0 the cut is identical to M; with ch 1/7 and every zone's s ≥ 1/7 the cut is identical to M.
7. The money accounts (MODEL_SPEC 11) close with `cl` on.
8. Eight draws per adult-year, unchanged; the switch draws nothing.
9. Results files match their checksums; the pieces cover seeds 1-500 once on the pinned engine with a clean checkout; the release start's baseline check passes in the job.

Unit tests for 3-6 in the engine (`clUnitSuite`), with `node harness.js unit --write-counts`.

## Decision rules (fixed now)
1. **A failed check:** the defect is fixed and the whole batch rerun on the new commit. Only the rerun is reported.
2. **Effect categories** per primary measure, row, environment, horizon and design (after Holm): *improves*, *no change* (interval includes zero), *worsens*. The report names every *worsens* cell beside any favourable statement.
3. **The fund's verdict** (the main fund row, A main): "the fund helps" where it improves at least one of basket poverty or wealth poverty (yearly) and worsens none of the six, in that environment and design. A null in Reference and Adverse is reported as a null, not hidden by the Stress result.
4. **Robustness:** a headline about the fund needs the same direction in the `haz` 'mature' and pace × 0.5 rows. Otherwise it is reported as depending on that reading, and the reading is named.
5. **Charters:** reported as their own result. No headline joins them to the fund unless Q5's interaction interval excludes zero.
6. **Into the main row:** if rule 3 holds in at least one environment and design, and rule 4 holds, the fund at its main reading is proposed for the release's main row as Duke's design statement. The decision is Duke's (ledger decision; default: the fund joins the main row at the release, with charters off). If rule 3 holds nowhere, the fund is reported as a reading beside the main row, and the main row is unchanged.
7. **No tuning:** nothing is changed to reach a figure. The values above come from opened sources, or are labelled design parameters and swept. A change after the dry run is a dated amendment with its reason and a full rerun.

## Reporting
Every cell above is published, null and unfavourable results included, in compassionism-sim-results and in a plain-words report (`dev/reports/s94-collectives-lending.md`), with the findings-page text if rule 6 applies. Duke's words are attributed to him and kept apart from the results.

## Limits stated in advance
- The model has no private firms, so lending to private start-ups that are not community businesses cannot be represented. The fund finances community-business capacity only.
- Transport, health care and child care have no community-business price in the model. Charters of roads, transit, airports and ports change nothing in it.
- Capacity is for the whole population, not by zone (as for reinvestment).
- The pace limit is a whole-economy rate of new establishments, generous to one network. Acquisitions of existing stores are not separated from new building.
- No concessional rate and no recovery on failures: no source opened.
- One utility share stands for electricity, gas and water (EPA gives no ownership share for water).
- Outlays are counted as matched output, like reinvestment. Under the supply limit (`sl`) they would compete for real resources; the supply-limit interaction is not in this design.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (Nov 20, 2026): the outside readings of the preregistration, before any build
Two readings by other makers' models, of the reading, sources and this file: Nemotron 3 Ultra (OpenRouter, free) and Mistral Large 4 (NVIDIA). Replies word for word in `audits/2026-11-20-pre-release/` (`nemotron-prereg`, `mistral-prereg`); triage in `audits/2026-11-20-pre-release-triage.md`. Nothing has been built or run. Changes:

1. **The pace limits the fund against all new capacity** (Nemotron 1, 3, 5). The rate of new establishments counts every new store and plant in the sectors, so the cautious reading counts reinvestment's growth against it: `paceOn` main **'total'**, f_t = min(Δ*, max(0, pace − (c_own,t − c_own,t−1))). 'lent' becomes the other reading in block A (it replaces the 'total' row).
2. **Charters act on electricity only** (Nemotron 1). Public power's share is for electricity customers; no ownership share was opened for gas or water. The utility part of the cut reads max(s_zone, ch) on electricity's share of household utilities (**0.5535**, BEA NIPA Table 2.4.5U, 2025: $269,938m of $487,685m, the engine's utility total), and s_zone on the rest. The 1/3 and 2/3 rows read the same way.
3. **The charter subsidy, stated exactly** (Nemotron 3 misread it, so the text was unclear). The community-business utility price is 1/1.80 = 0.556 of the market price (the BLEI paper's ε). Its full running cost under `po` is 0.814 of the market price. For chartered customers, as for any community-business customer, the Source pays cost − price = 0.258 of the market price on the chartered part. `chSub` is that amount on the customers who would not be at a community-business price without the charter. Public power's observed 0.839 is the `po` 'sector' reading's cost and is not used here.
4. **No double count of write-offs** (found by Nemotron's check on the identity). The outlay is programme cost in the year lent, so a write-off is not a second cost. It ends the loan's interest and removes its capacity. `clOff` is reported as information. `clNet` = outlay − interest received. Check 4 becomes: Σ outlays = (outstanding funded capacity + capacity lost) × K (year-0 $) within 1e-9 relative; interest = INT × outstanding loan balance; the depreciation part buys the funded capacity's replacement and is not income to the fund.
5. **Outlays are not matched output** (Nemotron 1). The fund's money is new programme money. Counting it as output it buys would credit the programme with output no source shows is new. Main: unmatched, like the rest of the payout, which the main row's full backing (`a` 1) then matches as it matches every programme dollar. Below full backing it is unmatched. The 'matched' reading is not run.
6. **The perpetual-loan convention, stated** (Nemotron 3). The loan's principal is never repaid. The depreciation part keeps the funded capital in repair, and interest is the only transfer back. In effect, the fund owns a stake in the network, as the model already treats borrowed membership capacity. A loan that amortises is not modelled (a limit).
7. **Added checks** (Nemotron 4). 3b: non-vacuity, in Stress, opt-in design, seed 1: funded capacity is above 0 in year 1 and the pace binds in at least one year. 6b: `chSub` equals a hand calculation for one adult in one year. 4b: `clGrant` + loan principal = `clOut` each year.
8. **Robustness rule 4 reads the stricter side only** (Nemotron 4). "Mature" failures give a larger effect, so it is not a robustness test. Rule 4 becomes: a headline about the fund needs the same direction in the pace × 0.5 row and the all-grants row (nothing repaid).
9. **Not changed:** the young-firm hazard stays main. It is the cautious side for both cost and effect (Nemotron called the mature rate cautious, but fewer failures give more capacity and a larger effect). The rate stays the model's corporate rate (a higher rate returns more to the programme and charges the network more, so no direction is clearly cautious). The all-grants row stays as the bound with nothing repaid. Pace × 2 and no pace limit stay as labelled sensitivities. The money-rule check is not added, because the money rule is the project's rule on paid computing, not a model quantity.
10. **What the model cannot represent of the request** (Nemotron 6), stated in the reading and the report. Duke's Nov 17 note covers start-ups in general, including private ones; the model has no private firms, so only community-business capacity is funded. Transport charters change nothing (no community-business price). Collectives issuing or managing bonds is not modelled.

Block A is now: main ('total'); pace × 0.5; pace × 2; no pace limit; `paceOn` 'lent'; `haz` 'mature'; `haz` none; `grant` 0; `grant` 1. Still 9 rows; 31 in all.
