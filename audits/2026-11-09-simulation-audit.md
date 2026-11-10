# Audit of the Compassionism Simulation before the round-2 freeze (Nov 9, 2026)

Asked for by Duke in Chat on Nov 9: audit the Simulation for clarity, rigour and technical issues, suggest improvements to the model, and add steps to the plan where they are needed. This note is the record. Plan changes it led to: PLAN.md steps S67-S70 and the amendments to S59, S63, S66 and S13; ledger decisions D21 and D22.

This audit was written by the same kind of AI system that built the engine. It is not the independent economist's review the project still lacks, and it should not be cited as one.

## What was checked, and how

- compassionism-simulation at commit `78e1dd7` (S58 merged): `node harness.js validate` passes; `node harness.js unit` passes (282 tests, 0 failed).
- Read in full: the S58, S57 and S61 reports; the price rule's code (`prStep`, `prRes`, `mfYear`), the distribution measures' code (`dmQuantiles`, `dmTail`, `dmMeasure`, `dmYear`), the labour-force scope code (`lfDraw`); `sources/s58_price_rule.py`, rerun on the committed FRED files (it reproduces the published values).
- Read by section: MODEL_SPEC.md (sections 2, 4, 5, 6.11-6.12), the S54 levers report, the handoffs, PLAN.md's round-2 sections, the ledger's open steps and archived decisions D11-D20.
- Not rerun: any 500-seed study, the guard test, domtest. Not read: most of the engine's 8,700 lines, the S55 code, the Hub pages. See the last section.

The project's own discipline is unusually good for work of this kind: switches with an identical-when-off proof, paired seeds, preregistration files committed before runs, nulls published, limits written into each report, two independent reimplementations of the release row. The findings below are about what that discipline does not yet cover.

## Summary

The three most important problems:

1. **Every real-wealth result measures one assumption more than it measures the programme.** Each adult holds wealth as a single number of dollars that earns nothing and is never revalued, while the programme's modelled inflation is 30-45% a year. Starting wealth is the SCF's net worth, most of which in the real economy is houses, shares and businesses that reprice with the price level. The fall in median real wealth, the halved wealth Gini, the vanishing debt, the fall in top shares and the rise in mobility all follow mainly from that (finding 1).
2. **The new price rule adds a cycle, not information, and its parameters do not come from the rule's own form.** Its long-run one-for-one pass-through is built in; its response speed is a Phillips-curve slope on the output gap applied to a different variable; its 9-year waves are the roots of its own difference equation; its parameters change sign between halves of the sample (finding 2).
3. **Round 2's main row will be a new model that nothing independent has checked.** Six or more mechanisms built in a few days, none in MODEL_SPEC.md or ODD.md, tested one at a time, with the second implementation still reproducing the old engine (findings 3 and 4).

The three most useful improvements:

1. Hold wealth by asset class (real assets, nominal assets, fixed and floating debt) in S59, so inflation moves real wealth only where it would (finding 1).
2. Carry the C2.2 design paid for by a contribution, the one setting in which the programme's inflation is near zero, on every round-2 outcome beside the main rows (finding 6; decision D21).
3. Show each headline as a range over every preregistered reading (a specification curve), with the seed interval inside it, and screen all round-2 parameters together before the freeze (finding 5).

## Findings

Severity: **A** blocks a published claim · **B** fix before the round-2 freeze (S63) · **C** worth doing later.

### 1. Wealth is one nominal number; under 30-45% inflation that assumption decides every wealth outcome (A)

**What the engine does.** `wealth += earnings − cost`, then `wealth −= share × max(0, cash surplus)` (MODEL_SPEC.md section 5, B10 and B16). No return, no revaluation. The spec's boundary row says so: no "interest rate, central bank, credit market (beyond a debt floor), land market or asset prices" (section 2). Starting wealth is each household's 2022 SCF net worth (section 6.13).

**Why it matters.** After 20 years at the C2.2 design's inflation the price level is about 400 times its start. A household that began with a $300,000 house and no cash is recorded as holding $300,000 of year-20 dollars, about $750 in year-0 dollars. In the economy that house would have repriced with everything else. The same arithmetic erases debts: a fixed nominal debt is inflated away with no creditor on the other side to lose it. So:

- median real wealth falls from about $212,000 to $41,000 (C2.2, Reference, audit prompt table);
- the wealth Gini falls from 0.73 to 0.35 and the top 10% share by 27-33 points (S57), because starting differences are wiped and what remains is a few recent years of saving;
- families in debt fall from 22% to under 1%;
- rank mobility rises, as S57's own report cautions, by compression.

The project's own results already show the dependence: savings that keep up with prices reverse the security findings (S53); the spending share alone (0.593 against 0.877) moves the programme's wealth-poverty effect by 18-50 points (S47); the year at which a wave is read moves it from −17.8 to +1.6 (S58).

**One sentence to correct.** S57's report says real wealth falls "because of its price level, not because wealth is destroyed". For the holder of nominal savings, wealth in real terms is destroyed: it is transferred to the issuer of the new money. The sentence should say that the model treats all wealth as nominal, and that this is an assumption (dated note, no figure changes).

**Fix (S59, amended).** Split starting net worth by SCF portfolio shares for the household's wealth group into real assets (housing, other real estate, corporate and business equity), nominal assets (deposits, bonds) and debts (fixed-rate, floating). Real assets move with the general price level plus a sourced real return; nominal assets earn a nominal rate that follows inflation with a sourced pass-through (0 is today's reading, 1 the full Fisher effect); fixed-rate debt keeps its nominal value. Report the programme's real-wealth effect in three parts: erosion of opening nominal balances, change in real saving, revaluation. Sources to open before use (named here from memory, not yet opened): the SCF 2022 public data and the Fed's Distributional Financial Accounts for portfolio shares by wealth group; Doepke and Schneider, "Inflation and the Redistribution of Nominal Wealth", *Journal of Political Economy* 2006, for nominal positions by group.

**Cheap first step (S66, amended).** On the frozen engine, reporting only: for each adult, how much of the gap in year-20 real wealth between the two runs is the erosion of the year-0 balance. That number says how much of every published wealth result is this assumption.

### 2. The capacity price rule (S58) (B)

Read against `prStep` and `sources/s58_price_rule.py`.

a. **One-for-one pass-through is built in.** The rule's state is a money-implied level `n` that grows by ln(1 + U/Y); each sector's log price closes part of the gap to it each year. With steady money growth m, any κ > 0 and α + ρ < 1, steady-state inflation equals m and the gap settles at (1 − α − ρ)m/κ. So "pass-through 0.96-1.04 in every reading" could not have come out otherwise under sustained money, and "the new rule agrees with that evidence" (report, item 2) and the proposed Hub sentence (section 8) present an assumption as a finding. The assumption is reasonable and McCandless and Weber support it; it should be named as one.

b. **κ is not estimated in the rule's own form.** The regression is annual CPI inflation on last year's inflation and last year's CBO *output gap* (realised output over potential, within ±9%). The rule applies that slope to x = n − p, the *cumulative* gap between money and prices, which starts above 0.3 and is a different variable. The empirical counterpart of the rule is the price-gap (P-star) form, in which inflation answers the gap between the money-implied price level and the actual one (Hallman, Porter and Small, *American Economic Review* 1991; named from memory, to be opened).

c. **The parameters are not stable.** Rerunning the script:

| Sample | Persistence | Slope above potential | Slope below | Two-sided slope |
|---|---|---|---|---|
| 1960-2024 (main) | 0.783 (0.073) | 0.445 (0.189) | 0.051 (0.147) | 0.213 (0.089) |
| 1960-1983 | 0.922 (0.101) | 0.282 (0.238) | 0.657 (0.244) | 0.466 (0.130) |
| 1984-2024 | 0.488 (0.153) | 0.615 (0.393) | −0.206 (0.176) | −0.000 (0.127) |

The asymmetry the rule depends on (0.445 above, 0.051 below) is about 1.6 standard errors wide, ignoring their covariance, and reverses in the first half of the sample. Standard errors are plain OLS with a lagged dependent variable; no correction for serial correlation.

d. **The waves are the rule's own roots.** With wage indexation and expectations both carrying last year's inflation (φ = α + ρ), inflation follows x_t = (1 + φ − κ)x_{t−1} − φx_{t−2} + κm. At the main values the roots are complex with modulus 0.885 and period 8.8 years; at ρ = 0.45, modulus 0.979 (almost undamped); at κ = 0.25 the period is 12 years, at κ = 1, 5.6. The report says the waves "follow from the rule's arithmetic"; the consequence is that a year-20 wealth reading under this rule is a reading of the wave's phase, set by an annual lag structure and unstable parameters.

e. **The regime is different.** The fit is on years with inflation under 15% and a central bank. At a sustained 35% a year, indexation periods shorten and people hold less money (Cagan 1956), so inflation can run ahead of money growth. No reading allows pass-through above 1 under sustained money.

f. **Smaller points.** The four "sectors" share one `n`, one κ, ρ and α and zero slack in the main reading, so they are identical apart from the essentials' own θ: the sector form is nominal. "Output answers first where there is slack" is a dead band on prices; nothing reported as output response (`prOut`) feeds back into incomes.

**Fix (new step S67).** Correct the wording by dated note; put the closed form in the spec; estimate the price-gap form on US data and the dynamics on high-inflation episodes; add a within-year price step as a reading (to see whether the waves and the 11-22% "shortage" survive a shorter lag) and a reading with rising velocity. Until then, this audit's advice for S63's main-row decision differs from the recommendation fixed in the S58 preregistration: keep today's rule as the main row (same long-run answer, no artefact cycle, one line to explain), the capacity rule beside it, and every wealth outcome as a yearly average under both. The reasons are about identification and form, not about which result looks better; S63 should put both views in the decision.

### 3. Round 2 is undocumented in the spec and outside the independent implementation (B)

MODEL_SPEC.md and ODD.md do not mention `PRICE_RULE` or `LF_SCOPE` (0 matches each); `PTF_ACCESS` appears once, in TESTBED_SPEC.md. The second implementation (`s50_release.py`) "reproduces the old engine, not the new one, until a new packet is built" (the Simulation's handoff). The guard test proves each switch changes nothing when off. Nothing independent says any of them is right when on. Release 1's row earned its standing through S10 and S50, which found 38 gaps and 8 contradictions; round 2's main row may differ from it in open access and growth, the price rule, scope, the debt reading, the tail, returns, bargaining and PTF running costs.

**Fix (new steps S68, S69).** Write round 2 into the spec with a plain-names table of the two-letter row options; then a fresh session writes a second implementation of the candidate main row from the spec alone, before the 500-seed run.

### 4. Switches are tested alone; state leaks between runs (B)

Each build step ends with "unit tests for each mechanism working alone". The handoffs already list cross-switch hazards found by accident: `lf` reuses the retired flag (`a._ret`), which produced a 0/0; a normal-years slack (`pr.h`) and the spending layer's slack (`ml.nt`) would use the same slack twice; and "a no-programme row's `pd*` keys read the previous run's PTF state", so the first study after a unit suite differs from later ones. The last is reporting-only today, but it shows the engine's module-level state (`PRS`, `LFS`, `DMS`, `DR_PL`, PTF capacity) is not reset per run, and a result that depends on what ran before it is not reproducible from its command line.

**Fix (in S68).** A run-order test (every row identical whatever ran before it in the process), a reset of module state at the start of each run, and pairwise on-together tests of the round-2 switches on the candidate main row: accounting identities, the eight-draws guarantee, no non-finite value.

### 5. Seed intervals are not the uncertainty (B)

The headline S55 wealth figure is "+2.42 points [2.40, 2.44]". The same outcome moves by 18-50 points with the spending share, by −17.8 to +1.6 with the price rule's readings, and disappears at a 25% demand ceiling. Five hundred paired seeds measure Monte Carlo error only; a reader shown the bracket will take it for the result's uncertainty. S63 already plans a structural-uncertainty section; a list is not enough. Round 2's sweeps are also one at a time, which cannot show interactions (for example the spending share with the price rule with asset classes).

**Fix (new step S70; S63 amended).** Screen every swept parameter together at reduced seeds (Morris elementary effects or a Latin hypercube; `dev/tools/gsa.js` may already do part of it) to rank what moves each headline. Preregister a specification curve as the main display: every preregistered reading of an outcome on one chart, ordered, seed intervals drawn inside. A headline sentence then gives the range across readings first.

### 6. The model's most defensible favourable result is not on the main rows (A, for what the Hub may claim)

The levers pilot (S54, 50 seeds, labelled pilot) found that no setting inside the design brings the programme's inflation under 21% a year, and that the C2.2 design paid for by a flat contribution on wages has inflation of 0.1 points a year, basket poverty down 18-29 points and wealth poverty down 18-28 in all three environments, failing one no-harm test (large income falls with no buffer rise by 1.4-5.2 per 100 adult-years). Duke's answer to D14 was no design change, and this audit does not reopen it. But round 2 as planned spends its effort measuring outcomes more finely inside the 30-45% regime, where findings 1 and 2 dominate. The financed row is the one place where the programme's effect on poverty and wealth can be read without the price rule or the nominal-wealth assumption in the way, and an economist will ask for it first, along with the contribution rate it needs.

**Fix (S63 amended; decision D21).** Carry "C2.2, paid for by a contribution" on every round-2 outcome and measure, as a labelled reading beside the main rows, printing the contribution rate and who pays. Whether the Hub may lead with it is Duke's call.

### 7. Clarity (C)

- The README describes the page as of v5.2.1 and "500 simulated adults"; it leads with the aspiration and "see how it does". The first screen should state, in two sentences, what the model finds on both sides: basic living improves; under the design's own financing prices rise 30-48% a year and savings lose most of their value.
- The model is called agent-based. Its adults do not interact except through one price level, the PTF share and shared pools; there are no firms or markets. "A dynamic microsimulation with a reduced-form price level" is the description an economist will recognise, and it sets the right expectations.
- Row options are two-letter keys (`pr`, `lf`, `pa`, `dm`, `mf`, `dr`, `fx`, `au`, `sc`, `cl`, `cm`, `lv`, `sx`); no one table maps them to plain names and to the section that defines them (S68).
- CHANGELOG.md is 416 KB, CONTRIBUTING.md 128 KB (and marked historical), the Simulation's HANDOFF.md 24 KB against a 45-line rule next door. A newcomer cannot tell what is current. One "start here" page with the model in a page, the current findings and the open limits would do more than another report.
- S57's "labour's share" is wages over household money income in a model with no capital income; its report says so. Do not carry the name to the findings page.

### 8. Process (C, but it bears on how results should be described)

- The builder, the preregistrar, the analyst and the triager of outside reviews are the same AI system, and the outside reviews were by AI systems too. Six mechanisms were preregistered, built, piloted and reported in two days. A preregistration written in the session that then runs the pilot protects against changing the analysis after seeing results (and the amendments after failed checks are disclosed, which is right); it does not give the distance a registry and a second person give.
- Suggested: register the S63 freeze on OSF (the project has a DOI there) before S64 dispatches; run S13's second audit in a session that did not build round 2 and is given only the spec, reports and results; keep the sentence "not yet reviewed by an independent economist" on every page until one has; and treat ECONOMIST-REVIEW.md rows 5 and 7 (the spending share and the price rule) as the first things to ask a reviewer, with finding 1 added as a row.

## Improvements to the model, ranked

| # | Improvement | Why it ranks here | Data | Size | Where |
|---|---|---|---|---|---|
| 1 | Wealth by asset class; real assets repriced; nominal rate follows inflation; debts by type | Decides every wealth outcome | SCF 2022, DFA | 2 sessions | S59 (amended) |
| 2 | The financed C2.2 row on every outcome | The cleanest reading of what the design does for people | none new | within S63-S64 | S63 (amended), D21 |
| 3 | Specification curve and joint screening | Honest uncertainty; a smaller batch | none | 1 session | S70, S63 |
| 4 | Price rule re-derived (price-gap form, high-inflation episodes, within-year step, velocity) | Removes an artefact from the main row | FRED M2, World Bank or IMF CPI and broad money | 1-2 sessions | S67 |
| 5 | Spec, cross-tests and a second implementation of the round-2 main row | The only independent check of "on" behaviour | none | 2-3 sessions | S68, S69 |
| 6 | Movement in and out of the labour force (yearly transitions instead of a status fixed for 20-40 years) | A student or carer fixed for the whole run overstates lasting exclusion; S61 lists it as a limit | CPS matched months or SIPP | 1 session | after S60, as a reading |
| 7 | Adults 65 and over at the start | Retirees hold the most nominal income and savings; inflation falls hardest on them | SCF, CPS | 1-2 sessions | later |
| 8 | A government budget line | Reconciles the conversion tax, today's safety net and any contribution (ECONOMIST-REVIEW.md row 13) | CBO | 1 session | later |

Not recommended now: a full firm and goods-market layer. It would be a different model, and findings 1, 2 and 6 can be answered without it.

## What could not be checked

- The S55 open-access and growth code, the S61 debt reading and most of the release engine were not read line by line. Finding 4's state leak is taken from the project's own handoff, not reproduced here.
- No 500-seed result was rerun; the figures quoted are the reports'.
- The closed form in finding 2d assumes wage indexation and basket inflation both equal last year's general inflation and steady money growth; the pilot's path (72% in year 4, 25% in year 9) matches it, but it is an approximation of the engine, not a proof about it.
- The sources named "from memory" were not opened in this audit. A build step must open each before using it (research rule 3).
- Whether study N (the levers study) ran at 500 seeds in the frozen batch and where its report is: not found in `dev/reports/`.
