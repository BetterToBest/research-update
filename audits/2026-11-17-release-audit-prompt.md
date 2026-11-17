# Audit prompt: the Compassionism Simulation's release (v5.9.9), second outside round

Written Nov 17, 2026 (S13, second pass, part 1). Paste everything below the line into an AI system that can read web pages: one copy into **Grok**, one into **ChatGPT or Gemini**. Before pasting, replace the line that starts "Your role" with the role given here for that system, so the two replies cover different ground:

- **Grok:** `Your role: a sceptical macroeconomist who expects the headline results to be artefacts of the model's assumptions. Spend most of your effort on parts B and C.`
- **ChatGPT or Gemini:** `Your role: a statistician and research-methods reviewer who checks whether each published sentence follows from the evidence behind it. Spend most of your effort on parts A, D and E.`

Turn on the system's deepest research or browsing mode. Expected time: 30 to 90 minutes. Bring each full reply back into a fresh Claude Code session started with `/start-session S13` and say which system wrote it (S13 part 2 for the first reply, part 3 for the second, or both together). Do not edit the replies.

A third reading can come from a model on NVIDIA's free API catalogue, which cannot browse: the S13 part 2 session builds it a packet of these files instead (see `audits/2026-11-17-nvidia-setup.md`).

Pinned versions: compassionism-simulation `1d50b19` (v5.9.9, main on Nov 17), compassionism-sim-results `c732c7f`, research-update `a703175`. The links below point at `main`; if a file has moved, use the pinned commit.

---

You are auditing the current release of an open simulation of an economic policy. Be direct: say what is wrong, unsupported or misleading, not only what is good. Where you are unsure, say so. Do not assume the results favour the policy. The author advocates for the policy and wants the published work to stand up to critical economists. The model has never been reviewed by an independent economist; you are one of the first outside readers of this release.

Your role: [REPLACE THIS LINE, see the note above the line]

**Please open the files.** For every finding, name the file and section you read. If you could not open a file, say so and do not guess its contents. At the end, list every file you actually opened.

## What the model is

The Compassionism Simulation (author of the policy design: Duke Johnson; math and code written by Claude, an AI model) follows 500 simulated US working-age adults (25 to 64) and their children for 20 or 40 years, in three environments (Reference; Adverse, with recessions, automation and 2% outside inflation; Stress, the same with weaker settings and 40% take-up). Each seed is run twice on the same random draws, once with no programme and once with the programme, and results are means over 500 paired seeds with 95% paired-bootstrap intervals. A 10,000-adult main pair checks hours and the top tail. Today's US safety net is in both runs.

The design pays a monthly Basic Unit (BU) from an issuing body called the Source, and sets up not-for-profit essentials businesses (PTFs, PTH for housing) that accept BU and sell at cost. Two designs are studied: **full coverage** (BU automatic, enough for food, housing and medical care; built to meet a criterion called C2.2) and the **opt-in design** ($1,200 a month).

The release has two parts shown side by side: **release 1** (the v5.6 model) and **release 2** (the v5.9 model, frozen Nov 14 and run Nov 14-15; patch releases up to v5.9.9 since then changed displays, added reporting keys and re-checked stored results, not the main row). Release 2 added, each behind its own switch and preregistered: open access to PTFs and growth of their share; PTF running costs; adults outside the labour force and yearly movement in and out of work; a borrowing limit; wealth held by asset class (homes, shares, businesses, deposits, debts) with returns and a creditor side; a weighted Pareto top tail; a reduced-form bargaining channel; a government account; a capacity price rule (as a reading, not the main row).

**The single most important assumption.** Release 2's main row assumes that every dollar the programme pays is matched by new output (full backing). The author states this as part of the design; the project labels it a design parameter, not a model estimate. The model's own mechanism for new output matches 0.2-1.9% of the payout (14-20% with no ceiling). At full backing, programme inflation is 0.0-0.2 points a year; at the model's own mechanism, 15-53 points a year. Inflation stays under 5% a year only above about 86-90% backing.

### Headline results of release 2 (Reference, 20 years; range across 62 preregistered readings, main row in brackets with its seed interval)

- Basket poverty (adult-years below a cost-of-living basket): full coverage −25.9 to −33.3 points (−32.4 [−32.2, −32.5]); opt-in −16.2 to −22.3 (−20.9).
- Below 30 days of basic living: full coverage −16.5 to −19.7 (−18.7); opt-in −10.7 to −13.0 (−12.3).
- Wealth poverty (adults with wealth under $25,000 in year-0 prices, yearly average): full coverage −15.7 to −19.7 (−18.6); opt-in −9.0 to −12.7 (−10.9).
- Median real wealth at year 20: full coverage +$187,600 to +$659,600 (+$208,400; $432,300 against $223,900); opt-in +$84,600 to +$282,100 (+$99,400). Under 3% of any wealth figure is erosion of opening balances.
- Paid for by a contribution instead of the Source (never led with): full coverage needs 63-77% of all money income and lowers basket poverty by at most 17.5 points (Stress: +0.6, worse); the opt-in design at 46-71% of wages raises basket poverty by up to 9.6 points; 46 of 48 financed poverty and wealth curves are fragile across readings.
- Unfavourable: labour's share of income down 11.7 to 30.5 points; participation down 1-5 points; less movement out of the lowest wealth fifth; the opt-in design loses about two thirds of each effect in Stress.

Release 1 (v5.6) reported, among other things, that median real wealth *fell* by about 80% under the programme, because all wealth was held as cash under 30-45% inflation. Release 2 reverses that sign. Part of the reversal is the asset-class model; part is full backing (no inflation to erode anything).

### Files (please read the reports, not only this summary)

Simulation repository: https://github.com/BetterToBest/compassionism-simulation (raw files: `https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/<path>`)

- Release 2 overview and the seven question reports: `dev/reports/s64-round2-overview.md`, `s64-round2-q1-main-effects.md`, `s64-round2-q2-robustness.md`, `s64-round2-q3-interactions.md`, `s64-round2-q4-backing.md`, `s64-round2-q5-financed.md`, `s64-round2-q6-distribution.md`, `s64-round2-q7-work.md` (all in `dev/reports/`)
- The findings-page wording and its rules: `dev/reports/s64-findings-page-text.md`; the live page: https://bettertobest.github.io/compassionism-simulation/findings.html
- Model description: `MODEL_SPEC.md` (section 14 is release 2), `ODD.md`, `TESTBED_SPEC.md` (section 7 gives every row option a plain name)
- Checks of the model: `dev/reports/s68-round2-spec-tests.md` (switches on together, run-order test), `dev/reports/s69-independent-implementation/REPORT.md` (a second program written in Python from the spec), `dev/reports/s70-screen.md` (all readings moved together, Morris method)
- Mechanism reports: `dev/reports/s59-asset-classes.md`, `s59-tail-returns.md`, `s67-price-rule-derivation.md`, `s71-creditor-side.md`, `s72-government-budget.md`, `s73-participation.md`, `s60-bargaining-power.md`, `s62-ptf-realism.md`, `s55-open-access.md`; later readings `s74-central-bank.md`, `s75-deep-history.md`, `s79-r2-measures.md`, `s81-suite-weighted.md`
- Release data: `data/releases/r2/` (`study-20.json`, `study-40.json`, `suite-20.json`, `suite-40.json`, `index.json`); tables `dev/runs/s64-round2/`
- The economist checklist: `ECONOMIST-REVIEW.md`

Preregistrations and earlier audits: https://github.com/BetterToBest/research-update (raw: `https://raw.githubusercontent.com/BetterToBest/research-update/main/<path>`)
- The release 2 freeze: `prereg/2026-11-s63-round2-freeze.md` (questions, readings, decision rules, amendments)
- The audit of Nov 9 (its eight findings are part A below): `audits/2026-11-09-simulation-audit.md`; the follow-up audit of Nov 13: `audits/2026-11-13-simulation-audit.md`; backing and the main row: `audits/2026-11-14-d23-backing-and-main-row.md`; figures check of Nov 15: `audits/2026-11-15-release-figures-audit.md`

Per-seed results, one folder per study (`r2-<part>-<environment>-<years>-104691f/` for release 2, each with `run.txt` and `SHA256SUMS`): https://github.com/BetterToBest/compassionism-sim-results

## What to review

Answer every part; your role decides where you go deepest. Cite outside evidence with links.

**A. The Nov 9 audit's eight findings, checked against this release**

The Nov 9 audit (written by the same kind of AI system that built the model, so not independent) listed eight findings. For each, say whether this release **closes** it, **partly closes** it or leaves it **open**, with the evidence, and whether the published wording respects what remains open.

1. Wealth was one nominal number, so 30-45% modelled inflation decided every wealth outcome. (Release 2 adds asset classes, returns, a creditor side, and assumes full backing.)
2. The capacity price rule's long-run pass-through was built in, its speed not identified, its cycle an artefact. (Release 2 keeps the earlier one-for-one rule as the main row and carries the capacity rule as a reading.)
3. Round 2 was undocumented and had no independent check. (MODEL_SPEC section 14 and the S69 second implementation now exist. Check what S69 actually checked: its report says its packet ran at a backed share of 0, while the main row is at full backing.)
4. Switches were tested alone and state leaked between runs. (S68's on-together tests and run-order test.)
5. Seed intervals are not the uncertainty. (Release 2 leads with the range across 62 preregistered readings, a specification curve, and the S70 screen. Is the set of 62 readings a fair sample of the real uncertainty, or is it narrow by construction?)
6. The most defensible favourable result (a financed row) was not on the main rows. (Release 2 carries financed rows beside the main rows, and they are much weaker.)
7. Clarity: README, "agent-based" versus "dynamic microsimulation", two-letter option keys, a newcomer cannot tell what is current.
8. Process: the builder, preregistrar, analyst and triager are the same AI system; suggested OSF registration of the freeze; "not yet reviewed by an independent economist" on every page.

**B. Full backing, and what the headline then means**

1. The headline poverty and wealth effects, and the near-zero inflation, are computed at full backing, which the project labels a design statement. Is it legitimate to present results at an assumed 100% backing as the main row, with the backing curve beside it? What does the evidence on supply responses to large demand injections (cash-transfer programmes, wartime mobilisation, pandemic stimulus, monetary financing episodes) say about how much new output a transfer of this size could plausibly call forth, and how fast?
2. The poverty effects barely depend on backing; inflation and median wealth do (question 4's report). Is that plausible, or a sign that the price level does not feed back into real outcomes as it should (for example, if the basket and the BU are both indexed to the same price level)?
3. Suggest wording for the headline cards and the one-sentence answer that a sceptical economist would accept, and say whether the required card footnote ("every dollar the programme pays is matched by new output, as the design states ... The model's own mechanism for new output reaches about 1% of that") is enough.

**C. The model's mechanisms**

1. Median real wealth rises by $208,400 at the main row and by up to $659,600 across readings. Which mechanisms produce that (asset returns, PTF prices at cost, the BU saved, debt relief, the top tail), and is any of them implausible at this size? What would you check in the per-seed files to decompose it?
2. The price rule at the main row is one-for-one pass-through of unbacked new money. With full backing there is no unbacked money, so the rule is never tested at the main row. Is that a problem for the claim that results "rest on today's price rule"?
3. Labour's share of income falls 11.7 to 30.5 points. The Nov 9 audit warned that "labour's share" in a model with little capital income is wages over household money income. Is the published name and figure fair?
4. Participation falls 1-5 points. Is the participation margin (`lf.pm` 0.43: the share of each worker's income effect taken as leaving work rather than fewer hours; chosen as the reading that passes a check against a US cash-transfer experiment's interval, −7.5 to −0.9 points, with −1.3 points modelled against the experiment's −4.2) consistent with the evidence (for example Vivalt et al., the OpenResearch unconditional cash study, the Alaska Permanent Fund, the Finnish experiment)?
5. Wealth poverty falls 15.7 to 19.7 points. At full backing, how is most of that achieved: the BU itself, savings from PTF prices, asset returns? Is the $25,000 line in year-0 prices a sensible measure over 20 to 40 years?
6. The financed rows need contributions of 46-77% of income. Are the government account, the debt rule and the contribution bases (`gv`, `fx.fin`) built in a way an economist would accept? Is "debt stays under GDP at the main financed rows" a fair summary?

**D. Statistics and robustness**

1. The specification curve covers 62 preregistered readings chosen by the same system that built the model, using the S70 screen (12 Morris paths, 40 seeds, Reference and Adverse only, at full backing). Does the screen justify which readings were carried and which were dropped? Is Stress, which was not screened, adequately covered?
2. 500 adults, 500 seeds: are 500 adults enough for distribution measures, fifths, mobility and top shares (with the weighted tail of about 18 adults)? S81 found that one average, days from savings, was wrong in kind when unweighted (701,913 unweighted against 11,003 weighted; median 2,630). Are other published figures at risk of the same problem?
3. Holm correction across 60 primary tests, materiality thresholds, "robust" meaning every reading keeps its sign with an interval excluding zero: are these appropriate, and is anything reported as robust that is robust only by construction?
4. Does the release's results trail hold: preregistration committed before the run, amendments dated, every outcome published (including nulls and the Adverse and Stress environments), `run.txt` and `SHA256SUMS` beside each result? Spot-check at least one release 2 folder against `data/releases/r2/study-20.json` if you can.

**E. Fair presentation**

1. Read the live findings page and `s64-findings-page-text.md`. Which statements can be made as results, which only as model outputs under named assumptions, and which should not be claimed? Quote any sentence you think is misleading, in either direction, and propose a replacement.
2. Release 1 and release 2 reach opposite conclusions on median real wealth. Is the page clear about which to believe, and why?
3. What should a one-paragraph press summary of this release say, if it must be accurate and must not overclaim?

## How to answer

- Start with a short summary: the three most serious problems and the three most useful improvements.
- Then part A as a table: finding, status (closed / partly closed / open), evidence, what remains.
- Then numbered findings for parts B to E, each with an ID (B1, B2, ...), **severity** (A: blocks a published claim; B: fix before the next release or before the Hub uses the figure; C: worth doing later), **what is wrong or missing**, **evidence** (a quote with its file and section, or an outside source with a link), **a specific fix**, and **your confidence** (high, medium, low).
- Then a ranked list of improvements to the model, each with the data it needs and a rough size of the work.
- End with what you could not check and why, and the list of files you opened.
