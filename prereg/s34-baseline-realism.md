# Preregistration: the no-programme baseline against outside data (S34)

Committed Oct 30, 2026 by S34, before any run. Engine: compassionism-simulation at commit `fc6880ba71f0493550a284a247854719ca72d172` (main; release v5.6.0 plus page-only changes). The study tool and the outside-data script land on a branch from this commit; they add reporting code only (no engine line changes, so every released figure stays as it is).

## Why
Every result compares Compassionism with "no programme" on the same simulated people. The no-programme run is the yardstick. This study asks how far that yardstick is from the US today, on income, poverty, wealth, work and today's safety net, and lists each gap. It is a check of the yardstick, not a test of the programme: no programme row is run.

## Questions
- Q1. Income: how close are the no-programme run's earnings and household income (level, spread, Gini) to the Census Bureau's CPS ASEC 2026 (income year 2025), for adults aged 25-64?
- Q2. Official poverty: how close is the share of people below the official poverty line (adults; children; all people in the model's households) to the CPS ASEC 2026 official measure for the same ages?
- Q3. Wealth: how close are the median net worth, the share in debt and the share below the model's wealth line ($25,000 in year-0 prices) to the Federal Reserve's Survey of Consumer Finances 2025 (and 2022, which the model is calibrated to), for families with a head aged 25-64 and wage income, overall and by household type?
- Q4. Work: how close is the share of adults at work to BLS figures (CPS, 2025 annual averages: employment-population ratio, labour force participation and unemployment rate at 25-54) and to the ASEC 2026 share of adults 25-64 with earnings?
- Q5. Today's safety net: for six representative households, how close are the engine's yearly SNAP, EITC and refundable Child Tax Credit to PolicyEngine-US's for the same household, earnings, rent and childcare?
- Q6. Drift: how much do the model's figures in Q1-Q4 move between Year 0 and Year 20 (the last year), against the same outside figures?

An answer is each comparison's figure, model beside outside, with the gap and its class (Decision rules).

## Design
- Rows (no programme only):
  - **A. As released.** The release's no-programme run: `relMainCfgs(tbPresets(P))[0]` with `sc: SPEND_SOURCED` (households, SCF starting wealth, income-graded spending, the accounting corrections, the v5.4 parts: risk measure, job loss and unemployment insurance, PTH balance, PTF scale), run as the release runs it (NR6 profile, `TB_PROFILE_G`, `fin 'tax'`, v5.2 reporting).
  - **B. With today's safety net.** Row A plus SNAP, the EITC and the refundable CTC with SNAP's work rule and the slope reading (`sn: {abawd: true, slope: true}`), as in the v5.6 study.
- Environments: Reference is the primary comparison (no outside inflation, no recessions: the closest to a steady US year). Adverse and Stress are run and published as secondary (they add recessions, automation and 2% inflation; the outside data are one recent year, so a gap there partly reflects a recession year that the data do not contain).
- Seeds 1-500, paired across rows (common random numbers); 500 adults and their children; 20 years. "Year 0" is the first simulated year, "Year 20" the last (year index 19).
- Where: the session machine (no-programme runs are cheap; nothing paid). Command: `node dev/tools/baseline_realism.js ENV 500 20` for ENV in ref, adv, st; results in compassionism-sim-results, folder `s34-baseline-realism-<engine commit, 7 chars>`, with run.txt and SHA256SUMS.
- Outside figures: computed from public microdata by a committed script, `sources/baseline_realism_us.py` (CPS ASEC 2026 public-use CSV, Census Bureau; SCF 2025 and 2022 summary extracts, Federal Reserve; person weights `A_FNLWGT`/`MARSUPWT` as the Census documentation directs, SCF weight `WGT` over five implicates), and BLS series from FRED (LNS12300060, LNS11300060, LNS14000060; mean of the 2025 monthly values published). PolicyEngine-US (`pip install policyengine-us`, AGPL; version recorded) for Q5: tax year 2025 for the EITC and CTC, SNAP for the twelve months of 2025, a state with SNAP's 200% gross income limit and no state income tax (Florida), take-up not applied (the engine's take-up draws are set to "takes up" for this check).

## Outcomes
- **Primary (Reference, row A and row B, Year 0 and Year 20):**
  1. Median yearly earnings of adults with earnings (2025 dollars); 10th, 25th, 75th and 90th percentiles; Gini of earnings.
  2. Official poverty rate: adults 25-64, children under 18, all people in the model's household types.
  3. Median family net worth; share of families with net worth below $25,000; share in debt (net worth below zero); each overall and by the four household types.
  4. Share of working-age adult-years at work (model: 1 − weeks out of work / 52, everyone is in the labour force) against the employment-population ratio; out of work against the unemployment rate.
  5. For each of the six households: SNAP, EITC and refundable CTC, yearly dollars, engine and PolicyEngine.
- **Secondary:** Adverse and Stress (all of the above); household money income median and Gini (households with a head 25-64); SPM rate beside the model's Supplemental-style rate (definitions differ; reported, not classed); the safety-net rows' recipiency shares against USDA and IRS figures where the model reports them.
- Units: dollars are 2025 dollars (the model's year-0 dollars; later years deflated by the model's own price level, as released). Shares are % of people (or adult-years where stated). Model figures are means over the 500 seeds of each seed's statistic, with the 2.5th-97.5th percentile range over seeds. "Basket poverty and wealth poverty" are the model's own headline measures and are reported beside the official measure, not compared with outside data (no outside series measures them).

## Analysis
- Each comparison: model figure, outside figure, difference (model − outside) and ratio. Survey sampling error of the outside figure is stated where the source gives it or computed from the five SCF implicates and weights; it is small next to the gaps this study can act on.
- No intervals on programme effects: no programme is run. No synergy claims. No multiple-comparison correction: nothing here is a hypothesis test; it is a list of gaps.

## Decision rules
- A **gap** is: for a share, a difference above 3 percentage points; for a dollar level, a ratio outside 0.80-1.25; for a Gini, a difference above 0.03; for a safety-net amount, a difference above the larger of $100 a year and 5%.
- Each gap is classed: (a) **scope**, explained by a stated limit of the model (for example, everyone works, no one over 64); (b) **constant**, a constant that differs from a cited primary source: fixed only behind a switch, off by default, with the guard test passing, and its effect reported, never folded into released figures before the S7 release; (c) **open**, not explained this session: recorded for S32 and S47.
- No constant is changed to close a gap unless a cited source gives the new value (no tuning to a target). A gap that only a design change could close goes to the ledger as a decision.
- If the drift (Q6) between Year 0 and Year 20 is itself a gap on any primary outcome, it is reported as a property of the yardstick, with the reason where it can be traced.

## Reporting
Every cell above is published, including figures that match and gaps that remain, in `dev/reports/baseline-realism.md` (compassionism-simulation) and in compassionism-sim-results.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

**Oct 30, 2026 (before any run).** The labels of the two rows are corrected; their switches are unchanged. The v5.6 release panel was run with `--v54 --snab --slope` (the release data's `_meta.command` in `index.html`), so its no-programme run includes today's safety net with SNAP's work rule and the slope reading. Row **B** is therefore the released yardstick ("as released"), and row **A** is the same run without today's safety net (the v5.4 release's no-programme run, and the "no programme, no safety net" reference line). Primary outcomes are read on row B first; row A is reported beside it.

**Oct 30, 2026 (after the first Reference results of rows A and B, before any exploratory run at 500 seeds).** Exploratory rows are added, labelled exploratory: they were chosen after seeing the gaps, so they answer "what would close this gap", not the preregistered questions. (1) Wages read from the CPS ASEC 2026 earnings of adults 25-64: all earners (median $60,000, spread 0.737) and full-time, year-round workers ($70,000, 0.626), through the existing LATENT wage reading with new constants (`CFG.CPS_EARN`, off by default; guard test). Reason: the model's wage scale was set from the median personal income of everyone 15 and over, earners or not, while every model adult works full time. (2) The older SCF wage reading (`lt: {s: 1, m: 1}`). (3) Ageing on (`ag: {}`), with and without (1): without ageing, children never grow up, so childcare and child costs last all 20 years. Every exploratory row also has today's safety net (row B's switches). All three environments, 500 seeds. The gap rules above apply to them unchanged; none of them changes a released figure.
