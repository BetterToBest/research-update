# Preregistration: a government budget line, three ways of meeting a deficit, and the financing frontier (S72)

Committed Nov 14, 2026 by S72, before the engine change and before any run. Engine: compassionism-simulation at commit `f910774` (main, S68 part 2 merged). The changes land on branch `claude/s72-government-budget`, off by default (guard test identical). The engine commit of the pilot is recorded in an amendment before the pilot runs.

## Why
The Nov 13 audit (`audits/2026-11-13-simulation-audit.md`, findings 1 and 2) found that the engine has no government account. A deficit, interest on borrowing, the cost of today's safety net under the programme's prices, the government's loss as a lender when household debt is inflated away (S71), and the erosion of the government's own debt at the programme's inflation all go nowhere. S68 part 1 measured the two ends for the C2.2 design paid for by a flat contribution on wages (ledger D21): 38-51% of its cost unpaid, or, with that part as new money, 21-33% inflation a year. This step builds the account, a third and fourth answer to "who pays the part the contribution does not raise" (borrowing, and a higher rate cap), and the frontier between contribution and deficit, so the financed row can be read as a curve rather than one point (D23).

## What the engine does today (read before this file; not a result of any run)
- `tbRunCore` (`index.html`), each year: `need` is what the contribution is meant to pay; `C.tax` is what the flat contribution raised at the rate set from last year (`min(tauMax, need/base)`, base = each adult's wages above `X`); `finStep` (S68) books the payout, taxes, new money, matched output and the unpaid part (`need − tax` where positive) and, with `fx.fin 'money'`, makes the unpaid part new money. `fx.fin 'debt'` is refused ("built in S72").
- Today's safety net (`sn`, session 2b) is paid outside the programme's cost ("by the basket's taxes"); its dollars per adult-year in year-0 terms are reported as `snAll` (SNAP, EITC, CTC).
- The creditor side (S71, `rt.cr`) reports the part of household debt relief that falls on the government as a lender (`crOutG`, year-0 dollars per adult, summed over the run).
- No interest rate other than the savers' fixed real rate (0.97%, FRED DFII10 mean 2003-2025, `sources/tips_real_rate.py`) and the deposit pass-through (0.46).

## Sources opened (Nov 14, 2026; `sources/s72_government.py` downloads and prints them)
- Debt held by the public, Sept 30, 2025: $30,277.8 billion (Treasury, Monthly Statement of the Public Debt, table 1, fiscaldata.treasury.gov). Of it: bills 21.1%, notes 50.8%, bonds 17.0%, TIPS 6.9%, floating-rate notes 2.3%, non-marketable 1.9%. Fixed-coupon share that inflation erodes until it matures (notes, bonds, non-marketable): 69.7%.
- GDP, fiscal year 2025: $30,322.8 billion (FRED FYGDP). Federal interest outlays FY2025: $1,215.6 billion (FRED FYOINT; context only).
- Adults (18 and over), July 1, 2024: 266,978,268 (Census Bureau, Vintage 2024 national estimates, nc-est2024-agesex-res.csv).
- Per adult in year-0 (2025) dollars: today's debt held by the public $113,410; GDP $113,579 (a debt ratio of 99.9%).
- The government's real borrowing rate: the 10-year TIPS yield, the engine's existing sourced real rate (mean 0.97% 2003-2025; 2025 alone 1.96%).
- Policy-rate rule: Taylor (1993), as the Federal Reserve's page "Policy Rules and How Policymakers Use Them" writes it: R = r_LR + π + 0.5(π − π*) + 0.5(y − y_P), π* = 2%.
- Debt and interest rates: Laubach (2003, Federal Reserve FEDS 2003-12, "New Evidence on the Interest Rate Effects of Budget Deficits and Debt"): about 4 basis points per percentage point of projected debt to GDP (regressions); 2.1 basis points in his model-based estimate, which he calls conservative.
- Not opened (CBO's site refused the session's requests): CBO's projections. No figure here depends on them.

## What is built (row option `gv`; switch `GOV`; off = identical)
1. **The government account (reporting).** For every row with `gv` set, each year in that year's dollars, deflated to year-0 dollars per adult-year: the payout the government finances (`need`, the part a contribution is meant to pay; under the Source the Source's own payout is new money and backed output as today, reported as `finMoney`), the contribution raised, interest paid on programme debt, the deficit (payout + interest − contribution), and how it is met: new money, borrowing, or unpaid; the stock of programme debt; today's safety net (`snAll`, its change against the no-programme run computed in the tables); the erosion of today's debt (below). An identity (`ACCT` id `gov`): payout + interest − contribution = new money + borrowing + unpaid − surplus, and the debt stock moves by the year's borrowing at its rate. `gv: {}` changes no existing key.
2. **Erosion of today's debt (reporting).** Today's debt per adult ($113,410), of which the fixed-coupon share (69.7%) loses real value at each year's inflation: `E_t = Dfix × π_t/(1 + π_t)`, `Dfix` then falling by the same factor. Two readings: no repricing (an upper bound, `gvEr`), and the fixed-coupon stock repricing at 1/6 a year (`gvErM`; 6 years is a design parameter close to the average maturity of marketable debt, which was not opened). Read against the no-programme run's own erosion (2% outside inflation in Adverse and Stress).
3. **Who pays the part the contribution does not raise (`fx.fin`):**
   - `'money'` (S68): new money, unchanged.
   - `'debt'` (new): borrowed. No new money for it; the stock carries interest. Two rate readings (`gv.r`):
     - `'fixed'` (main): a real rate `gv.rr` = 0.0097 (readings 0 and 0.0196), so the debt keeps its real value and pays the real rate (as an inflation-indexed bond). Plus a debt premium `gv.dk` × (programme debt / GDP per adult): main 0.04 (Laubach's 4 basis points per point), readings 0.021 and 0.
     - `'rule'` (item 5, D24): the nominal rate the year pays is set from last year: `max(0, r* + π + a(π − 2%) + b × gap)` with Taylor's a = 0.5, b = 0.5, r* = 0.0097 (the same real rate, so the two readings agree at zero inflation and no gap); swept: a 0.25 and 1.0; b 0 and 1.0; r* 0 and 0.02. The gap is the environment's recession income cut (log of the year's income multiplier; 0 in calm years). Claude's reading (modelling assumption): a fall in hours chosen in response to the programme lowers potential output with output, so it is not a gap. The debt premium is added as in `'fixed'`. This year's inflation, unexpected when the rate was set, erodes the debt.
     - Interest is paid from the account (`gv.ip 'tax'`, main): next year's contribution targets the payout's share plus this year's interest, up to the cap; what it cannot raise is borrowed. Reading `gv.ip 'borrow'`: interest is added to the debt. Interest goes to bondholders outside the modelled households' incomes (a cautious modelling assumption: no adult's income rises by it).
   - `'cap'` (new): the rate cap is raised to `gv.capHi` (design parameter, main 0.99, reading 0.95); what the higher cap still cannot raise is new money (as for the progressive and land-value taxes). Printed with years at the cap.
4. **The frontier's settings (on the flat contribution, `o.fin 'tax'`).**
   - `gv.sh`, the share of the payout the contribution is set to raise (0, 0.25, 0.5, 0.75, 1): the rate is `min(cap, sh × need/base)`; the rest is the deficit, met by `fx.fin`.
   - `gv.base`: `'w'` wages (today); `'wc'` wages plus conversion proceeds; `'all'` all money income (the engine's money income measure `tbCashIncome`: wages, conversion proceeds, Social Security, the programme's cash, capital income where `rt.ci` is on; not the safety net, as the official measure). The parts other than wages are charged on last year's amounts, unindexed (as a tax return is filed after the year; so inflation lowers their real yield, the Olivera-Tanzi effect, which is kept). They enter the labour response as an income effect only (one income effect per unconditional dollar, guardrail 7); wages keep the one wage elasticity.
   - The cap: `o.tauMax` 0.5, 0.7, 0.9.
5. **The candidate main row.** `gv: {}` and `fx.fin 'report'` added to `R2_MAIN` (no figure moves under the Source); `R2_ALT` gains `'gv'`: the C2.2 design's flat contribution with its unpaid part borrowed (`fx.fin 'debt'`, programme run). `node dev/tools/s68_pairs.js ENV 5` is rerun, three environments.

## Unit tests (written with the build)
- Off identical: guard test; `gv: {}` identical to off in every existing key (release and C2.2 rows, Source and flat contribution); `gv: {sh: 1, base: 'w'}` identical to `gv: {}`.
- The `gov` identity holds on every reading (`report`, `money`, `debt` fixed and rule, `cap`), both designs, 2 seeds, Reference.
- `'debt'` makes no new money for the unpaid part: `finGapM` 0, and new money equals the `'report'` row's in year 0.
- With `gv.rr` 0, `gv.dk` 0 and `gv.ip 'borrow'`, the year-20 debt equals the sum of the yearly deficits in year-0 dollars.
- `gv.sh` 0: the contribution raises nothing; the deficit equals the payout.
- `'cap'` with `capHi` equal to `tauMax` equals `'money'`.
- `gv.base 'wc'` and `'all'` raise at least as much as `'w'` at the same rate in year 1 and nothing extra in year 0.
- `ACCT`, eight draws per adult-year, no non-finite output: through `r2PairCheck` with the new `R2_ALT` entry.

## Pilot (100 seeds; session machine, free)
Seeds 1-100, 500 adults, 20 years, Reference, Adverse and Stress, the candidate main row (`r2MainRow`, `r2MainStudy`) in both runs; both designs (the release design and C2.2):
- (A) The account and the readings: no programme; the Source (main); the flat contribution on wages, cap 0.9, share 1 with `fx.fin` `'money'`, `'debt'` fixed, `'debt'` rule, `'cap'`.
- (B) Readings, the C2.2 flat contribution with `'debt'`: rule a 0.25, 1.0; b 0, 1.0; r* 0, 0.02; `rr` 0, 0.0196; `dk` 0, 0.021; `ip 'borrow'`; `'cap'` with `capHi` 0.95.
Outcomes: programme inflation (`endoAnn`); the mean contribution rate (`tauMean`) and years at the cap; the deficit, new money, borrowing and interest per adult-year; programme debt at year 20 as % of GDP per adult; the mean nominal and real rate; today's safety net and its change; the erosion of today's debt (both readings) and its change; the government's creditor loss (`crOutG`); basket poverty (`fgt0PY`) and wealth poverty (`pov` at year 20, and its yearly average from the path keys); hours (`hrs`). Paired differences against the no-programme run with 95% intervals (paired t over seeds).
Command: `node dev/tools/s72_pilot.js ENV 100`; tables `node dev/tools/s72_table.js`.

## The frontier (20 seeds; session machine, free)
Seeds 1-20, the same rows and environments. Both designs × share (0, 0.25, 0.5, 0.75, 1) × base (`w`, `wc`, `all`) × cap (0.5, 0.7, 0.9), the share-0 cell once per design (base and cap do nothing there): 37 cells per design, each under `fx.fin 'money'` and `'debt'` (fixed, main values). D21's row is the cell (1, `w`, 0.9). Outcomes as the pilot.
Command: `node dev/tools/s72_frontier.js ENV 20`; tables `node dev/tools/s72_table.js`.

## Decision rules (fixed now)
- (A) For each design, environment, base and cap, the note states the lowest share on the grid at which programme inflation under `'money'` is under 5% a year with its 95% upper bound under 5%, or that no cell on the grid does. The answer for the design as a whole is the lowest share that passes in all three environments.
- (B) S63's choice between `'money'` and `'debt'` for any financed row (S68's rule) is informed by: Claude recommends `'debt'` as the main reading only if, in every environment, programme debt at year 20 is under 30% of GDP per adult and fell or held over years 16-20; otherwise `'money'` is the main reading and `'debt'` is printed beside it with its debt ratio and interest bill.
- (C) If the rule reading's year-20 debt differs from the fixed reading's by more than 10% in any environment, both go to S70's screen; otherwise the note says the rule changes little and why.
- (D) The Source rows: `gv` moves no figure (unit test); their account is reported as it is.
- (E) The bases: the note states, for each design, whether `'wc'` or `'all'` lowers the share found in (A) by at least one grid step.
- Every outcome above is published (compassionism-sim-results and the report), whatever its direction.

## Limits stated in advance
- Contribution rates of 50-99% of a base are far outside the changes the labour response's elasticity (Chetty's 0.33) was measured on; avoidance and informal work are not modelled.
- Laubach's estimate is for changes around US debt ratios of 30-60%; programme debt several times GDP is far outside it. Lenders' willingness to hold such debt at any rate is not modelled.
- The model has no GDP: debt ratios use the US GDP per adult of fiscal 2025, held fixed in real terms.
- Interest paid to bondholders does not reach any modelled household's income.
- Hours depend on population size in the frozen engine (C2.2: +11% at 500 adults, +1.8% at 10,000; S68 part 2); every flat-contribution figure here carries that.
- The rule's gap reads only the environment's recessions; there is no central bank layer (S74).

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

## Amendment 1 (Nov 14, 2026, before the pilot)
- Engine for the pilot and the frontier: compassionism-simulation `df9cfbe` (branch `claude/s72-government-budget`; guard test identical, validate passed, the 9 new unit tests pass). Commands as above; results in compassionism-sim-results `s72-government-df9cfbe`.
- **Found while building (a debugging run of the contribution base's parts; no outcome read): the weighted tail and the contribution's books.** With the weighted top tail on (`wt`, part of the candidate main row), the engine's books count every adult as one person (S59: "weights enter measures only"). The tail's 18 adults stand for very few people but, counted as one each, carried about a third of the unweighted wage base in the C2.2 flat-contribution row (mean wage $88,000 unweighted, $61,500 weighted) and almost all of its capital income ($1.58 million of $1.58 million per adult unweighted; $10,800 weighted). So the contribution's base, and so its rate, misstate the population whenever the tail is on. Added `gv.wb` (on by default with `gv`): the contribution's base and what it raised count each adult at its weight. Without the tail every weight is 1 and nothing moves (unit test); with it, `gv: {}` in the candidate main row moves the Source rows' small contribution. The pilot adds, for each design, the Source row with `gv: {wb: false}`, to report the size of this change. The payout, prices and every decision stay unweighted (S59's rule), a stated limit.
- A numerical guard: the debt reading's rate is held at 100% a year at most (key `gvGuard` counts the years). Without it the premium, compounding on debt many times GDP, overflows to infinity in some seeds. It is reached only where the debt has already exploded; it is not a reading.
- Added keys: `gvY100` (the first year programme debt passed 100% of GDP per adult; 21 = never) and `gvGuard`. Debt and interest are summarised by medians over seeds as well as means, because in some readings they explode.
- Added outcomes beside the preregistered ones: the weighted basket poverty and wealth poverty at the last year (`wtF0E`, `wtPovE`). With the tail on, S59 says the weighted measures are the ones to read; the unweighted `fgt0PY` and `pov` stay the preregistered outcomes.
- Unit test changed from the list above: "`gv: {sh: 1, base: 'w'}` identical to `gv: {}`" is run as `gv: {sh: 1, base: 'w'}` identical to off, on the frozen rows (no tail); and "with the tail, `gv: {wb: false}` identical to off".

## Amendment 2 (Nov 14, 2026, after the frontier ran; a check added, nothing above changed)
- **Found after the frontier ran (reading its tables):** under the base "all money income", hours rise by 60-160% against no programme. A two-seed check (C2.2, share 1, cap 0.9) traced it to the weighted tail: its 18 adults, counted as ordinary adults in every decision and in the price module (S59's rule), have very large capital incomes; the contribution on them is a large income effect, so their hours and wages rise many times over, and those wages enter the price module's income unweighted, which lowers measured inflation (4.6% a year with the tail, 7.5% without; hours +143% with the tail, +21% without). On the wages base the tail changes nothing material (hours −8.0% and −8.3%, inflation 34.2% and 34.4%).
- **Check added:** the whole frontier is run again with the weighted tail off in both runs (everything else as the candidate main row), `node dev/tools/s72_frontier.js ENV 20 DIR --nowt` (compassionism-simulation `c5db934`, engine unchanged from `df9cfbe`). Both runs are published. Decision rule (A) is stated on both; where they differ, the note relies on the run without the tail for the bases "wages plus conversion" and "all money income" and says so, because the tail's distortion there is a property of the engine's unweighted behaviour, not of the contribution.
