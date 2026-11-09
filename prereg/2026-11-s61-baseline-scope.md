# Preregistration: baseline scope, adults outside the labour force and the debt drift (S61)

Committed Nov 9, 2026 by S61, before any run of the rows below and before the switches are built. Engine: compassionism-simulation at commit `7895f27e82030f9b4db0ee01f4995a5aec942f2e` (main); the two switches land on branch `claude/s61-baseline-scope` from it, off by default (guard test identical). The engine commit of the pilot is recorded in Amendment 1 before the pilot runs.

## Why
Every result compares Compassionism with "no programme" on the same simulated people. S34 found two gaps in that yardstick that matter for the round-2 results (review triage `audits/2026-11-s39-s55-review-triage.md`, D1-D2):
1. **Everyone works.** The model's adults are all in the labour force. In the US, 19.4% of adults aged 25-64 did not work at all in 2025; 17.3% gave a reason outside the labour market: illness or disability 5.8%, retirement 4.1%, caring for home or family 6.3%, school 1.1% (CPS ASEC 2026, `sources/lf_scope.py`).
2. **The debt drift.** With no programme, families in debt rise from 15.5% to 33.4% over 20 years (21.4% with US earnings; the SCF 2025: 9.3% for families with a head aged 25-64 and wage income). The cause is the spending rule: a household below its living-wage budget spends `budget × (income/budget)^0.557`, which is more than its income, every year, with no limit but the debt floor (−$10,000), where the rest is written off. S35's debt reading (study F) let the excess be paid only from positive savings, with a borrowing limit of zero; it cut the Year-20 figure to 14.9% but has no borrowing at all, which the reviews rightly call unrealistic.

This study builds both parts behind switches and measures what each does to the yardstick. It is a check of the yardstick and a choice of model, not a test of the programme.

## The criterion, fixed before anything is built or run
The S34 report left two candidate spending rules open. Which reading S61 recommends to S63 for the main row is decided by these rules, in order. The SCF's 9.3% (or any outside figure) is **not** a criterion: no reading is chosen because it lands closer to an outside figure.
- **C1. Admissible.** A spending rule is admissible only if, in every year and every household, spending above the year's cash income is paid from the household's savings at the start of the year (if positive) or from an explicit borrowing limit, and from nothing else (no write-off of ordinary spending at the debt floor). A unit test enforces this. The debt floor still applies to job loss, shocks and every other flow, as now.
- **C2. Sourced.** Every constant is from a cited, opened source or is a labelled design parameter swept over a stated range.
- **C3. Fewest free choices.** Among admissible readings, the recommendation is the one with fewer labelled design parameters; if equal, the one that changes less of the released rule (the graded spending rule kept where income covers spending).
- **C4. Stability of the programme's effects.** If, in the pilot below, the sign or the 95% interval's exclusion of zero of the C2.2 design's effect on basket poverty, wealth poverty or the cost-of-living measure differs between the recommended reading and another admissible reading, S63 must carry both beside the main row and the headline must say the result depends on how households below their budget borrow. C4 never changes the recommendation; it decides what S63 must carry.

Under C1, the released rule and the floor rule on its own are not admissible; each candidate below therefore includes the borrowing limit.

## The two switches (what will be built)
**`DEBT_READ` extended (row option `dr`, built in S35; off = released):**
- `lim`, the borrowing limit for ordinary spending, in year-0 dollars moved with the price level. Main value **$2,500**: the median unsecured consumer debt (credit-card balances after the last payment, other instalment loans and other debt; `CCBAL + OTH_INST + ODEBT`) of families with a head aged 25-64 in the bottom 40% of income who hold any, SCF 2025 (five implicates, `WGT`). Swept: 0 (S35's study F), $5,000 (the median for all holders aged 25-64), $8,700 (the 75th percentile in the bottom 40%), $10,000 (the size of the debt floor). Design parameter: what share of a family's unsecured debt is a limit for ordinary spending.
- `liq`, the share of positive start-of-year net worth that can pay for ordinary spending. Main value 1 (the model has one wealth stock; S35's reading). Reading: 0.046, the SCF 2025 median of liquid assets (`LIQ`) over net worth for families aged 25-64 with positive net worth. Design parameter.
- `fl`, the subsistence floor (new). Off (`'none'`) in the cap reading. In the floor reading (`'fpl'`), the graded rule applies only to spending above the household's official poverty threshold (Census, thresholds for 2025, `CFG.HH_FPL`, as a share of the household's year-0 budget): spending = F + (cost − F) × ((income − F)/(cost − F))^0.557 when income lies between F and the cost, F when income is below F; the borrowing limit then applies as in the cap reading.

So the two candidates are **cap** (`dr: {lim: 2500}`) and **floor** (`dr: {lim: 2500, fl: 'fpl'}`). The floor reading adds one labelled choice (which floor), so under C3 cap is recommended unless the floor reading turns out not to need it (it does: the threshold is sourced, but choosing the poverty line as the floor is a design choice).

**`LF_SCOPE` (new; row option `lf`; off = everyone in the labour force, as released):**
- At the start, each adult is drawn out of the labour force for the whole run with the CPS ASEC 2026 probability for the adult's household type (single, single parent, couple without children, couple with children) and reason (disability, early retirement, care, school); `sources/lf_scope.py`, table `shares`. Where adults have ages (ageing on), the table by age band (25-34, 35-49, 50-61, 62-64; `sharesByAge`) is used, falling back to the type's all-ages row in a cell with fewer than 100 survey records. Own stream (seed + 600071), two draws per adult at the start: the main streams and the eight-draws-per-agent-year guarantee are untouched.
- Their own yearly income: drawn once from the CPS distribution for their reason (`ownIncome`, percentiles 0-100 by 5, linear between): Social Security (including disability insurance), SSI, other disability income, pensions, survivor and veterans' payments, public assistance, unemployment and workers' compensation, educational assistance, child support, help from outside the household, other income. In year-0 dollars, moved with the price level (as Social Security's cost-of-living adjustment moves it). Property income and withdrawals are left out (the model pays those from wealth); SNAP and tax credits come from the engine's safety net, as for everyone.
- They earn no wages, have no job loss, do no paid programme (ESP) work, and are left out of the wage index: the engine's existing rules for a retired adult (`a._ret`), which they reuse. Under the programme they receive the Basic Unit and every price effect, and convert under the row's rule for retirees (as released: they may convert, and give up no wage for project hours). **Claude's reading of the design (modelling assumption):** the Hub papers give the Basic Unit to every adult and say nothing particular about adults outside the labour force; the most cautious reading is to treat them as the engine treats retirees and not to let them gain programme income through work. A `conv: 'none'` reading (no conversion income) is built and reported beside it.
- Status is fixed for the run (no one enters or leaves the labour force): a stated limit. With ageing, status stays until 67, when nothing changes (a disability benefit continues as the retirement benefit does, as Social Security converts it); new adults entering at 25 are drawn with the same table.

## Questions
- **Q1. Debt drift.** How do families in debt (net worth below zero) at Year 0 and Year 20, overall and by household type, change under cap and floor, against the frozen yardstick and against the SCF 2025 figure (as a check)?
- **Q2. Borrowing limit.** How much do Q1's figures move over the `lim` sweep and the `liq` reading?
- **Q3. Labour-force scope.** With `LF_SCOPE` on, how close are the share of adults 25-64 with earnings, official poverty (adults, children, everyone), household money income, median net worth and families in debt to the outside figures in S34's table?
- **Q4. Adults outside the labour force.** Their own official poverty rate, basket poverty, median net worth and share in debt, by reason, Year 0 and Year 20 (no outside comparison except official poverty: CPS ASEC 2026 for the same adults, from the same script).
- **Q5. The programme (mechanism check only).** Does the C2.2 design's effect on the primary outcomes change sign or significance under cap, floor, `LF_SCOPE`, and `LF_SCOPE` with cap (criterion C4)? Pilot seeds only; not a result.

## Design
- **Yardstick (every row):** the frozen engine (`frozenRow`: `au`, `fx`, spending share 0.877), CPS earnings (`lt: {s: 'all', m: 'all'}`), today's safety net (`sn: {abawd: true, slope: true}`), the manifest's common settings (`fin: 'tax'`, NR6 profile, `TB_PROFILE_G`, `REL_V52_STUDY`), octave raise off, no ageing (except rows marked "age").
- **No-programme rows:** F0 the frozen yardstick; DC cap; DF floor; DC0, DC5, DC87, DC10 (cap with `lim` 0, 5,000, 8,700, 10,000); DCL (cap with `liq` 0.046); L lf; LC lf + cap; LF lf + floor; LCn lf (`conv: 'none'`) + cap; F0age, LCage (with ageing).
- **Programme rows (Q5):** the C2.2 design (`c22Design`) on F0, DC, DF, L, LC, each with its own no-programme row above (paired).
- **Environments:** Reference, Adverse, Stress.
- **Seeds 1-100** (a pilot: round 2 runs nothing at 500 seeds before S63's freeze), paired across every row (common random numbers); 500 adults and their children; 20 years.
- **Where:** the session machine (no money spent). Command: `node dev/tools/s61_scope.js ENV 100 20 [--prog]` for ENV in ref, adv, st; outputs in `dev/runs/s61-scope/` (compassionism-simulation) with the command and commit, and in compassionism-sim-results folder `s61-scope-<engine commit, 7 chars>` with run.txt and SHA256SUMS.
- **Outside figures:** S34's table (`dev/reports/baseline-realism.md`), unchanged; for Q4 the CPS ASEC 2026 official poverty of the same adults (added to `sources/lf_scope.py`).

## Outcomes
- **Primary (Q1, Q3):** at Year 0 and Year 20, Reference: families in debt, overall and by the four types; median family net worth; families below $25,000; the share of adults 25-64 with earnings; official poverty of adults, children, everyone; median household money income.
- **Secondary:** Adverse and Stress (all of the above); Q2's sweep; Q4 by reason; the engine's own headline measures (basket poverty `fgt0PY`, wealth poverty `pov`, cost of living `hhCostPY`); for the floor and cap rows, the share of household-years whose spending was cut by the limit, and the mean cut.
- **Q5:** the C2.2 design's paired effect on basket poverty, wealth poverty and the cost-of-living measure (`fgt0PY`, `pov`, `hhCostPY`, points), with the 2.5th-97.5th percentile interval from 2,000 paired bootstrap replicates over seeds.
- Units as S34: 2025 dollars (year-0 dollars, later years deflated by the model's own price level); shares in % of families or adults; means over seeds with the 2.5th-97.5th percentile range over seeds.

## Analysis
- Each comparison: model, outside figure, difference, class, under S34's gap rules unchanged (a gap: a share more than 3 points away; a dollar level outside 0.80-1.25 of the outside figure; a Gini more than 0.03 away).
- No hypothesis tests on Q1-Q4 (a list of gaps). Q5 is a mechanism check at 100 seeds, labelled pilot; no multiple-comparison correction; no claim from it but C4's.

## Decision rules
1. The recommendation to S63 follows criterion C1-C3 above, whatever the pilot shows on the outside figures.
2. C4 decides which readings S63 must carry beside the main row.
3. `LF_SCOPE` is recommended to S63 for the main row if its unit tests pass and the share with earnings moves toward the CPS figure (a mechanism check: the switch does what it says); its effects on every other outcome are reported, not used to decide.
4. A remaining gap is classed as in S34 (scope, constant, open); no constant is changed to close it.
5. If building either switch needs a choice not written here, the choice is a dated amendment below, before the pilot runs.

## Reporting
Every cell is published, matching or not, in compassionism-simulation `dev/reports/s61-baseline-scope.md` (plain words, Claude's reading, sources opened, labelled design parameters with their ranges) and in compassionism-sim-results.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

**Amendment 1, Nov 9, 2026 (after the build, before the pilot; no pilot row had run).** Choices made while building that the text above did not fix (compassionism-simulation `dev/DECISIONS.md`, S61):
1. An adult outside the labour force carries its own income in the engine's wage field from the start (as a retiree's benefit is carried each year), so every Year-0 measure reads it.
2. Where such an adult has no own income, the engine's labour-raise ratio divided 0 by 0; it is set to 1 for these adults only (off: unchanged).
3. Starting wealth is the household's SCF draw, as for every household, not drawn by labour-force status: a stated limit (adults outside the labour force start with the same wealth distribution as workers).
4. The floor rule's threshold is a share of the household's year-0 budget (`CFG.HH_FPL` over the budget at year-0 prices, childcare included), applied to the year's cost.
5. Q4's basket poverty by reason is not in the pilot tool (it needs a per-adult reporting key); the pilot reports official poverty, family net worth and the share in debt by reason, and S63 lists the key.
6. The tally `drHit` (share of graded spending decisions the limit cut) and `drCut` (mean cut, year-0 dollars) are the secondary outcome "share of household-years whose spending was cut"; a decision is a couple's or a single adult's.
7. Before this amendment the tool was smoke-tested at 2 seeds in Reference to check that it runs. Those figures were seen (for example, the cap reading at $2,500 left the share of families in debt almost where the frozen rule has it, while the limit of zero lowered it); nothing in the design, the criterion or the rows was changed after seeing them, and they are not reported.
The pilot engine is the commit recorded in compassionism-simulation `dev/runs/s61-scope/` (each output's `_meta.manifest`).

**Amendment 2, Nov 9, 2026 (after the first pilot run; reason: an input-data error found by checking the engine's table against its source).** The own-income table used percentiles in 5-point steps with linear interpolation, as written above. The pilot's mean own income of adults outside the labour force ($15,202) was well above the survey's ($10,200 for the same mix of reasons), because the top bin interpolates between the 95th percentile and the survey's top-coded maximum: by reason, the 5-point grid overstated the mean by 28% (disability), 43% (retirement), 279% (care) and 10% (school). The table now uses 0.5-point steps (201 points per reason), whose means are within 1-7% of the survey's; a unit test checks the engine's draws against the table's mean. This corrects the input to match its source; nothing was set to reach an outcome. Every pilot row is rerun on the corrected engine and only the rerun is reported; the first run's files are kept in the scratch record only, not published, because they come from an engine whose input table was wrong. The rows without `lf` are unaffected by the change and their figures are expected to be identical in the rerun (a check).
