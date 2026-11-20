You are an independent reviewer of a preregistration for an agent-based economic simulation (the Compassionism Simulation: a guaranteed-income
programme paid in an expiring currency, with community-owned not-for-profit essential businesses, PTFs). You are a different maker's model from the
one that wrote it. Read the design reading, the sources script and the preregistration below, then answer, numbered:
1. Choices that favour the programme without a source, or that are not the cautious reading where the text is silent. Say which reading would be cautious.
2. Values: is each constant correctly derived from the cited source as described (check the arithmetic shown)? Anything mis-sourced or misapplied?
3. Mechanism: anything incoherent in the fund, the pace limit, the failures, the repayment convention, or the charters (accounting, double counting, a share that cannot fall, effects in the no-programme run)?
4. Checks and decision rules: what is missing to catch a defect, or to stop a favourable reading being over-claimed?
5. Missing rows or readings you would add before any run, and rows you would drop.
6. Anything in the author's request (quoted) the design misreads.
Be concrete and short; cite the section you mean. Do not praise. Plain text.

=== Claude's reading of the design (dev/reports/s94-collectives-lending-reading.md) ===
# The Creative Collectives' lending to start-ups: Claude's reading of the design

Nov 20, 2026. A reading and a plan, written before any build or run. Nothing here is a result. The study's preregistration is research-update `prereg/2026-11-s94-collectives-lending.md`; the figures below come from `sources/s94_lending.py`.

## What the author asked, in his words
On Nov 17 the author said the Creative Collectives can lend to, or support, start-ups that banks will not lend to. On Nov 19 he added: "For small businesses that provide essentials, the program could support in ways such as the physical location, logistics, and setup costs that a normal grocer or restaurant owner would normally have to take on. For large projects such as utility and transportation efforts, this is much different [...] these large sums of money are usually handled by municipal bonds, and government debt. Many of these organizations are currently public operated such as the road and highway systems, airports, train infrastructure, shipping/boat ports, and public utility systems - so that could be an easy transition to Creative Collective charters."

## What the Hub's papers say
- The papers describe Creative Collectives as chartered, opt-in groups of at least 50 members that run the review of conversion rates, pool resources (the glossary's example is a musicians' collective sharing recording facilities) and may be "industry-specific, regional, local, age-based, or thematic". No paper gives them a lending role, a fund, or loan terms.
- The community businesses that sell essentials (grocers, counter-service restaurants, utilities) are the Public Trust Foundations. Their capital comes from the reinvestment account of the essential-service split. The housing papers propose bond finance for housing (tax-exempt municipal "Social Housing Bonds"), not for essential businesses.
- The community development paper contrasts the programme with microfinance, which "relies on debt relationships".

So the author's note adds something the papers do not have. In the model it is an addition to the design, recorded as his statement, not a reading of existing text.

## Where it acts in the model
The model already has a precise place where lending matters. Under open access (the main row), the share of a zone's essential sales that the community businesses can serve grows each year only as far as the capital they own allows: $18,862 of capital per adult serves a whole population's food and utilities (BEA net stock). In a short check of the main row (two seeds, no outcome read), that capital limit:
- holds back growth in about a quarter of adult-years in Reference and Adverse, until the share reaches the 49% demand ceiling around years 6 to 10;
- binds in every year of the 20 under Stress in the opt-in design, where the share is 13% at year 5 and 34% at year 19.

Money for premises, equipment and set-up costs, beyond what reinvestment has paid for, is exactly what that limit lacks. The membership side already has a borrowing rule: capacity is borrowed at a real corporate rate, and lenders are not modelled. The sales side has none, because borrowing on that rule would move the share from 18% to the ceiling in one year, which no retail network does.

## Claude's reading of the design (modelling assumptions where the text is silent)
1. **Small essential providers: a Collectives' fund.** Each year the fund pays for new capacity that zones want and owned capital cannot supply. The mix follows the closest real programme found: Pennsylvania's Fresh Food Financing Initiative (2004-2010) financed "predevelopment, acquisition, equipment and construction costs, as well as start-up costs such as employee recruitment and training" for grocers "where infrastructure costs and credit needs were not met by conventional financial institutions": $73.2 million in loans and $12.1 million in grants, so 14% grants.
2. **Who pays.** The fund's money is programme money, counted in programme cost in the year it is lent. Repayments come back from the community businesses' premium before the split, at the model's existing charge on borrowed capacity (depreciation 4.53% plus a real corporate rate of 3.67%), and they lower programme cost. The fund is not given a cheaper rate than the model's other borrowing: no source sizes a concessional rate (the cautious reading).
3. **How fast.** New capacity paid for by the fund can be added at most at the pace at which new establishments add capacity in these sectors: 2.96 points of the sector a year (Census Business Dynamics Statistics, 2014-2023: jobs created by new establishments over all jobs, weighted by each sector's capital). That figure measures how fast the whole economy opens new stores and plants, so it is generous to a single network. Half and double are run, with no limit as a sensitivity. A stricter reading counts reinvestment-built capacity against the same pace.
4. **Failures.** New businesses close. The main reading applies the exit rates of young firms' establishments in these sectors (BDS, capital-weighted): 22% in the first year, then 13%, 14%, 12% and 10%, falling to 4% after 25 years. That means 45% survive five years; BLS's survival tables give 49-52% for older cohorts. When a funded unit closes, its capacity is lost and its unpaid balance is written off as programme cost. Where capacity falls below a zone's share, the share falls with it: shoppers go back to private stores. Other readings use mature firms' rate (4.4% a year) and no failures. Closing a funded store is the cautious reading, even though the Source already pays a community business's running-cost gap.
5. **Large infrastructure: charters, not loans.** Utilities, roads, transit, airports and ports are already financed mostly by state and local borrowing ($4.5 trillion of municipal bonds outstanding, SIFMA, mid-2026). The Collectives would not lend at that scale. the author's route is a charter: an existing public operator becomes a community business. In the model only utilities have a community-business price; transport and the rest have none (the papers give no figure). So the charter reading lets the utility part of the price cut reach the customers of public operators without new capital: one in seven electricity customers (APPA). Their existing bonds stay with them, since their debt service is already in the observed running cost of public power (0.839 of investor-owned prices). The Source pays the gap to the community-business price, as it does for every community business. Water is publicly supplied to 90% of Americans, but EPA gives no ownership share, so the model's electricity share stands for all utilities (a stated limit). Larger charter shares (one third, two thirds) are design parameters, swept.
6. **The density tests** (the 40% test) keep reading the network's share of sales without the chartered utilities, the reading with the smaller effect.

## What would count as an answer
- How much faster the community businesses' share grows with the fund, in each environment and design, and what it does to basket poverty, wealth poverty, median wealth and savings against the main row.
- What the fund costs net of repayments and write-offs, per adult a year, and per point of poverty reduced.
- Whether charters of public operators change any outcome, and at what subsidy.
- Expected from the check above: the main effect, if any, is under Stress and in the opt-in design. Under Reference and Adverse the ceiling binds by year 10 anyway. A null result there is reported as such.

## What is left out
- Lending to private start-ups that are not community businesses: the model has no firms, so it cannot represent private entry.
- Transport, health care and child care charters: the model gives these sectors no community-business price.
- Interest rates the fund might charge below market, and recoveries on failed loans: no source opened.
- Capacity by zone: the fund, like reinvestment, adds capacity for the whole population.

=== The sources script and its output (sources/s94_lending.py) ===
"""Start-up finance for small essential providers, and public operators: the values for the Creative Collectives' lending switch.
Written Nov 20, 2026 for the study of the Collectives' lending to start-ups where banks will not lend (research-update
prereg/2026-11-s94-collectives-lending.md). The engine constants of the switch are set from the figures this file prints.

Sources (all opened Nov 20, 2026):
- Census Bureau, Business Dynamics Statistics 2023 release, tables by sector (bds2023_sec.csv) and by sector and firm age
  (bds2023_sec_fa.csv), www2.census.gov/programs-surveys/bds/tables/time-series/2023/. Rows for utilities (22), retail trade (44-45) and
  accommodation and food services (72), 2014-2023, are saved in s94_lending/; the full downloads' SHA-256 are recorded below.
- BEA, Fixed Assets Table 3.1ESI, current-cost net stock of private fixed assets by industry, yearend 2025 (Section3All_xls.xlsx, file
  created Sep 28, 2026): utilities (line 9) $4,250,891m, food and beverage stores (line 45) $383,164m, food services and drinking places
  (line 95) $454,294m. Their sum, $5,088,349m, is the stock behind the engine's capacity rule ($18,862 per adult).
- Federal Reserve Banks, Small Business Credit Survey, 2025 Report on Employer Firms (survey of 2024): "41% of applicants received all
  the financing they sought, 36% received just some, and 24% received none"; fully approved by firm age: 0-5 years 48%, 6-20 years 48%,
  21+ years 64%; retail 49%. The page is saved in s94_lending/sbcs2025_p_fully_approved.txt.
- Reinvestment Fund, Pennsylvania Fresh Food Financing Initiative (2004-2010): a $30 million state grant leveraged with $145 million;
  "loans and grants for predevelopment, acquisition, equipment and construction costs, as well as for start-up costs such as employee
  recruitment and training", for operators "in communities where infrastructure costs and credit needs were not met by conventional
  financial institutions"; 206 applications, 88 projects financed; $73.2 million in loans and $12.1 million in grants approved.
- American Public Power Association, "Public Power" (publicpower.org): public power utilities "serve 1 in 7 electricity customers".
- EPA, Information about Public Water Systems (updated Mar 16, 2026): public water systems "provide drinking water to 90 percent of
  Americans"; "A public water system may be publicly or privately owned" (no ownership share given).
- SIFMA, US Municipal Bonds Statistics (Nov 3, 2026): outstanding $4.5 trillion (2Q26); issuance through October 2026 $521.0 billion.
- BLS, Business Employment Dynamics Table 7, survival of private sector establishments by opening year (read through the fetch tool; only
  the 1994 and 1995 cohorts were read verbatim): all private, 79.6% and 78.8% survive one year, 49.6% and 48.8% five years; retail, 1994
  cohort, 82.8% and 52.4%. A cross-check only: the engine uses the BDS rates below, which cover 2014-2023.

Run: python3 sources/s94_lending.py
"""
import csv, os
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's94_lending')
FULL_SHA256 = {
    'bds2023_sec.csv': '758a263b166167e9557d4fc4ba8cd60229c5e05d341214b7494982c4764cf224',
    'bds2023_sec_fa.csv': '07f3b6c3e34add284c1e5b900605eb6d45b4c22420cc4670ee0a9e0d94661755',
    '2025-report-on-employer-firms.pdf': 'a637b0030a236af2428ab9bbd6b9dfb80d6d72c5ab7f91a13a6e674d8b9ccbac',
    'reinvestment.com FFFI page': '52dabc02cb9c7eeba0c6ebb033ef101730b4d57b1d152e478c69023d6ea3c6d5',
    'publicpower.org public-power page': '51ed8ea75316f0e4f6335367e6fe29f8e37dec9ece42bb4405fd0755407c0e5f',
}
STOCK = {'22': 4250891, '44-45': 383164, '72': 454294}  # BEA 3.1ESI yearend 2025, $m (food stores and food services weighted at their own lines)
TOT = sum(STOCK.values())
W = {k: v/TOT for k, v in STOCK.items()}

def num(v):
    try:
        return float(v)
    except ValueError:
        return None

sec = list(csv.DictReader(open(os.path.join(HERE, 'bds2023_sec_extract.csv'))))
fa = list(csv.DictReader(open(os.path.join(HERE, 'bds2023_sec_fa_extract.csv'))))

print('Capital weights (BEA 2025 net stock): ' + ', '.join('%s %.4f' % (k, W[k]) for k in W))

# 1. The pace at which new establishments add capacity: jobs created by establishment births over the sector's jobs (BDS
#    job_creation_rate_births), mean of 2014-2023, weighted by the capital each sector holds in the capacity rule.
pace = {}
for s in STOCK:
    v = [num(x['job_creation_rate_births']) for x in sec if x['sector'] == s]
    v = [a for a in v if a is not None]
    pace[s] = sum(v)/len(v)
PACE = sum(W[s]*pace[s] for s in STOCK)
print('New establishments add, per year (% of the sector\'s jobs, 2014-2023 mean): ' + ', '.join('%s %.3f' % (s, pace[s]) for s in STOCK))
print('Capital-weighted pace: %.3f points of the sectors\' capacity a year  -> CL pace main %.4f' % (PACE, PACE/100))

# 2. Exit rates of establishments of young firms, by firm age (BDS estabs_exit_rate), mean of 2014-2023, capital-weighted.
AGES = ['b) 1', 'c) 2', 'd) 3', 'e) 4', 'f) 5', 'g) 6 to 10', 'h) 11 to 15', 'i) 16 to 20', 'j) 21 to 25', 'k) 26+']
def exit_rate(age):
    out = 0
    for s in STOCK:
        v = [num(x['estabs_exit_rate']) for x in fa if x['sector'] == s and x['fage'] == age]
        v = [a for a in v if a is not None]
        out += W[s]*sum(v)/len(v)
    return out/100
EX = [exit_rate(a) for a in AGES]
print('Exit rate by firm age (capital-weighted): ' + ', '.join('%s %.4f' % (a.split(') ')[1], e) for a, e in zip(AGES, EX)))
# The hazard for a unit in its k-th year after opening (k = 1, 2, ...): ages 1-5 one by one, then each band's rate for its years.
haz = EX[:5] + [EX[5]]*5 + [EX[6]]*5 + [EX[7]]*5 + [EX[8]]*5 + [EX[9]]*15
surv = 1
for k in range(5):
    surv *= 1 - haz[k]
print('Survival to 5 years: %.3f (BLS cross-check, all private 1994-95 cohorts: 0.49-0.50; retail 1994: 0.524)' % surv)
s40 = 1
for h in haz[:40]:
    s40 *= 1 - h
print('Survival to 40 years: %.3f' % s40)
print('CL hazard young (main), years 1-40: [' + ', '.join('%.4f' % h for h in haz) + ']')
print('CL hazard mature (other reading): firms 26+ every year %.4f' % EX[9])

# 3. Credit: the share of applicants that banks turn away in full or in part (context; not an engine constant).
print('Small employer firms, 2024: 41% fully funded, 36% in part, 24% none; fully approved 0-5 years 48%, 21+ years 64%.')
# 4. The Pennsylvania programme's mix of loans and grants.
L, G = 73.2, 12.1
print('Pennsylvania FFFI: loans %.1f, grants %.1f ($m): grant share %.4f  -> CL grant share main' % (L, G, G/(L + G)))
# 5. Public operators.
print('Public power: 1 in 7 electricity customers -> CL charter share main %.4f' % (1/7))
print('Municipal bonds outstanding (SIFMA, 2Q26): $4.5 trillion; issuance Jan-Oct 2026: $521.0 billion (context only).')

--- output ---
Capital weights (BEA 2025 net stock): 22 0.8354, 44-45 0.0753, 72 0.0893
New establishments add, per year (% of the sector's jobs, 2014-2023 mean): 22 2.493, 44-45 3.447, 72 6.880
Capital-weighted pace: 2.957 points of the sectors' capacity a year  -> CL pace main 0.0296
Exit rate by firm age (capital-weighted): 1 0.2238, 2 0.1323, 3 0.1410, 4 0.1249, 5 0.1036, 6 to 10 0.0843, 11 to 15 0.0674, 16 to 20 0.0583, 21 to 25 0.0504, 26+ 0.0440
Survival to 5 years: 0.454 (BLS cross-check, all private 1994-95 cohorts: 0.49-0.50; retail 1994: 0.524)
Survival to 40 years: 0.060
CL hazard young (main), years 1-40: [0.2238, 0.1323, 0.1410, 0.1249, 0.1036, 0.0843, 0.0843, 0.0843, 0.0843, 0.0843, 0.0674, 0.0674, 0.0674, 0.0674, 0.0674, 0.0583, 0.0583, 0.0583, 0.0583, 0.0583, 0.0504, 0.0504, 0.0504, 0.0504, 0.0504, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440, 0.0440]
CL hazard mature (other reading): firms 26+ every year 0.0440
Small employer firms, 2024: 41% fully funded, 36% in part, 24% none; fully approved 0-5 years 48%, 21+ years 64%.
Pennsylvania FFFI: loans 73.2, grants 12.1 ($m): grant share 0.1419  -> CL grant share main
Public power: 1 in 7 electricity customers -> CL charter share main 0.1429
Municipal bonds outstanding (SIFMA, 2Q26): $4.5 trillion; issuance Jan-Oct 2026: $521.0 billion (context only).

=== The preregistration (prereg/2026-11-s94-collectives-lending.md) ===
# Preregistration: the Creative Collectives' lending to start-ups where banks will not lend, and charters of public operators

Committed Nov 20, 2026 by S94 (part 1), before any build or run. Engine: compassionism-simulation at commit `3835242968d6a11d4d8070c9b2d4a249d5a11649` (main, after the frozen-model wording correction). The switch is built on branch `claude/s94-collectives-lending`. Its commit is recorded in an amendment before the first study run.

Claude's reading of the design: compassionism-simulation `dev/reports/s94-collectives-lending-reading.md`. Values: `sources/s94_lending.py` (all sources opened Nov 20, 2026). the author's words: ledger step S94, Nov 17 and Nov 19.

## Why
the author (Nov 17): the Creative Collectives can lend to or support start-ups where banks will not. the author (Nov 19): small essential providers get help with premises, logistics and set-up costs; large utility and transport projects are financed by municipal bonds and public debt, and public operators could move to Collective charters. The study of output per hour lists this as a limit. The Hub's papers give the Collectives no lending role (reading, section 2), so this models the author's statement as an addition to the design.

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
6. **Into the main row:** if rule 3 holds in at least one environment and design, and rule 4 holds, the fund at its main reading is proposed for the release's main row as the author's design statement. The decision is the author's (ledger decision; default: the fund joins the main row at the release, with charters off). If rule 3 holds nowhere, the fund is reported as a reading beside the main row, and the main row is unchanged.
7. **No tuning:** nothing is changed to reach a figure. The values above come from opened sources, or are labelled design parameters and swept. A change after the dry run is a dated amendment with its reason and a full rerun.

## Reporting
Every cell above is published, null and unfavourable results included, in compassionism-sim-results and in a plain-words report (`dev/reports/s94-collectives-lending.md`), with the findings-page text if rule 6 applies. the author's words are attributed to him and kept apart from the results.

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
