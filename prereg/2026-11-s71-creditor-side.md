# Preregistration: a creditor side for debt that inflation wipes out (S71: option `cr` of RETURNS)

Committed Nov 13, 2026 by S71, before the option is built, before any coefficient below is computed and before any run. Engine: compassionism-simulation at commit `63cda963860abc34e3ca635bc1deb36fe7b4ca55` (main); the option lands on branch `claude/s71-creditor-side` from it, off by default (guard test identical). The coefficients and the engine commit of the pilot are recorded in Amendment 1 before the pilot runs.

## Why
- With wealth held by asset class (S59), a fixed-rate debt keeps its dollar value while the programme's inflation runs 30-45% a year. The debtor's gain is real. Nobody in the model holds the other side of the debt, so nobody loses it.
- S59 found that about half of the release design's wealth-poverty reduction, and the sign of the programme's effect on the top 1% share of wealth, rest on that gain (main reading against the no-debt-relief reading).
- S59's two readings are bounds. This step builds what lies between: the households that hold the debt, directly or through banks, funds and shares of lenders, lose what the debtors gain, in proportion to their claims.

## What is already on the books (found while reading the engine; not a result of any run)
The engine already pays holders of nominal assets (deposits, bonds, the non-stock part of funds) only 46% of inflation as extra interest (`phi` 0.46, Drechsler, Savov and Schnabl 2017). They lose 54% of inflation on every dollar every year, and no one in the model gains it. Part of those nominal assets are, looking through the banks and funds, the claims on household debt. So part of the creditors' loss is already charged; it is not attributed to anyone. This step attributes it and adds the part that is missing. A claim dollar can lose at most the whole of inflation, so the new charge on a nominal claim is the difference between what it is paid now (`phi` times inflation) and what the debt itself is paid (`chi` times inflation: nothing in the main reading). Charging the full loss on top of the 54% would count it twice.

## Method (Doepke and Schneider, *Journal of Political Economy* 2006, opened before this file)
Their rule: every nominal claim is finally owned by households, the government or foreigners. Funds that only issue shares of themselves (mutual funds, money market funds, defined-contribution pension funds) are looked through to their shareholders. Every other business, banks included, is owned through its shares, and its shareholders carry its net position. Defined-benefit pension assets belong to the sponsor. The government includes the Federal Reserve, state and local governments and government retirement funds. Short claims (deposits) reprice; long fixed claims do not.

This step applies that rule to one ledger only: household fixed-rate debt (home mortgages and non-revolving consumer credit). It does not build the whole net nominal position of every sector (limits, below).

## Sources and rules for the coefficients (fixed now; `sources/s71_creditors.py` computes them; no engine run involved)
1. **Who holds the debt.** Federal Reserve, Financial Accounts of the United States (Z.1), release of Sep 11, 2026, levels at 2022:Q4 (the year of the survey the engine's balance sheets come from): L.218 one-to-four-family residential mortgages less home equity loans, and L.222 consumer credit, by holder. Mortgages held by the government-sponsored enterprises and by agency and GSE-backed pools pass to the holders of agency and GSE-backed securities (L.211) in proportion to holdings. Issuers of asset-backed securities pass to the same holders in the same proportions (the table does not show who holds their bonds). Latest quarter (2026:Q2) computed beside it as a check, not used.
2. **Final holders**, by these rules:
   - *Government:* federal government, state and local governments, the central bank, federal and state and local government pension funds.
   - *Foreigners:* rest of the world; foreign banking offices in the U.S.
   - *Households, bond-like claims:* households and nonprofit organisations directly; mutual funds, hedge funds and private defined-contribution pension funds, by the holders of their shares (L.226); life insurers' share of mutual funds.
   - *Banks and credit unions* (U.S.-chartered depository institutions, credit unions, banks in U.S.-affiliated areas, holding companies): the share of their balance sheet funded by deposits (checkable plus time and savings deposits over total liabilities and equity, L.110) passes to depositors by their shares of those deposits (L.203, L.204; foreigners' currency left out): households (deposit-like claims), government, foreigners, businesses. The rest of the balance sheet is the banks' own (their shareholders').
   - *Money market funds:* deposit-like claims of their shareholders (L.206).
   - *Businesses* (the enterprises' own holdings, finance companies, mortgage trusts, brokers, insurers' general accounts, private defined-benefit pension funds, nonfinancial businesses, and the banks' own part): their shareholders, by the holders of U.S. corporate equities (L.224), looked through funds; shares held by other U.S. businesses are netted out. Households' part is charged on the model's shares class (`eq`); private-business equity is not charged.
   - Revolving consumer credit is floating in the engine. L.222 does not split holders by type of credit; the federal government's holding is all student loans (fixed), and every other holder's revolving part is taken as proportional. Adjustable-rate mortgages are taken as held in the same proportions as fixed-rate ones. Both are modelling assumptions (limits).
3. **Who bears a claim's loss (incidence).** Three readings, the main one fixed now by a rule: the reading that follows the named paper's method with the engine's own constants.
   - `pass` (main): a bond-like claim loses in full. A deposit is paid `phi` of inflation as now; what the depositor does not lose on a deposit-funded loan, the lender's shareholders lose. Businesses' direct holdings are their shareholders' loss.
   - `hold`: holders of record. Deposits that fund the debt lose in full, like bonds; shareholders carry only businesses' direct holdings and the banks' own part.
   - `hedge`: lenders' shareholders are not charged at all (Drechsler, Savov and Schnabl 2021 find banks' equity close to insulated from interest-rate changes because deposits reprice so little); bond-like claims lose in full; the shareholders' part is stated and left outside.
4. **The model's households are not all households.** The engine's families have a head aged 25 to 66 with wage income. Retired households hold claims too and are outside the model. From the Survey of Consumer Finances 2022 (the file of `sources/s59_portfolio.py`): the engine families' share of all families' deposit-like assets (transaction accounts and certificates), bond-like assets (other financial assets less stocks) and stocks, each divided by their share of all families' fixed-rate debt. The model's creditors bear that fraction of the household-held loss on each kind of claim; the rest is a stated outside part ("households outside the model's population").
5. **Within the nominal class.** The engine holds deposits and bonds as one class. The bond-like fraction of nominal assets for each of the engine's seven wealth groups comes from the same survey file and population. The Fed's Distributional Financial Accounts (all U.S. households, five wealth groups) are the outside check: the share of creditor losses borne by the top 1%, the next 9%, the next 40% and the bottom half, computed from the accounts' instrument shares and the coefficients above, is printed beside the model's. Deviation from the step's wording, with the reason: the accounts describe all households in five groups, the engine's groups describe its own families, so the split inside the model comes from the survey the accounts are themselves built on; the accounts check it and are not an input.

No coefficient is tuned. Each is a ratio of published levels under the rules above; `phi` and `chi` are the engine's existing constants.

## The mechanism (option `cr` of `rt`; off = identical)
Each year, before any adult's year, with pi the year's change in the price level, D the fixed-rate debt of adults already in the model, and NB, ND, EQ their bond-like nominal assets, deposit-like nominal assets and shares (last year's saving placed first, weighted as below):
- the debt inflated away is (1 − chi)·pi·D;
- bond-like claims of the model's households are bHH·wB·D dollars (capped at NB). Each bond-like dollar is charged (phi − chi)·pi times claims over NB, so that claim dollars are paid chi·pi like the debt;
- under `hold` deposit-like claims dHH·wD·D are charged the same way on ND;
- shares are charged pi times the shareholders' part (set by the incidence reading) times eH·wE·D, spread over EQ;
- nothing else changes: debtors keep their relief; floating debt, real assets other than shares, and every rule of the programme are untouched. No random draw.

With no inflation every charge is zero. With `chi` equal to `phi` the nominal charge is zero. If claims exceed holdings the excess is not charged and is reported ("unplaced").

**Weights.** With the weighted top tail on, D, NB, ND and EQ are weighted sums, so that the ledger balances in the population the weighted measures describe. This is the first rule that reads a weight; it reads it only through these four totals. Reading `w: 0` uses unweighted sums (no rule reads a weight), reported beside it.

**Scope readings.** Main: the government's, foreigners' and outside households' parts are stated and left outside. `pop: 1`: the model's families are treated as the whole household sector (every factor of item 4 set to 1). `out: 0`: nothing is outside; every dollar of relief is lost by a household in the model in proportion to its claims (the hard upper bound on creditor losses).

**Reporting** (with `cr` only; Year-0 dollars per adult, weighted, summed over the run): debt relief; the part of it already on the books; new charges on nominal assets and on shares; each outside part (government, foreigners, outside households, lenders' shareholders not charged); unplaced; the ledger gap (relief less everything else: zero if the build is right); new charges and relief by fifth of starting wealth; the top 1% of adults' share of new charges.

## Unit tests (written with the build)
1. Off is identical (guard test; and the revaluation function returns the same dollars with `cr` absent).
2. Conservation, the step's test: on a built population with several wealth groups and weights, debt inflated away equals creditors' losses (measured from the balances, plus the part on the books) plus the stated outside parts, to rounding, under each incidence reading, each scope reading and `chi` 0 and 0.5.
3. With no inflation nothing moves.
4. In proportion to claims: twice the bond-like assets, twice the charge; twice the shares, twice the charge.
5. Claims above holdings are capped and the excess reported; the ledger still balances with it.
6. In a full short run the reported ledger gap is zero to rounding.

## Pilot (100 seeds, 500 adults, 20 years; Reference, Adverse, Stress; the release row and the C2.2 design against no programme on the same seeds; the rows of S59 part 2)
| Row | Reading |
|---|---|
| `main` | S59's main reading (owners, capital income, tail), no creditor side: bound 1 |
| `chi1` | the same with fixed-rate debt repricing (no debt relief): bound 2 |
| `cr` | creditor side, main: `pass`, outside parts left outside, weighted totals |
| `crhold`, `crhedge` | the other two incidence readings |
| `crpop` | the model's families as the whole household sector |
| `crall` | nothing outside |
| `cru` | unweighted totals |
| `r2`, `r2cr` | without the tail, without and with the creditor side (does the tail decide anything here?) |

`main` and `chi1` must reproduce S59's per-seed files exactly (the option is off in them): a check.

**Outcomes** (programme minus no programme, paired by seed; mean and the 2.5th-97.5th percentiles of 2,000 paired bootstrap replicates; weighted measures): wealth poverty at year 20; the three parts of real wealth (opening nominal position, opening real assets, saving since); the top 0.1%, 1% and 10% shares and the bottom half's share of wealth; the wealth Gini; median real wealth; basket poverty and yearly inflation (does the creditor side move the rest of the economy?); the ledger. A pilot is a mechanism check at 100 seeds, not a result.

## Decision rules (fixed now)
1. **Checks.** (a) Unit tests and guard test pass. (b) In every pilot row with `cr`, the ledger gap is below one millionth of the relief. (c) Unplaced claims are below 5% of the relief in every environment. If (b) or (c) fails, the creditor side is not recommended as a main-row candidate and S59's two-bound presentation stands.
2. **Direction of the programme's effect on the top 1% share of wealth.** Reported as established for a design only if the effect has the same sign, with a 95% interval excluding zero, in all five creditor readings (`cr`, `crhold`, `crhedge`, `crpop`, `crall`) in all three environments. Otherwise: not established, with the readings that disagree named.
3. **Bounds.** The step expects S59's two readings to bound the creditor readings. Whether each outcome under each creditor reading lies between them is reported row by row; an outcome outside the bounds is reported and explained, not hidden.
4. **How much of the wealth-poverty reduction rests on the free gain.** Reported as the effect under each creditor reading beside both bounds. No threshold; no reading is preferred for its figure.
5. **Recommendation to the design freeze (S63), fixed now, subject to rule 1:** the creditor side under `pass` as a main-row candidate for every wealth and concentration outcome, with `main` (no creditor side) and `chi1` (no debt relief) kept beside it as bounds, and `crhold`, `crhedge` and `crpop` as readings. S63 chooses.
6. No synergy is claimed: these rows are not a factorial design.

## Limits known before the build
- One ledger only. Businesses and the government are net debtors too; in the paper's accounts shareholders gain from inflation on corporate debt, and the government gains on its own debt. Neither is modelled, so the `pass` reading charges shareholders a loss without the offsetting gain: `hedge` and S59's main reading show the other side.
- Depositors' losses on deposits that fund floating loans (a gain to banks) stay unattributed, as before.
- Fixed-rate debt is never repaid or newly issued in the engine, and claims are spread over all holders of a class each year in proportion to holdings (as through a fund), not tracked claim by claim.
- The coefficients are one year's levels (2022); the holders of adjustable-rate and revolving debt are taken as proportional.
- The outside parts are left outside: the government's loss is not passed on to taxpayers, and retired households are not in the model.
- Tested with wealth by asset class only (no ageing, capacity price rule or adults outside the labour force): S68's pairwise tests.

## Amendments

### Amendment 1 (Nov 13, 2026, before the pilot): the coefficients, the build, and four small departures
Engine commit of the pilot: `f7572fd4c3efec2393df779df2d3459269cdb217` (branch `claude/s71-creditor-side`). Guard test identical; engine lineage linked; 7 unit tests (`crUnitSuite`), all passing.

**Coefficients** (`sources/s71_creditors.py`, `sources/s71_creditors.json`; file hashes inside), computed after this file's first commit by the rules above:
- One dollar of household fixed-rate debt, by final holder (2022:Q4): households' deposit-like claims 0.2393; households' bond-like claims 0.0845; businesses (their shareholders) 0.3242; government 0.2556; foreigners 0.0641; government's deposits 0.0182; foreigners' deposits 0.0141. At 2026:Q2 (check, not used): 0.2200, 0.0826, 0.3723, 0.2173, 0.0720, 0.0216, 0.0141.
- Owners of U.S. shares: households 0.7313, government 0.0710, foreigners 0.1977.
- The engine's families hold 79.0% of all families' fixed-rate debt, 51.8% of deposit-like assets, 47.9% of bond-like assets and 49.2% of stocks. Factors: deposits 0.6566, bonds 0.6067, shares 0.6233.
- Bond-like fraction of nominal assets by wealth group (below zero, then up to the 25th, 50th, 75th, 90th, 99th percentile, above): 0.3805, 0.3920, 0.4977, 0.5883, 0.6648, 0.7260, 0.6624; all 0.6753.
- So, per dollar of debt inflated away in the main reading (`phi` 0.46, `chi` 0): 11.3 cents are already on the books of the model's households, 2.4 cents are newly charged on their bond-like assets, 20.5 cents on their shares, and 65.9 cents are outside the model (government 29.7, foreigners 16.1, households outside the model 20.1). These are arithmetic from the coefficients, not results of a run.
- Outside check (Distributional Financial Accounts, all households, 2022:Q4): the top 1% would bear 46-48% of the new charges, the next 9% 38%, the next 40% 13-15%, the bottom half under 1%.

**Departures from the text above, each decided before the pilot:**
1. The year's totals are taken at the first adult's turn in the year, not before the year's loop: a pathway exit pays equity into wealth between the two, which left a ledger gap of 3 parts in a million in the first build (found by unit test 6 on a 2-seed, 6-year run; no pilot row had run).
2. In 338 of 22,975 survey records the stock total counts stock held inside transaction accounts; deposit-like assets are capped at the nominal total there (0.35% of the bond-like total).
3. Money market fund shares held by private pension funds count as households' deposit-like claims; nonprofits' student loans as households' direct claims; holding companies' agency securities as banks'. None was named in the rules; each follows the nearest named rule.
4. Shares are charged at most their own value times inflation (a cap, never reached in the tests), and the "top 1% of adults" for the share of new charges is taken by starting wealth, like the fifths.

**Rows as run:** the ten rows of the table above, in each environment, by `dev/tools/s71_creditors.js`; tables by `dev/tools/s71_table.py` with S59's folder for the equality check (now also on row `r2`).
