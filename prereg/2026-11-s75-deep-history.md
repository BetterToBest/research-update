# Preregistration: deep history: US policy eras and their stability (S75)

Committed Nov 16, 2026 by S75 (part 1), before any panel figure is computed and before any engine change or run. Engine: compassionism-simulation at commit `3de028e2f0fd1198b218b3c873479e6819a0efa1` (main; S74's engine `a60ecd1` plus later merges). The only era figures seen before this file are the ones quoted in PLAN.md's S75 text (from the planning chat, not yet checked) and S74's 2005-2025 paths (S74's report).

## Why
Duke's view (planning chat, Nov 13): 2005-2025 was less stable than the decades before it, and earlier eras had different policy settings worth comparing (much higher statutory top tax rates in the 1950s; health care financed mostly through non-profit hospitals and plans before managed care grew after the HMO Act of 1973). The record is mixed and the study must show it either way: the 1970s and early 1980s had the postwar period's highest inflation and two deep recessions; 1984-2007 is usually called the Great Moderation. The study has two parts: a descriptive panel of the eras from published data (no engine), and engine readings that put today's households under each era's measured settings.

## Plain-words summary
- Four eras are fixed now, before any figure: 1947-1972, 1973-1983, 1984-2007 and 2008-2025, with 1913-1946 as a reading where the data reach. S74's window, 2005-2025, is shown beside them.
- The panel describes each era: how much prices, essentials, jobs, home and share prices swung; who held income and wealth; poverty; health spending; tax rates actually paid by each income group; and how the central bank set its rate. It describes; it does not say which policy caused which outcome.
- The engine readings ask a narrower question: how would today's households fare, without and with the programme, under each era's measured settings? That is a model counterfactual, labelled as such, not a reconstruction of the era.
- "Less stable" is said on a measure only where a 95% interval excludes zero. A mixed result is reported as mixed.

## Questions
- Q1 (panel). On each stability measure below, was 2008-2025 (and 2005-2025) less stable than 1947-1972 and than 1984-2007? How did 1973-1983 compare with each?
- Q2 (panel). How did the eras' policy settings differ: effective tax rates by income group, top income and wealth shares, health spending and its ownership mix, and the central bank's rule as estimated in each era?
- Q3 (engine). Without the programme, do today's households fare steadier under an earlier era's measured settings than under 2008-2025's? Which setting (the era's macro path, its estimated central-bank rule, its tax schedule, its health cost growth) moves it, inside the model?
- Q4 (engine). Does the programme's effect on household stability (S74's P1-P5) keep its direction under every era's settings, for both designs?

## Eras (fixed now)
- E1 1947-1972 (postwar; fixed exchange rates to 1971). E2 1973-1983 (oil shocks, stagflation, the Volcker tightening). E3 1984-2007. E4 2008-2025. Reading only: E0 1913-1946 (two world wars, the Depression; data from 1913 where the series reach). S74's window W 2005-2025 is shown beside E4 (it overlaps E3 by three years).
- A year belongs to the era that holds it. Yearly changes are December over December (the fourth quarter for quarterly series), as S74; a year's change is assigned to the later year (1947's is December 1946 to December 1947).
- 2025: where a series' 2025 is incomplete, the figure is what the file holds, flagged (as S74). Nothing is filled in.

## Sources to open (opened before use, research rule 3; each kept in the repository with its SHA-256 and the date downloaded)
- FRED (St. Louis Fed): CPI-U (CPIAUCSL from 1947; CPIAUCNS from 1913), CPI food (CPIUFDSL), food at home (CUSR0000SAF11), shelter (CUSR0000SAH1), medical care (CPIMEDSL), unemployment (UNRATE), CBO's noncyclical rate (NROU), real and potential GDP (GDPC1, GDPPOT), population (for per-person figures), the federal funds rate (FEDFUNDS from July 1954), the 3-month bill (TB3MS), the 30-year mortgage rate (MORTGAGE30US from 1971), NBER recession months (USREC). S74's raw files are reused where they already hold these.
- Shiller's online data: the S&P composite real price and CPI from 1871 (already in the repository, `sources/s59_shiller/ie_data.xls`), and his real home price index (Irrational Exuberance, Figure 3.1 file, from 1890).
- Piketty, Saez and Zucman's US distributional national accounts (the latest appendix file opened): top 1% and top 10% shares of pre-tax national income and of wealth, and average tax rates (all taxes, as a share of pre-tax income) by income group (bottom 50%, middle 40%, top 10%, top 1%, top 0.1%). The planning figures (about 42% of income in all taxes for the top 1% and 50.6% for the top 0.1% in the 1950s, against 36.4% and 39.8% in 2014) are checked against the file and reported as found.
- The Historical SCF (Kuhn, Schularick and Steins, SCF+, from 1949), if its file opens: the top 10% wealth share and the bottom half's share by survey year, beside PSZ.
- Jordà, Schularick and Taylor's Macrohistory database (rates of return on housing, equity, bills and bonds, US): a cross-check of Shiller's real returns by era.
- Census historical poverty tables (official rate, people, from 1959) and the Columbia historical and anchored SPM (from 1967), both already in `sources/history/`.
- CMS national health expenditure (from 1960): spending's share of GDP, real spending per person, and out-of-pocket spending's share.
- Hospital ownership mix (non-profit, for-profit, government) by year: from an opened source with counts (AHA Hospital Statistics, Health, United States, or the Historical Statistics of the United States). If none opens on this machine, the gap is stated and the file is asked for (as with BLS's R-CPI-I in S74); nothing is estimated in its place.
- NBER business cycle dates, for the recession count and the months in recession.

## Part A: the descriptive panel (no engine)
Built by one script in compassionism-simulation (`sources/s75_eras.py`, writing `sources/s75_eras.json` and a table), from the raw files only.

Stability measures (Q1), per era:
- A1. Inflation (CPI-U): mean and standard deviation of the yearly change; the worst year (highest); years above 5%; years of falling prices.
- A2. Essentials prices: the same for food (food at home where it reaches, CPI food before), shelter (from 1953) and medical care, and each one's mean yearly change relative to CPI-U.
- A3. Jobs: mean and standard deviation of the yearly unemployment rate; its highest year; the share of months in NBER recession; the number of recessions that start in the era.
- A4. Growth: mean and standard deviation of real GDP per person's yearly growth; the worst year.
- A5. Real share prices (Shiller, monthly) and real home prices (Shiller, yearly): the largest fall from peak to trough with both inside the era; the months or years until the earlier peak is regained (which may run past the era); the standard deviation of the yearly real change.

Policy and distribution measures (Q2), per era (start, end, change in points, mean):
- B1. Top 1% and top 10% shares of pre-tax national income and of wealth (PSZ); SCF+ beside them where it opens.
- B2. Poverty: the official rate (from 1959) and the anchored SPM (from 1967): mean, change, highest year.
- B3. Health: spending's share of GDP, real spending per person's growth, the out-of-pocket share (from 1960); medical prices' growth relative to CPI-U; the ownership mix where an opened source gives it.
- B4. Effective tax rates (PSZ average rates, all taxes) by income group: era mean and change. The top statutory rate is shown beside them only as context, with the plain statement that it applied to few incomes.
- B5. The central bank's rule as estimated in the era. Quarterly ordinary least squares: `i = c + φ π + β gap`, where i is the federal funds rate's quarterly average (the 3-month bill before the third quarter of 1954; in E4, the Wu-Xia shadow rate in quarters at the floor, as S74), π is CPI-U's change over four quarters, and gap is 100 × (real GDP / CBO's potential − 1). Newey-West standard errors, 4 lags. In S74's terms, a = φ − 1 and b = β. A smoothed version (`i = ρ i(−1) + (1 − ρ)(c + φ π + β gap)`, non-linear least squares) is a reading beside it. These are descriptive fits, not structural rules; published estimates (for example Clarida, Galí and Gertler 2000; Taylor 1999) are set beside them where opened.

Analysis (panel):
- Era comparisons of a mean or a standard deviation (A1-A4, the yearly-change spread in A5): the difference between two eras with a 95% interval from a moving-block bootstrap of each era's yearly values (block 3 years, 10,000 replicates, seed 75, each era resampled on its own).
- Drawdowns (A5) and the distribution measures (B) are single paths: they are described, with no interval.
- Holm's correction across the A1-A4 comparisons within each pair of eras.

Decision rules (panel):
- "2008-2025 was less stable than era X on measure M": the Holm-adjusted interval of (2008-2025 minus X) excludes zero in the less-stable direction (higher mean inflation, unemployment or spread; lower mean growth). "More stable": the same, the other way. Otherwise "no clear difference". The same is said for 2005-2025.
- Duke's view ("2005-2025 was less stable than the decades before it") is reported per measure against 1947-1972, 1973-1983 and 1984-2007 together: "supported on M" where 2005-2025 is less stable than all three; "against it on M" where it is more stable than at least one with none the other way; otherwise "mixed". The tally is given, with every cell. No overall verdict is formed by weighting measures.
- A planning figure that the opened file does not match is reported as such, with the file's figure.

## Part B: engine readings (part 2; built behind switches off by default; off = identical)
- Environment: S74's history environment (`hx`) gains era paths (option, for example `hx.era` 'e1'-'e4'), each running the era's length (26, 11, 24 and 18 years). Each year's path is built from the opened files exactly as S74's (outside inflation CPI-U; real home and share gains; the year's policy rate; the 30-year mortgage rate; recession flags by S74's rule: any NBER recession month or an unemployment gap of 2 points or more; the output gap). Where a series does not reach back, the substitute is fixed in Amendment 1 before any engine run and labelled a modelling assumption (expected: the 3-month bill as the policy rate before July 1954; the long-term rate plus a fixed spread for the mortgage rate before 1971; Shiller's home index before Case-Shiller; real median family income for the recession income multiplier, which S74 read from household income, not available before 1967).
- Population and rows: today's population (500 adults, the 2022-based start), seeds 1-100, the frozen round-2 main row, both designs (C2.2 and the release design), each paired with a no-programme run on the same seeds. The session machine (free).
- Arms, per era (each paired on seeds, and the same seeds across eras):
  - P "path": the era's macro path, the actual rate path, the central bank off (S74's actual-rate arm).
  - R "path + the era's rule": the S74 rule (`cb`, forced sales on) with the era's estimated a, b and intercept (B5) in place of S74's main values.
  - S "path + S74's rule": `cb` at S74's main values (today's rule in every era).
  - T "path + the era's tax schedule": each household's average tax rate changes by its income group's PSZ average rate in the era minus the latest PSZ year's (bottom 50%, middle 40%, next 9%, top 1%; groups by the run's own income ranking each year). Main: the change is revenue-neutral (the net returned or charged equally per adult), so it changes the schedule's shape, not the size of the state, which the engine does not model; reading: not returned.
  - H "path + the era's health cost growth": the basket's medical line grows in real terms at the era's mean (medical CPI minus CPI-U) each year.
  - A "all": R, T and H together.
  The build's exact mechanics (how T and H enter the engine) are written in Amendment 1 after the build and before any engine run, as S74 did.
- Outcomes (engine): S74's P1-P5 (definitions unchanged), plus basket poverty (`fgt0PY`) and wealth poverty (yearly average and last year) as secondary. Because the eras differ in length, P3 (largest fall in real wealth) is also read over each era's first 11 years.
- Analysis (engine): paired differences over seeds with 95% intervals (paired t; a paired bootstrap of 2,000 replicates for P3 and P5), Holm across P1-P5 within each era, arm and design.
- Decision rules (engine):
  - Q3: "today's households, without the programme, fare steadier under era X's settings (arm) than under 2008-2025's (same arm)" on an outcome: the Holm-adjusted paired interval excludes zero in the steadier direction. Which setting matters is read from arms P, R, T and H against each other, inside the model only.
  - Q4: "the programme's effect keeps its direction in era X" on an outcome: the Holm interval excludes zero in the same direction as in S74's History (arm S); "no measurable difference" and "reversed" are said as found.
- Unit tests: off identical (guard test; `hx` without `era` gives S74's History bit for bit); each era's built paths equal the JSON; arm T with every group's change at zero equals arm P exactly; arm H with a zero real medical growth equals arm P exactly; eight draws per agent-year; no non-finite output; the account identities hold.
- Results: compassionism-sim-results `s75-eras-<engine commit, 7 chars>` with `run.txt` and `SHA256SUMS`; the panel's tables and JSON also go there (`s75-panel-<commit>`).

## Reporting
- A report in plain words (compassionism-simulation `dev/reports/s75-deep-history.md`) with every cell above, the mixed and unfavourable ones included (research rule 2).
- **A separate Hub page** (Duke's instruction, Nov 16, 2026): the study's findings get their own page on the Research Hub, named by Claude, linked from the simulation page and the wiki page once it is complete. Readings also go to the Hub's history section and to NEEC.
- Duke's note (planning chat, Nov 13) is stated on that page as the design's aim, in his words: 2005-2025 was marked by war and corruption; Compassionism is meant as a way past war, with stability and prosperity as goals instead of exploitation and extraction. The model does not represent war, military spending or corruption, and no figure is claimed about them.

## Limits stated in advance
- Each era differs from the others in many ways at once: the US's postwar position, union membership, demography, fixed exchange rates, wars, the size of government, finance's rules. The panel describes and does not attribute stability to any one policy. The engine readings isolate only the settings they change, inside the model.
- The 1950s' top statutory rate (91-92%) applied to few incomes; the panel uses the rates actually paid (PSZ), not statutory rates.
- For-profit insurance and hospitals existed before 1973. The HMO Act of 1973 promoted HMOs and opened the way for for-profit ones; it did not make health profit legal. The ownership mix is shown as found.
- An era's estimated rule is a fitted summary of how the rate moved with inflation and the gap; in E1 and E2 it may break the Taylor principle (φ below 1). The engine has no expectations channel, so it cannot show the instability that such a rule is thought to cause; this is said wherever R is read.
- Era samples are short (11-26 years); intervals will be wide, and "no clear difference" is the expected reading on many measures.
- The engine readings keep today's population, prices of today's basket and today's institutions apart from the setting changed.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first panel figure is computed or the first engine run.
