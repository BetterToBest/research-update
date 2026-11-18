# Preregistration: limits on supply and on indexing, read along the backing curve (S82, the v6 engine)

Committed Nov 17, 2026 by S82, before any switch below is built and before any run. Engine: compassionism-simulation at commit `38753fa5e731bbc5289fb91e68cb54f1a901a23f` (main, v5.9.15). The switches land on branch `claude/s82-supply-indexing` from it, each off by default (guard test identical). The sourced values, the engine commit of the dry run and of the batch, and the dispatch lines are recorded in Amendment 1 before the dry run (moved to Amendment 2 by Amendment 1).

Claude's reading of the design for this step, in plain words: compassionism-simulation `dev/reports/s82-supply-reading.md` (same commit as the build's first commit).

## Why

The release reviews (triage `audits/2026-11-release-review-triage.md`, theme 1; in-house finding 1; Nemotron B2-B3) found that below full backing the model has no limit on what the economy can supply: wages, the Basic Unit (BU) and the basket follow prices in full and at once, and no household is ever short of goods. So with no backing, the programme still cuts basket poverty by about 31 points at 40% inflation a year (v5.9, question 4's report), and the only payers are holders of savings and lenders. This study reads the backing curve with three limits added, each behind its own switch: (a) essentials demand above what the economy can supply is cut; (b) wages follow programme inflation only in part; (c) the BU follows prices with a delay. It carries the triage's smaller readings in the same batch (themes 9-11, 13, 15, 20, 22, 24).

**The limit as agreed with Duke (Nov 17, two discussions).** (1) It applies only to goods with physical capacity: housing, medical care and food. Copied goods are never limited. (2) It is what the economy can produce, not a policy cap, and not today's consumption of the needs baskets: today's economy produces far more of all three than the needs baskets use, and that headroom is counted. (3) No producer's sales, earnings or conversion rate is capped. (4) Prices act first, then idle capacity and the above-needs consumption better-off households give up as prices rise, then new capacity built over the years. Only what is still unmet is cut. (5) It is behind a switch, off = identical, and inactive at full backing, so the main row's figures cannot move. (6) Supply in all three sectors is partly set by policy (land use, residency places and licensing, farm programmes that pay to idle land). The low readings are labelled as those policies, not as facts of nature. (7) How a shortfall is shared is not settled by one assumption: three rules are run side by side (below). (8) The design's cost-of-living adjustment is monthly or quarterly (Duke, Nov 17; the Hub's Inflation Surge Protocol: "Monthly COLA adjustments to basic units"); a yearly one is acceptable.

## What the engine does today (read in the code before this file; no run)

1. **Essentials.** `runYear` accumulates `PRICE.acc.essD`, the mean over adults of the share of the needs basket the adult paid for (the write-off at the debt floor and, with `SPEND_GRADE`, the spending cut counted unmet; `index.html` 6641-6643, households after pooling 4558-4560). `tbRunCore` (7250, 7290 ff.) compares it with the supply path `S` (under `fx.sp` the no-programme run's own path, `tbBaseS`) and sets next year's essentials prices `P_E,k = 1 + θ_k (D − S)/S` (`pmEssLevel`; θ food 0, housing 0.6, medical 0.5, unsourced placeholders), times the general level. Every household then receives what it paid for. In supply-and-demand terms, θ is a market in which supply and above-needs demand absorb any extra need at a price rise of θ per unit of excess: the implied elasticity is 1/θ (1.7 housing, 2 medical, unlimited food), and supply never runs short.
2. **The capacity price rule's rationed share** (`prRat`, `prRatE`) and shadow-price readings (`prSh`, `prWsh`, `prPovSh`) are reported only (`prRes`; `PR_KEYS`: "nothing reported feeds back"). The price-rule study found that under today's rule about 22.5% of demand a year at no backing (full coverage, Reference) is more than any output could supply, because the year's new money is spent at last year's prices (`dev/reports/s58-price-rule.md`, item 5).
3. **Wages:** `wg += PRICE.wIdx × PRICE.piG` (6395), `piG` the year's endogenous general inflation; `wIdx` 1 in the release row. In a no-programme run `piG` is 0, so `wIdx` acts only where the programme adds inflation. Exogenous inflation reaches wages only with `AUD.wOut`.
4. **The BU** under the C2.2 design (`C22.idx` 'needs', the headline design) is reset each year to the year's price of the needs, `colaF = oIdx × c22Share(comp)/c22Share(null)` (6204): no delay. The release design's surge protocol (6203) ratchets to the full level in a year whose rise exceeds 5%.
5. **Timing:** prices for year t are set at the end of year t − 1; households shop at the year's prices.
6. **Not in the engine:** the Inflation Surge Protocol's "enhanced luxury restrictions" and "temporary conversion limits" (Hub, integrated implementation roadmap). Both would lower demand in a surge; leaving them out is the cautious side for the design. Not in this study.

## Questions

- **Q1 (supply).** At each backed share below 1, how much of the programme's effect on the four primary outcomes remains when essentials demand above what the economy can supply is cut, under each supply reading and each sharing rule?
- **Q2 (wages).** The same, when wages follow programme inflation only in part.
- **Q3 (BU indexing).** The same, when the BU follows the price of the needs with a monthly, quarterly, yearly or two-year delay.
- **Q4 (together).** Do the three interact? (2 × 2 × 2 factorial at the central readings, at each backed share.)
- **Q5 (who goes short).** Under each sharing rule, the essentials shortfall by fifth of cash income and by participation, beside the no-programme run's unmet need on the same scale (the market's rationing by ability to pay today).
- **Q6 (the triage's smaller readings).** Each at the main row and at no backing.
- **Q7 (the screen).** The assumptions screen in Stress, and on the financed rows with the weighted top tail.

An answer to Q1-Q4 is a table per environment of the programme's paired effect at every backed share under every reading, with intervals, and the break-even backed shares under each reading.

## What is built (each behind its own switch; off = identical, proved by full-output diffs and the guard test)

### A. Essentials supply (`SUPPLY_LIMIT`, row option `sl`)

On the programme run of a pair paid for by the Source (`o.fin` 'source'). Not applied to rows paid for by a contribution (backing is not defined there) and not to the no-programme run, which is never short by construction: its supply is its own demand (a stated limit).

At the end of each year t − 1 (the essentials prices' timing), for each sector k (food, housing, medical), in shares of the supply path `S`:
- `D` = the year's demand before any cut (the engine's `essD` with this study's cut added back, so a cut does not lower the demand it answers), `e = max(0, D/S − 1)` the excess, and `eu = (1 − a) e` the part not met by the programme's own output (`a` the row's backed share, `o.a`; at `a` = 1, `eu` = 0 and nothing is ever cut).
- Met at once: idle capacity `v_k` and the above-needs consumption that better-off households give up as the sector's price rises, `m_k × η_k × θ_k × e` (`m_k` the above-needs share of the sector's output, `η_k` the price elasticity of that demand, `θ_k e` the engine's own relative price rise for the sector). `θ_food` is 0, so food's price does not move and food meets extra need only from idle capacity and new capacity (a stated limit of today's placeholder).
- Capacity built so far `c_k` (0 at the start).
- Cut: `r_k = max(0, eu − c_k − v_k − m_k η_k θ_k e)`, as a share of `S`; next year's share of demand cut is `R_k = r_k / (1 + e)`.
- New capacity: `c_k += λ_k × max(0, eu − c_k − v_k)` (building answers the lasting excess above idle capacity, both the part cut and the part met by squeezing above-needs use; it persists).

**Supply readings** (option `rd` of `sl`), every sector at once:
- `'full'`: every extra need met (infinite headroom): today's engine. A check row, not a reading.
- `'sourced'`: `v_k`, `m_k`, `η_k`, `λ_k` from sources opened before the dry run (script `sources/s82_supply.py` in compassionism-simulation, output JSON; values in Amendment 1). Named now, to be opened: housing: rental and homeowner vacancy (Census Housing Vacancy Survey) against its normal level (the price-rule study already opened 7.1% against 7.3%); the price elasticity of housing demand; new construction as a share of the stock and its price response (Census new residential construction; Saiz 2010). Medical: residency places and their growth (NRMP), physicians per capita; the price elasticity of medical care (RAND Health Insurance Experiment). Food: exports and idle cropland (USDA ERS; Conservation Reserve Program acreage); the price elasticity of food demand (USDA ERS). For `m_k`: BEA personal consumption expenditures by function (housing and utilities, health, food) against the MIT needs baskets for the model's population. A value whose source cannot be opened is a labelled design parameter, set to the middle of its range here: `v` 0.02, `m` 0.3, `η` 0.5, `λ` 0.25.
- `'restricted'`: every sourced value halved. A design parameter standing for supply held back by today's land-use, residency and farm policies, labelled as a policy reading.
- `'strict'`: `v = m = λ = 0`. No essentials beyond what the no-programme economy gives the needs baskets. Neither the economy nor the design; the strictest case the reviews raise, reported as a bound.

**Sharing rules** (option `sh`), each household's cut `x_i` in dollars at the year's prices, summing to the sector's cut; no household cut beyond its own spending on the sector:
- `'pay'` (the market's rule: those least able to pay go short first): `x_i ∝ E_ik × 2 (1 − F_i)`, `E_ik` the household's spending on sector k, `F_i` its rank in cash income over its cost of living (0 the least able to pay, 1 the most). Reported first in every table: it is the most cautious rule for the programme's claims and what a shortage does when nothing protects the basics.
- `'even'`: `x_i ∝ E_ik`.
- `'bu'` (the design's rule: basics bought with BU are served first, because a provider converts the BU it accepts at three times face value under the progressive tax, which the model already pays): `x_i ∝ max(0, E_ik − BU_ik)`, the part bought with cash; if that total is smaller than the cut, the rest `∝ E_ik`. With no BU (a non-participant) it is the even rule.

**What a cut does to a household.** It does not receive `x_i` of housing, care or food. Main reading: the money is spent on other goods at the year's prices, so cost, income and wealth are unchanged and a shortage raises no one's savings (the cautious reading for the wealth results). Option `fs`: the money is kept as savings (cost falls by `x_i`). Basket poverty on what was received: the gap is `max(0, cost − income + x_i) / basket` (money that cannot buy the needs does not count toward them); `fgt0PY` and `fgt2PY` read it with `sl` on; the paid-for gap is kept beside as a reporting key. BLEI and wealth move only through prices in the main reading.

No random draw. Households are cut as the household reading decides their status (after pooling).

### B. Wages that follow programme inflation in part (study option `wIdx`, existing; new option `wc`)

`wg += wIdx × π_t + wc × (1 − wIdx) × π_{t−1}`, `π` the year's endogenous general inflation. `wc` 0: the part not indexed is never made up; `wc` 1: it is made up a year later. Both runs (a no-programme run has `π` = 0, so it is unchanged: a check). Default `wc` 0, so `wIdx` 1 is identical whatever `wc`.

### C. The BU's delay (`BU_LAG`, row option `bl`, in years)

The price index the BU is set from (the C2.2 needs' price; with the surge protocol, its full level) is read at `t − L`: `exp((1 − f) ln I(t − n) + f ln I(t − n − 1))`, `n = floor(L)`, `f = L − n`; years before 0 read year 0. Readings: `L` = 0.125 (a monthly adjustment: half a month's average delay plus a month for the figures), 0.25 (quarterly), 1 (yearly, as Social Security's COLA), 2 (a bound). `L` 0 is today. It applies to the programme's BU and child allowance. Today's safety net in both runs keeps the engine's indexing, so the delay falls only on the programme run (the cautious side).

### D. Reporting keys (study option `s82`; reporting only, draws nothing, changes no adult)

The excess `e`, the unbacked excess, `R_k`, `c_k` by sector (means over the run and the last year); the essentials shortfall (mean `x_i` over the basket, %) overall, by fifth of cash income and by participation; the same for the no-programme run's unmet need; the real BU (BU over the needs' price) and the real wage (mean wage over the general level) at year 20; the paid-for basket gap; the share of adult-years below 30 days of basic living, weighted (triage theme 10); wages over factor income beside labour's share of money income (theme 22). Computed by the job from each pair: wealth poverty at 50% of the same seed's no-programme median real wealth, for both runs (theme 24). The engine comment that says no rule reads the weights (`index.html` about line 4237) is corrected (theme 10).

### E. The triage's smaller readings (existing options unless stated)

1. The wage-only spending share 0.862 (theme 9): `sc` 0.862 on both runs.
2. The top tail's exponent at plus and minus two standard errors, 1.762 and 1.218 (1.490 ± 2 × 0.136), and one other cutoff, the 95th percentile, fitted by `sources/s59_tail.py`'s method and added to `WT_CUTS` before the dry run (theme 11).
3. Ageing: `AGE` on with `lf.fl` 'panel', at 20 and 40 years (theme 13). Partnerships stay fixed (a stated limit).
4. PTH's equity base from the basket: new option, 25% of the member's actual PTH saving (the MIT housing component's 35% cut) instead of the saving at the BLEI daily cost (12.6% of the actual saving; theme 15).
5. The screen: compassionism-sim-results `runner/jobs/s70-screen.js`, as frozen in `prereg/2026-11-s70-screen.md`, its Source block in Stress and its financed block in all three environments with the weighted tail on (theme 20). Same inputs, ranges, trajectories and rules.

## Design

- **Pairs.** The frozen round-2 main pair (`harness.js` `r2FreezePair`, the C2.2 design, full coverage, today's price rule), with the programme run at backed share `a` = 0, 0.25, 0.5, 0.75 or 1. Every reading as stated above; B and E on both runs.
- **Rows per environment** (programme rows unless stated):

| Part | Rows | Count |
|---|---|---|
| Base | the programme run at each of the 5 shares; the no-programme run | 6 |
| A, supply | 3 readings (sourced, restricted, strict) × 3 rules × shares 0-0.75; option `fs` (sourced, `pay`) at shares 0 and 0.5 | 38 |
| A, checks | `'full'` at share 0; `'strict'` with each rule at share 1 | 4 |
| B, wages | `wIdx` 0.5 and 0.75 × `wc` 0 and 1 × 5 shares; the no-programme run with each | 24 |
| C, BU delay | `L` 0.125, 0.25, 1, 2 × 5 shares | 20 |
| Q4, factorial | at the central readings (A sourced, rules `pay` and `bu`; B `wIdx` 0.75, `wc` 1; C `L` 1): AB, AC, ABC with each rule and BC, at shares 0-0.75 (7 each); BC at share 1 | 29 |
| E1-E4 | each its own pair at shares 0 and 1 (the no-programme run shared): spending share, tail low, tail high, other cutoff, PTH base, ageing | 18 |
| | | **139** |

- **Environments:** Reference, Adverse, Stress.
- **Seeds:** 1-500, paired across every row (common random numbers); 500 adults; 20 years, and 40 years as the round-2 batch ran them.
- **Where it runs:** GitHub Actions, the `run-study` workflow of compassionism-sim-results (`prereg/RUNNING.md`), a new job `runner/jobs/s82.js` (every reading a row option of the pinned engine), seeds split into shards (paired, so splitting changes no figure). First a dry run at seeds 1-2 (timings, shard sizes, every check), then the batch, then the screen (`s70-screen.js`). Results folders `s82-<part>-<env>-<years>-<engine 7>` and `s82-screen-<block>-<engine 7>`, each with `run.txt` and `SHA256SUMS`.
- **Cost:** 139 rows × 3 environments × 500 seeds × about 1.86 s (both horizons, the round-2 dry run's rate) ≈ 108 core-hours, plus the screen (about twice S70's two blocks; measured in the dry run). Well below `prereg/RUNNING.md`'s 1,000 core-hour mark. Free. No Runpod, no other paid service.
- **Outside reading:** an NVIDIA-hosted model (a different maker from Claude) reads this file and Amendment 1 before the dry run, as `audits/2026-11-17-nvidia-setup.md` describes. Its reply is saved in `audits/` and triaged. It is a reading, not a result.

## Outcomes

**Primary** (the headline can only come from these; Q1-Q4, each backed share, each environment, 20 years; each the paired programme − no-programme effect):
1. basket poverty (`fgt0PY`; under A, on what households received);
2. below 30 days of basic living, design-neutral (`bNAPy`);
3. wealth poverty, the yearly average over years 1-19 (`ppovA`, as question 4's report), and at the last year (`pov`);
4. median real wealth, weighted (`wtMedE`) and unweighted (`medWealthReal`).

**The change a reading makes** = the reading's effect − the base effect at the same share, paired by seed.

**Secondary:** programme inflation (`endoAnn`); the Q5 shortfall table; `R_k` and `c_k`; the real BU and real wage; poverty severity (`fgt2PY`); the shadow-price readings (`prSh`, `prWsh`, `prPovSh`); the household reading; the 40-year figures; the D keys; Q6 and Q7's outcomes as their own preregistrations define them (Q7: `prereg/2026-11-s70-screen.md`).

Every gain is confirmed on basket poverty and wealth poverty, not on severity alone.

## Analysis

- Paired differences over seeds, 95% paired-bootstrap intervals (10,000 replicates, seeds resampled), as the study reports from S36 on.
- **Break-even backed shares** under each reading, by question 4's method: scanning down from 1, the share at which each primary outcome's effect is no better than no programme, by linear interpolation between grid points, with the bootstrap interval of the crossing; never extrapolated ("below 0" where no point reaches it). The same for programme inflation reaching 5 points a year.
- **Q4:** at each share and each rule, main effects and all interactions of the 2 × 2 × 2 design, with intervals; Shapley shares of the joint change. An interaction is claimed only where its 95% interval excludes zero (research rule 4).
- **Multiple comparisons:** Holm across the four primary outcomes within each question, environment and share, for any statement that a reading "changes the effect"; unadjusted intervals published beside.

## Checks (before any table is read; each must pass)

1. Off = identical: the guard test, and full-output diffs with every new option at its off value.
2. Nesting: A `'full'` at share 0 equals the base programme row in every key.
3. Inactive at full backing: A `'strict'` at share 1, every rule, equals the main row in every key.
4. The no-programme run is unchanged by A and C, and by B (`π` = 0 there).
5. B with `wIdx` 1 is identical whatever `wc`; C with `L` 0 is identical.
6. The money accounts (MODEL_SPEC section 11) close with every new option on; under A the cut's dollars appear once (spent on other goods, or saved with `fs`).
7. Eight random draws per adult-year, unchanged; A draws nothing.
8. The release start's baseline check (`startRelease({baseline: true})`) passes in the job.

## Decision rules (fixed now)

1. **A failed check:** the defect is fixed, and the whole batch is rerun on the new engine commit; only the rerun is reported.
2. **"Holds under a supply limit"** (per backed share, per primary outcome, never pooled across shares): the effect keeps its sign and its 95% interval excludes zero under the sourced reading with all three sharing rules.
3. **Depends on the rule:** where it holds with the design's rule but not the market's, the report says the result rests on how a shortage is shared, and that the market's rule is what a shortage does when nothing protects the basics.
4. **The strict bound** is in every table, labelled "the strictest case: no essentials beyond today's needs consumption; not the economy and not the design". No headline is taken from it alone, and no statement about supply limits leaves it out.
5. **The findings page.** The main row's headlines cannot change (full backing; check 3). The dated note on "the poverty effects barely depend on backing" is replaced by the curve under the sourced readings, with the restricted and strict readings beside it and the break-even shares under each.
6. **Indexing:** Q3's monthly and quarterly readings (the design's) are reported first, then the yearly, then the two-year bound. A sentence about indexing names the delay.
7. **Q4:** if an interaction's interval excludes zero, the readings' separate effects are not summed anywhere; the joint row is reported.
8. **No tuning:** nothing here is changed to reach a figure. The sourced values are fixed in Amendment 1 from opened sources only, before the dry run. A change after the dry run is a dated amendment with its reason and a full rerun.

## Reporting

Every cell above is published, null and unfavourable results included, in compassionism-sim-results and in a plain-words report (`dev/reports/s82-supply-indexing.md`), with the findings-page text. Advocacy material may lead with the strongest robust findings; nothing is dropped from the record. Duke's views on supply policy are attributed to him and kept apart from the results.

## Limits stated in advance

- Only housing, medical care and food can be short (Duke's narrowing). Other goods and copied goods are never cut. The general shortage at no backing (price-rule study, item 5) stays a reported reading at shadow prices.
- The extra need is one share of the basket, spread over the three sectors in the basket's proportions.
- A cut answers last year's gap (the engine's price timing).
- The essentials price response θ is unchanged and unsourced. With A on, prices and quantities are not derived from one elasticity.
- The no-programme run is never short. Its poorest go without through prices, as today.
- The surge protocol's luxury restrictions and conversion limits are not modelled (cautious side).
- Building capacity costs nothing in the model's accounts; Creative Collectives' lending and output per hour are the next engine step (S85).

## Amendments

Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (Nov 17, 2026, after the build and before any run for results)

**The build.** compassionism-simulation `claude/s82-supply-indexing` (v5.9.16, engine commit `cf17465`; pull request 151, merged as `2120662`; Claude's reading `dev/reports/s82-supply-reading.md`; decisions in `dev/DECISIONS.md`, "S82"). Guard test identical (25 rows, 20 seeds, 483 outputs, Reference and Adverse). Unit suite `s82UnitSuite`, 5 tests, all pass. Nothing in the questions, readings, grids, outcomes or decision rules changes. What the build settled, and why:
1. **Names.** `sl` and `bl` are options of the row's price options (`c.o.sl`, `c.o.bl`), set per row like the backed share `a`, not top-level row options. Both are added to `SP_PROG_OPTS`, so the no-programme supply path never sees them. `wc` is a price option too.
2. **"The engine's essD with this study's cut added back".** The cut changes neither cost nor wealth in the main reading, so the engine's `essD` already measures demand before the cut. The build uses it as it is.
3. **The cut's total.** The engine's poverty accounting runs adult by adult. Each cut is therefore allocated as the adult is accounted, using last year's totals as normalisers and last year's ranks for the market rule. The realised cut is close to the sector's share, not equal to it. It is reported (`slCutSh`) beside the target (`slRfood`, `slRhousing`, `slRmedical`). In the 2-seed build check the realised share was within about 5% of the target, in both directions. Section A's "summing to the sector's cut" is read as "summing to about the sector's cut, the realised share reported". A second pass at year end would make it exact, but it would move the poverty accounting and its reporting modules, so it is not done.
4. **`fs` (the cut kept as savings) is not built yet.** It is refused until it is built with its money accounts. Its two rows (Design, part A) wait for that build. If it is not built before the dry run, the rows are dropped, and that is said in the report.
5. **Sourced values.** `SL_SRC` holds the design-parameter middles named in section A (`v` 0.02, `m` 0.3, `η` 0.5, `λ` 0.25 in every sector) until the sources are opened. The sourced values, the dry run's engine commit, its timings and the dispatch lines move to **Amendment 2**, before the dry run (the header's "Amendment 1" now reads "Amendment 2").

**What was seen before this amendment.** A 2-seed smoke test of the build (Reference, 20 years, 500 adults; a session script, not kept) printed every check line and, on the same lines, the outcome keys of 13 rows at 2 seeds. The checks were that `'full'` equals the base programme row, `'strict'` at share 1 equals the main row, and `wc` with `wIdx` 1 equals the base. All three passed. The unit suite's run checks were also seen (200 adults, 1 seed). From those lines: at no backing, the programme run's essentials demand stands about 15% above the no-programme path (`slE`); the market rule cuts the poorest fifth 8-9 times as much as the richest; the BU-first rule cuts the richest fifth slightly more than the poorest. Nothing in the design, the readings, the grids or the rules was changed after seeing them. No 500-seed or 100-seed run has been made.

**The outside reading, triaged** (`audits/2026-11-17-s82-prereg-reading-mistral-partial.md`: Mistral Large's reasoning, word for word; it stopped at the token limit before writing an answer, so it is a partial reading. A full reply is still to be requested before the dry run.) Its points, checked against this file and the build:
1. *Units of the headroom* (confirmed; changes section A's wording, not the design). `e` is measured on the needs baskets (the engine's `essD`, the share of needs paid for), and `S` is the no-programme run's same share. It is not total sector output. So `v` and `m` are shares of the no-programme **needs consumption**: idle capacity over needs consumption, and above-needs consumption over needs consumption. Section A's "the above-needs share of the sector's output" is replaced by this. A sourced share of output is divided by needs' share of output before use (for example, needs 60% of output and above-needs use 40% give `m` = 0.67).
2. *A limits only the three essentials; the wealth figures move only through prices* (confirmed; already a stated limit, now a reporting rule). In the main reading the money a cut leaves unspent goes to other goods, which are never limited. So under A alone the wealth outcomes change only through the engine's prices. The report must say so beside every A row: A's real cost shows in basket poverty and the shortfall; B, C and the shadow-price readings are the ones that bear on wealth.
3. *The market rule ranks by current cash income, not savings or credit* (confirmed, as a limit). A household with savings but a low income is ranked as less able to pay. This is kept as preregistered (transparent and monotone) and stated as a limit in the report.
4. *A capped cut leaves the rest unallocated* (confirmed). When a household's cut reaches its whole spending on the sector, the remainder is not passed to others, so the realised cut falls short of the target. This is the gap reported as `slCutSh` (item 3 of the build notes above).
5. *The headroom terms are not derived from one market-clearing model* (already a stated limit; no change). The reading's source suggestions (Census Survey of Construction and Building Permits; USDA NASS acreage reports; AHA hospital beds; Census construction spending for health care buildings) are added to the list for Amendment 2. Each is opened before use.

### Amendment 2 (Nov 17, 2026, after the sources were opened and before the dry run; no run for results has been made)

**The sourced values** (compassionism-simulation v5.9.17, branch `claude/s82-part2-sources`, pull request 152; script `sources/s82_supply.py`, output `sources/s82_supply.json`, FRED files in `sources/s82_fred/` with their hashes; decisions in `dev/DECISIONS.md`, "S82 part 2"). The year is 2025, the last complete year and the year of the engine's other inputs. Every value is a share of the sector's no-programme needs consumption (Amendment 1, item 1).

| Sector | v, idle capacity | m, above-needs use | η | λ |
|---|---|---|---|---|
| Housing | 0: rental vacancy 7.10% and homeowner vacancy 1.15% are below their 1956-2025 means (7.27%, 1.52%; Census Housing Vacancy Survey) | 0.7914: BEA consumer spending on housing and utilities (rents and owners' rental value), $3,814 billion over 134.8 million households = $28,296, against the model population's needs, $15,796 a household (the engine's line, basket share and household ratios) | 0.697: Albouy, Ehrlich and Liu (2016, NBER w22816), their preferred column; their table's range 0.49-0.83 | 0.2: Wheaton, Chervachidze and Nechayev (2014, MIT), housing markets close about 20% a year of the gap to their long-run price-stock relation (68 metro areas). They find the correction runs mainly through prices, not the stock, so this is the generous side for building |
| Medical care | 0: hospital occupancy 75.3% (May 2023-April 2024) against 63.9% in 2009-2019 (Leuchter et al. 2025, JAMA Network Open, CDC data) | 0: the CE's household health spending, $6,470 a unit, against MIT's medical line for the model population, $6,544 (both the household's own payments) | 0.2: the RAND Health Insurance Experiment (Keeler and Rolph 1988, as summarised by Aron-Dine, Einav and Finkelstein 2013, NBER w18642) | 0.25: design parameter (no source opened) |
| Food | 0: food-manufacturing utilisation 84.9% against its 1972-2025 mean, 82.2% (Federal Reserve G.17) | 0: the CE's food at home, $6,491, against MIT's food plan, $7,508 (not used: θ food is 0) | 0.5: design parameter (not used: θ food is 0) | 0.25: design parameter (no source opened) |

What these choices mean, in plain words:
1. **Idle capacity is measured beyond normal use**, as the price-rule study measured slack. In 2025 the economy runs at or above its normal use of housing, food manufacturing and hospital beds, so nothing is met "at once" from idle capacity in any sector. Headroom to a practical maximum (85% hospital occupancy, Leuchter et al.'s shortage line: 13%; the lowest rental vacancy since 1980: 2%) is printed in the output, not used. Drawing on it is a price-driven response of supply, which the engine's form does not have, and the cautious reading leaves it out.
2. **Above-needs use is measured on matching coverage.** Housing is the one sector with large headroom: the economy's housing services are about 1.8 times the needs baskets' housing. The CE's housing outlays (owners' costs, not their homes' rental value) give 0.43, printed as the low end. The spending covers every US household, while the needs are the working-age model population's, which has more children and higher needs. So m is, if anything, understated.
3. **Consequence, stated before any run.** Under the sourced reading, medical care and food are met only by new capacity, and housing also by the use better-off households give up as rents rise. So the sourced reading is closer to the strict bound than the design-parameter middles (v 0.02, m 0.3 in every sector) were. Nothing here was chosen to move a figure. No outcome of any S82 reading has been seen at more than two seeds (Amendment 1).
4. **Sources named in Amendment 1 and not opened**: the Census Survey of Construction and Building Permits, USDA NASS acreage reports, AHA hospital beds, and Census construction spending for health care buildings. The measures used cover the same quantities: hospital occupancy from the CDC's staffed-bed data, and the speed of housing supply from the error-correction estimates. The idle cropland of the Conservation Reserve Program is not counted as idle capacity. Food manufacturing, not land, runs above its normal use, and food's price does not move in today's engine.

**`fs` is dropped** (Amendment 1, item 4). A cut is shared out in the poverty accounting, which runs after the year's wealth and money accounts are settled, so keeping the cut as savings would move those accounts and the reporting that reads them. Its two rows (Design, part A) are dropped. The batch has **137 rows** per environment and horizon. The main reading (the money is spent on other goods) is the cautious one for the wealth results, and the report says so.

**The smaller readings, as built.**
- E2: the tail exponent at 1.218 and 1.762 is `wt.a` at the main cut. The other cutoff is the 95th percentile, `wt.cut` 'p95' (`sources/s59_tail.py`, one line added; every stored fit reproduces; exponent 1.265, s.e. 0.092; threshold $3.59 million in 2025 dollars; the tail's weight is 5.1% of all against 2.6% at the main cut).
- E4: the PTH equity base from the basket is `fx.eb`. It is named `eb` because `fx.pe` (the PTH books when a member dies) is taken and is on in the main row.
- E3: ageing is row option `ag {}` with `lf.fl` 'panel'.

**The job.** compassionism-sim-results `runner/jobs/s82.js` (pull request 52).
- Its `--check` confirms the 137 rows against this file's counts.
- Its `--selftest` runs checks 1-8: every new option at its off value; nesting; inactive at full backing; the no-programme run unchanged; `wc` with `wIdx` 1 and `bl` 0 identical; the money accounts; eight draws per adult-year; the release start's baseline check.
- All eight passed on engine v5.9.17 (Reference, 500 adults, 20 years, seeds 1-2, equality tests only; no outcome value was printed), and every row runs.
- Results folders: one per environment and horizon, `s82-v6-<env>-<years>-<engine 7>`, holding every part's rows, named by part. This replaces "one per part", to keep the dispatches to six. The rows are the same.

**What remains before the dry run** (no change to the questions, readings, grids, outcomes or rules):
1. **Section D's reporting keys** are not yet built: the real BU and real wage at year 20; the no-programme run's unmet need by fifth; the weighted share of adult-years below 30 days; wages over factor income; wealth poverty at 50% of the same seed's no-programme median, for both runs; and the corrected weights comment. They come as a study option `s82` (reporting only) in the next engine version. The job stores every key with the prefix `s82` without a change.
2. **Question 7 (the screen).** `runner/jobs/s70-screen.js` runs Reference and Adverse only, and its financed block removes the weighted tail (S72 Amendment 2: two of the contribution's bases are not read with the tail on). Running it in Stress and with the tail on the financed block needs an environment and a tail flag in that job. Where a base is not read with the tail, a dated note here will say what is run in its place, before the screen runs.
3. **The full outside reading** of this file with both amendments (the Mistral reading stopped before its answer).
4. **The dry run** at seeds 1-2 on the final engine commit. Its timings, the shard counts and the dispatch lines will be recorded here, dated, before the batch.

**Seen while building this amendment** (no outcome read for a decision):
- A 200-adult, 1-seed probe printed the base programme row's median real wealth with and without `fx.eb` (457,903 against 457,514), to confirm that the option acts.
- The same probe printed the tail weight at the two cutoffs.
- A 200-adult, 1-seed accounts check printed only identity counts.
Nothing was changed after any of them.

### Amendment 3 (Nov 18, 2026, before the dry run; no run for results has been made): the strict-bound sweep, section D as built, and question 7 as run

**Why the sweep.** Duke asked on Nov 18 for a sweep on the strictest bound. Amendment 2 found that in medical care and food the sourced reading has no idle capacity and no above-needs use to give up. So in those two sectors it differs from the strict bound only by the building speed λ, 0.25 a year, a design parameter: no source was opened for it. Research rule 3 asks that design parameters be swept, and the design above did not sweep λ. Without the sweep, a statement that a result "holds under the sourced supply limit" would rest, for medical care and food, on one unsourced value. Duke gave a rule of thumb for engine additions at the same time: "source, measure, sweep test, inspect, verify, if correct validate, if not modify and repeat"; "the sweep is key." This amendment is that sweep for the supply limit.

**Rows added** (per environment and horizon; the batch has **197 rows**; rows 0-136 keep their numbers):

| Part | Rows | Count |
|---|---|---|
| Slam | The building speed of medical care and food, λ = 0, 0.1, 0.5 and 1 (the sourced row is 0.25), every other value sourced (housing m 0.7914, η 0.697, λ 0.2), × 3 rules × shares 0-0.75. At λ = 0, medical care and food are exactly at the strict bound and housing at its sourced reading. | 48 |
| Sgrid | The strict bound at shares 0.125, 0.375, 0.625 and 0.875 × 3 rules: the strict bound on a backing grid twice as fine. | 12 |

No share-1 rows are needed: at full backing nothing is cut (check 3). Food's λ is swept with medical care's. Food's price does not move (θ food 0), so new capacity is food's only headroom in today's engine as well.

**Analysis added** (nothing above changes):
1. For each primary outcome, share, rule and environment: the effect at each building speed (0, 0.1, 0.25, 0.5, 1), with intervals, and the change from the sourced row (paired by seed; Holm across the four primary outcomes as in Analysis).
2. **The slowest building speed at which a result holds:** per primary outcome and share, the smallest λ on the grid at which decision rule 2's test passes (the effect keeps its sign and its 95% interval excludes zero under all three rules). If λ = 0 passes, the result "holds at the strict bound for medical care and food". If λ = 1 fails, it "does not hold at any building speed on the grid". Read on the grid, never interpolated.
3. **Break-even backed shares at the strict bound** on the 9-point grid (0, 0.125, ..., 1), published beside the 5-point grid's as preregistered.
4. Break-even backed shares at each building speed (5-point grid).

**Decision rules added:**
- The sweep is a sensitivity reading of one design parameter. Decision rule 2 stays judged on the sourced reading. Every statement that a result holds under the sourced reading names, for medical care and food, the slowest building speed at which it still holds (item 2).
- Decision rule 4 (the strict bound's label; no headline from it alone) applies to the Sgrid rows and to the λ = 0 rows.
- No building speed is chosen after the run. The swept values are design parameters, labelled as such wherever they are shown.

**The engine** (compassionism-simulation v5.9.18, branch `claude/s82-part2b-strict-sweep`, pull request 154; decisions in `dev/DECISIONS.md`, "S82 part 2b"). It is off = identical: guard test identical, lineage link recorded, 392 unit tests.
- `sl.lam`: the building speed by sector over the reading's own value (a number, or `{sector: λ}`, in [0, 1]; refused with the full reading).
- Study option `s82`: section D's reporting keys (item 1 of Amendment 2's "what remains"). As built:
  - The unpaid need by fifth (`s82U`, `s82Uq1-5`, `s82UP`, `s82UN`) on both runs. The fifths rank the year's own adults by cash income over the cost of living. The supply cut is tallied again on the same fifths (`s82Xq1-5`), because the cut's own fifths (`slXq`) use last year's ranks and question 5 needs one ranking for both.
  - The share of adult-years below 30 days of basic living, weighted (`s82B30w`), beside the unweighted (`s82B30`, equal to `bNAPy`).
  - What a month of the BU buys at the needs' price (`s82BuR20`, `s82BuRE`).
  - The mean wage over the general price level (`s82WgG20`, `s82WgGE`). The engine's other real-wage figures divide by the basket's price.
  - Wages over factor income (`s82WF`, `s82WFPY`), beside labour's share of money income (`s82LS`, `s82LSPY`).
  - Wealth poverty at half the same seed's no-programme median real wealth (`s82Wp50`, the yearly average `s82Wp50A`, and weighted versions). The median is read from the supply-path run, which is that same no-programme run with the row's other options. In the no-programme run it is the run's own median (a check).
  - The weights comment corrected: the creditor side's totals and the contribution's books do read the weights.
- **The job** (compassionism-sim-results `runner/jobs/s82.js`): rows 137-196 added, and the study option `s82` on every run. `--check` confirms 197 rows. `--selftest` adds check 9: the building speed given at the sourced values equals the sourced row, at 0 it moves the limit; `s82` moves no other key; every run reads the no-programme median, and the no-programme run reads its own.

**Question 7, as run** (the dated note promised in Amendment 2, item 2). The screen job (`runner/jobs/s70-screen.js`) gains the Stress environment and a block FT, run with the frozen design's inputs, ranges, trajectories, outcomes and rules (`prereg/2026-11-s70-screen.md`):
- Block S in Stress: S70's design, unchanged (seed 70001, 408 points × 5 rows).
- Block FT, the financed rows with the weighted tail on, in Reference, Adverse and Stress. It is block F's design with the tail kept and its three inputs added, and the contribution's base held at wages: 43 inputs, 528 points × 3 rows, its own trajectories (seed 70003).
- **In place of the two bases not read with the tail:** block F (no tail) in Stress. S70 ran it in Reference and Adverse. Why: S72's Amendment 2 found that the tail's 18 adults, counted as ordinary adults in every decision, distort the bases "wages plus capital income" and "all money income": hours +143% with the tail against +21% without. That is a property of the engine's unweighted decisions, not of the contribution. On the wages base the tail changes nothing material.

**Cost.** 197 rows × 3 environments × 500 seeds × about 1.86 s (both horizons) ≈ 153 core-hours, plus the screen's five environment-blocks (measured in the dry run). Free on GitHub Actions, below `prereg/RUNNING.md`'s 1,000 core-hour mark.

**Seen before this amendment** (no outcome read for a decision; the sweep's grid was fixed before any of it was printed):
- A 200-adult, 1-seed smoke test of v5.9.18 (Reference, 20 years) printed the `s82` keys for the no-programme run, the base programme row at share 0, and the strict market-rule row at share 0:
  - unpaid need: 12.0% of the basket with no programme (51% in the poorest fifth) and 0.6% at share 0;
  - the strict cut: 7.9% of the basket in the poorest fifth, 0.9% in the richest;
  - wealth poverty at half the no-programme median: 36% with no programme and 24% at share 0.
- The unit test printed the same no-programme median twice (its check).
- Nothing in the design, the grids or the rules was changed after seeing them.

**What remains before the batch:** the full outside reading of this file with its three amendments; the dry run at seeds 1-2 on the final engine commit, its timings and the dispatch lines, recorded below, dated.

### Amendment 4 (Nov 18, 2026, after the outside reading and before the dry run; no run for results has been made)

**The outside reading** (`audits/2026-11-18-s82-prereg-reading-nemotron.md`: Nemotron 3 Ultra on the NVIDIA catalogue, word for word, with its triage; a Mistral Large attempt was cut before it answered). Of its points, three are confirmed and change the study. The rest are agreed as stated limits or not confirmed, with the reasons in the audit file.

1. **The real BU, fixed.** The key divided the BU by the whole basket's price. Section D asks for the BU over the needs' price, and the BU follows the C2.2 needs' price. On the basket's price the key would move with the needs' relative price even with no delay, so the cost of a delay could not be read from it. Fixed in compassionism-simulation `3e345eb` (v5.9.18, pull request 154; guard test identical, lineage link recorded, a unit test added).
2. **The essentials price response θ is swept.** θ (housing 0.6, medical care 0.5, food 0) is an unsourced engine value. It sets the essentials' price rise in every programme run and scales housing's above-needs give-up in the supply limit (`m·η·θ·e`). Research rule 3 asks that it be swept.

| Part | Rows | Count |
|---|---|---|
| Th | θ for housing and medical care at half (0.3, 0.25) and double (1.2, 1.0) the engine's own, food 0. At each: the programme run at shares 0-1, and the sourced limit × 3 rules × shares 0-0.75. | 34 |

The no-programme run is shared: its supply path is its own demand, so no essentials price moves in it (check 10). *Analysis:* at each θ, the programme's effect on the four primary outcomes at every share, base and sourced; the change the sourced limit makes against the base row at the same θ; the break-even shares. *Decision rule:* every statement that a result holds under the sourced reading also says whether it holds at half and at double θ. θ stays a design parameter, labelled wherever it is shown.

3. **"The slowest building speed at which a result holds" (Amendment 3, analysis item 2), defined for any pattern.** It is the smallest λ on the grid from which the test passes at that λ and at every larger λ on the grid. If the test passes at some λ and fails at a larger one, the whole pattern is reported instead, and the result is said not to hold steadily in the building speed.

**Units, stated** (the reading's item 5 was not confirmed, but the wording can be clearer). Every term of section A is a share of sector k's own no-programme needs consumption: `e`, `eu`, `v_k`, `m_k`, `c_k` and `r_k`. `e` is the same proportional excess in every sector, because the extra need is spread over the sectors in the basket's proportions (a stated limit). `R_k` is applied to each household's own spending on sector k.

**The job:** 231 rows (rows 0-196 keep their numbers). `--check` confirms the counts. `--selftest` adds check 10: θ at the engine's own values given explicitly equals the base row; doubled, it moves the programme run and leaves the no-programme run unchanged.

**Cost:** 231 rows × 3 environments × 500 seeds, at the dry run's rate (recorded below).

### The dry run and the dispatch (Nov 18, 2026, before the batch)

**The engine is pinned** at compassionism-simulation `eb0969cc56615d3c268c7a9dd17951be0b8d3d37`, the merge of pull request 154 (v5.9.18; CI green). Its tree is identical to `3e345eb`, the commit the dry run ran on (the diff between the two is empty). The job is compassionism-sim-results `runner/jobs/s82.js` at `4881a84` (pull request 53).

**The dry run.** `node runner/jobs/s82.js --dry --seeds=1-2 --procs=4` on the session machine (4 cores; Node 22.23.5, where the workflow uses 22.22.0) ran every environment and horizon: 1,386 rows (231 × 6), in 599 s.
- No output is missing or non-finite.
- The engine checkout was clean, and the release start's baseline check passed in every run.
- The job's `--selftest` (checks 1-10) passed on the same commit.
- Processor time per seed for all 231 rows: about 127 s at 20 years and 240 s at 40, in each environment. The batch is therefore about 153 core-hours.
- An earlier dry run (197 rows, on `ef15c3e`, before the fix of Amendment 4) printed its timings only.

*Seen in it* (no decision read from it): what a month of the BU buys at the needs' price, in the base row at no backing. It is the same in both seeds and at every θ (1,788 Year-0 dollars), and it falls to about 975 with the two-year delay, as the fix intends.

**The dispatch** (the `run-study` workflow of compassionism-sim-results, `prereg/RUNNING.md`; engine `eb0969cc56615d3c268c7a9dd17951be0b8d3d37`; each shard 4 vCPU; seeds are paired, so the cut changes no figure):

| Study (folder `<study>-eb0969c`) | Job | Job arguments | Seeds | Shards |
|---|---|---|---|---|
| s82-v6-ref-20 | s82.js | `--env=ref --years=20 --procs=4` | 1-500 | 20 |
| s82-v6-adv-20 | s82.js | `--env=adv --years=20 --procs=4` | 1-500 | 20 |
| s82-v6-str-20 | s82.js | `--env=str --years=20 --procs=4` | 1-500 | 20 |
| s82-v6-ref-40 | s82.js | `--env=ref --years=40 --procs=4` | 1-500 | 20 |
| s82-v6-adv-40 | s82.js | `--env=adv --years=40 --procs=4` | 1-500 | 20 |
| s82-v6-str-40 | s82.js | `--env=str --years=40 --procs=4` | 1-500 | 20 |
| s82-screen-s-str | s70-screen.js | `--block=S --env=str --procs=4` | 1-40 | 20 |
| s82-screen-ft | s70-screen.js | `--block=FT --env=all --procs=4` | 1-40 | 20 |
| s82-screen-f-str | s70-screen.js | `--block=F --env=str --procs=4` | 1-40 | 20 |

At the dry run's rate, a batch shard runs about 13 minutes at 20 years and 25 minutes at 40 years (25 seeds), well inside the workflow's 350-minute limit. S70's screen shards took 14-34 minutes. Each folder gets `run.txt`, `SHA256SUMS` and `DONE` from the workflow's last job. The batch is run once, as frozen here.

### Amendment 5 (Nov 18, 2026, after the first batch was read and before any result was reported): a defect in the design's sharing rule, fixed; the batch rerun

**What was read, in order.** The nine folders on engine `eb0969c` were complete (`DONE`, `SHA256SUMS` matching). The checks were read first: the job's `--selftest` (checks 1-10) passed again on the pinned commit, and the batch's own rows passed checks 2-4 in all 500 seeds of every environment and horizon (the full reading equals the base row at share 0; the strict bound equals the main row at share 1 with each rule; the no-programme run is unchanged by the wage readings), with every value finite and every run reading the same seed's no-programme median. Then the tables of questions 1 to 6 were read, made by `dev/tools/s82_tables.py` (compassionism-simulation; written before any table was printed), and the screen's three blocks by S70's tool (question 7).

**The defect.** Under the design's sharing rule (`sh` 'bu': basics bought with the BU are served first), the realised cut was two to four times its target under the sourced and restricted readings. For example, Reference, 20 years, share 0.5: target 0.15% of housing and 1.32% of medical care and food; realised 2.25% of all three, against 0.57% under the market and even rules. One seed traced year by year cut 31.4% of demand against a 5.35% target in one year and 0.32% against 4.6% the next. The cause: the rule divided this year's cut by last year's totals of spending and of the part bought with cash, and that cash share swings from year to year (for medical care: 1.8%, 33.5%, 4.0%, 24.4%, ...). After a year with a low cash share, all of this year's cash spending was cut. The market rule's normaliser is a ratio of ranks, which is stable, and the even rule has none; both realise their targets within a few per cent. Amendment 1 (item 3) reads section A as "summing to about the sector's cut, the realised share reported". The design's rule did not do that, so its rows did not measure the preregistered rule. No preregistered check tests the realised cut against the target; the defect was found by inspecting it.

**The fix** (compassionism-simulation v5.9.19; decisions in `dev/DECISIONS.md`, "S82 part 3"). Under the design's rule only, the year's poverty accounting, which allocates the cut, is queued and run once the year's flows are done and before any of the year's readers, with this year's totals. The sector's cut is then exact: if the households' cash spending on the sector covers the cut, it is shared in proportion to each one's cash spending; otherwise all cash spending is cut and the rest falls on BU spending in proportion. The poverty accounting reads only its arguments and fields set earlier in the same year, so nothing else moves. The market and even rules are untouched.
- Guard test identical; a unit test added: the design's rule and the even rule now realise the same total cut, as both cut each sector's share exactly, while cutting different households.
- Full-output comparison on the fixed engine: every one of the 231 rows at seeds 1-2 (Reference, 20 years; `node runner/jobs/s82.js --env=ref --years=20 --seeds=1-2 --procs=2`) against the first batch's stored values for the same seeds. 179 rows are identical in every key; the 52 that moved are exactly the design's rule's rows below full backing. In them the realised cut now equals the even rule's to the stored 7 digits (for example 11.92036% and 12.58079% at the strict bound, share 0, seeds 1 and 2).
- The fix was decided on the realised cut against its target, a quantity of the mechanism, before any outcome under the fixed rule was seen. A 2-seed check after the fix printed the realised cuts and basket poverty for the three rules (sourced at shares 0 and 0.5, strict at share 0 and 0.5). Under the fixed rule, basket poverty is close to the even rule's. Nothing in the design, the rows or the rules was changed after seeing it.

**Decision rule 1, applied.** The defect is fixed and the whole batch (231 rows × 3 environments × 2 horizons, seeds 1-500) is rerun on the new engine commit, with the job unchanged (`runner/jobs/s82.js` at `4881a84`). Only the rerun is reported. The first batch's folders `s82-v6-<env>-<years>-eb0969c` stay in compassionism-sim-results, as everything does (research rule 2), marked superseded by this amendment; no figure is quoted from them.
- **Check 11, added for the rerun:** every row except the design's rule's rows below full backing equals the first batch's stored value in every key and seed. That is 179 of the 231 rows. The other 52 are the design's rule's rows below full backing (A 12, X 12, Slam 16, Sgrid 4, Th 8). At full backing nothing is cut, and the queue keeps the order in which households are accounted, so the design's rule's share-1 check row is identical too. Check 11 shows the fix moved only what it was meant to. **Check 12:** under the design's rule, the realised cut equals the even rule's at the same reading, share and seed, to the stored digits. Both checks are in `dev/tools/s82_tables.py` (`--first eb0969c`).
- **The screen (question 7) is not rerun.** Its runs set no supply limit, so the fix cannot reach them: the queue exists only under the design's rule, and every run without it is identical (guard test, check 11). Its analysis on `eb0969c` stands.

**Seen while inspecting, outside S82's design** (recorded, not acted on here):
1. The swing in the cash share comes from the BU's relief to the cost of living, which runs a damped two-year cycle even in the main row (full backing, flat prices; Reference, seed 1, mean per adult: $22,838 in years 0-1, then $10,969, $21,452, $13,819, $19,472, $16,202). The BU paid per month holds its real value (`s82BuR20` is the same in every row without a delay). This is in every programme row and predates S82. It is listed as its own inspection step in PLAN.md.
2. The realised cut (`slCutSh`) averages the cuts applied in years 0 to T−1, and year 0 has none. The target (`slR*`) averages the targets set at the ends of years 0 to T−1, and the last of them is for a year never run. So a rule that cuts its target exactly shows a realised share of about (T−1)/T of the target's mean: 12.25% against 12.88% at the strict bound, share 0, 20 years. The report says so beside both.

**The rerun's dispatch** (Nov 18, 2026, 10:39 UTC; run-study runs 137-142). The engine is pinned at compassionism-simulation `aa2a4e0c5b4a2b425596f4728051bd2d3cbcbdde`, the merge of pull request 156 (v5.9.19; CI green). Its engine files equal the tested head `bd384db`; the merge also carries pull request 157's tools. The job is unchanged (`runner/jobs/s82.js` at `4881a84`). The six lines are the dispatch table's first six, with the new engine: `s82-v6-<env>-<years>` with `--env=<env> --years=<years> --procs=4`, seeds 1-500, 20 shards. Results land in `s82-v6-<env>-<years>-aa2a4e0/`. The rerun is read with `python3 dev/tools/s82_tables.py <results> <out> --engine aa2a4e0 --first eb0969c`; checks 11 and 12 must pass before any table is read.
