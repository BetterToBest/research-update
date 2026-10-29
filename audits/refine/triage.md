# refine.ink audit triage (S29)

Oct 29, 2026. I checked the 145 refine.ink comments (A01-A13 on the mechanism-design paper, B001-B132 on the Oct 10, 2025 compendium) against the live Research Hub at research-hub commit `8a72c68`. Every comment has a row in `triage.csv`. `recompute.py` reruns each arithmetic point: 64 checks, all of which run clean. `triage.py <research-hub checkout>` rebuilds the CSV and the lists below.

## How each comment was judged

- **Where the passage is now.** `presence_check.py` searches every Hub page, PDF and data file for the passage each comment quotes. Where the locator missed, I searched by hand. I also fixed the script: it used to treat a bare "<" (as in "p* < 0.05") as the start of an HTML tag, which hid text on several pages. I also corrected ten locators that missed or matched the wrong passage.
- **Whether the critique is right.** For live passages I read the passage on the HTML page. Where the HTML page has been rewritten since the PDF was built, I judged the HTML text.
- **Classes.** Hub: *live* (on a live page or data file), *pdf* (changed on the HTML page but still in that paper's PDF), *gone*. Verdict: *valid*, *partly valid* (the critique is right but the audit's own explanation or fix is wrong), *wrong*, *moot* (gone, or nothing to fix). Severity: *headline* (a figure stated as a result in an abstract, summary or headline), *derivation* (a derivation, a table or a model statement in a paper body), *wording*.

## Summary

| | Count |
|---|---|
| Comments | 145 |
| Live on the Hub | 99 |
| Changed on the HTML page, still in the PDF | 36 |
| Gone from the Hub | 10 |
| Valid | 124 |
| Partly valid | 5 |
| Wrong | 0 |
| Moot | 16 |
| **Valid or partly valid and live** | **96**: 30 headline, 23 derivation, 43 wording |
| Valid, PDF only | 33 (fixed by rebuilding the PDFs) |

The audit holds up: none of its critiques is wrong. Where it goes wrong is in some of its explanations and proposed reconciliations, which it sometimes supplies on the paper's behalf without any support in the text:

- **B097** (NPV $1,847). The paper's printed formula gives $2,046. The audit's explanation (growth starting in year 2) gives $1,832, so neither matches $1,847. The audit also writes "$2.04 million" where it means $2,046.
- **B053** (poverty "below 5% within 15 years"). The audit says the path "passes through 5% on its way" to the steady state. It does not: with a steady state of 11.8%, the rate falls toward 11.8% and never reaches 5%. The paper's 15-year formula only works if poverty starts at 82%.
- **B093** ($82,000 listed as an input). The audit excuses this as a "calibration target", but the file never says so. Its header calls the values "optimal parameters".
- **B017, B095, B036, B075, B016, B083.** The audit reconciles each inconsistency with an assumption the paper does not state: a cost ramp, a 60% net credit, "rigorously defined" indices, two separate wealth metrics, two definitions of viability, and a stock reading of B_i. The inconsistencies themselves are real. The reconciliations are the audit's guesses.

## What the recomputation found (`recompute.py`)

- **Confirmed paper errors.** The paper's figures do not follow from its own printed inputs in all of these:
  - poverty steady state 0.118 and 0.074, against a theorem that says below 0.05 (B001);
  - elasticities, every row about half its arc elasticity: -1.60, -2.04, -1.20, -0.57, -0.38 (B002);
  - $4,616B, not $1.52T (B009);
  - multiplier 1.95, not 2.86 (B025, B050);
  - $3T is 11% of 2023 GDP, not 14% (B032);
  - inflation 51-61% lower, not 65% (B033, B061);
  - half-life 3.72 years, not 4.1 (B031);
  - budget items sum to $12.0B, not $12.5B (B030), and to $8.8B, not $8.5B (B017);
  - $390B, not $385B (B094);
  - 13 points, not 15 (B103, B127);
  - earn-in timelines 4-40 times slower than the stated rates imply (B010);
  - the buy-in pathway grows 2.67x while the other pathways double (B079);
  - no weighting of the carbon components gives the 45% total (B062);
  - V(n) is convex everywhere, so it cannot show diminishing returns (B023);
  - the stability index is not unit-free (B076).
- **The avalanche example (B005).** None of the five mortgages amortizes at its stated payment over its stated term. With the table's own payments and no extra money, pooling them pays everything off in 18.3 years and saves about $900 in interest. The paper says 10 years and "$85,000+".
- **Drug-policy net values (B044).** No single pair of dollar values for a prevented death and a prevented incarceration-year produces both scenarios' net social values. Solving for a common pair gives about $7.2M per death and a *negative* $363,000 per incarceration-year. The HTML table also differs from the PDF: the integrated scenario's cost is now $786B (PDF $450B) and its net value $5.0T (PDF $4.7T).
- **External figures (B028 Portugal, B011 Bristol Pound).** On the audit's quoted figures, deaths fell 85%, not 95%. £5 billion through about 2,000 individual users is £2.5M per person, which is implausible. Both sources are to be opened in S23 (research rule 5) before the text is corrected.

## Overlap with the corrections already drafted

The session-5 package (`audits/corrections-package-s5.md`, C23-C30) already corrects the research-summary blurbs for B003/B009/B018 ($1.52T, $847B: C23), B066 ($70,000: C24), B097 ($1,847: C25) and B005 ($85,000: C26). The paper bodies (abstracts, conclusions, tables) still carry those figures and need the same corrections. The new items are in `audits/corrections-additions.md`. The main package (C01-C22) is not in these repositories, so S24 should merge both files.

## For later steps

- **S23 (claims ledger).** Every *headline* row here is a figure S23 must class. Most of them have no run behind them: B002, B048, B062, B071, B075, B084, A05, A08. The `S29 id` column in `data/claims.csv` should cite these ids.
- **S30.** B093 ($82,000, an input reported as a result) and B055 (the housing regression, no estimate published).
- **S46 (formal model).** A01, A04/B035/B070 (Lemma 2), A06 (Lemma 1), B001/B053 (convergence theorem), B013, B019, B067, B108.
- **S24.** The 36 PDF-only rows go away when each PDF is rebuilt from its current HTML page. A new finding from this pass: the HTML pages of optimal-transfer-design and dual-currency-inflation are rewrites, not lightly edited copies of their PDFs. optimal-transfer-design's sec 6.2 states "E[W_20] = $68,500 (95% CI: [$52,000, $85,000])", and dual-currency-inflation gives the same claim as "$1,850" (sec 5.2) and "$1,760" (conclusion) monthly UBI equivalent. Both are for S23.

<!-- generated by triage.py: everything below this line is rewritten on each run -->

## Valid and live: changes a headline figure (30)

| Id | Page | Correction needed |
|---|---|---|
| A01 | optimal-transfer-design.html | The HTML (sec 9) still says 'mathematical analysis confirms Pareto improvements' but no longer contains a proof; the PDF's proof assumes c_CCO >= c_TRAD for everyone. Restate as a conjecture, or state the condition (B0 at least the traditional transfer) under which it holds (S46). |
| B001 | community-monetary-development.html | community-monetary-development sec 3.3: the theorem says p* < 0.05, the proof gives 0.118 and 0.074 (recompute.py). Restate the theorem with the computed steady states (S46). |
| B003 | drug-policy-reform.html, dual-currency-inflation.html, papers/index.html ... | $847B: already C23 (retire in the summary). The paper body (abstract, conclusion) also needs it: it is one line of Scenario 2, not the integrated net. |
| B004 | pth-government-integration.html | pth-government-integration 3.1: $12-20B a year of 'community wealth' on a $12.5B one-time outlay (96-160% a year) has no derivation. Derive or label as an illustrative projection. |
| B005 | pth-independent-financing.html | pth-independent-financing 2.2-2.3: the payments do not amortize the stated balances; with the table's own payments the avalanche takes 18.3 years and saves about $900, not 10 years and $85,000+ (recompute.py). C26 retires $85,000 in the summary; the paper body needs the same. |
| B009 | drug-policy-reform.html | drug-policy-reform abstract/sec 1: $1.52T vs the table's $4,616B (recompute.py). Already C23 for the summary; the paper body needs it too. |
| B016 | cco-ptf-integrated-framework.html | 30% viability (cco-ptf-integrated-framework) vs 55% minimum (economic-modeling-simulation). The audit's reconciliation (two definitions) is its own guess, not in either paper. One threshold, from a run: S5. |
| B018 | drug-policy-reform.html | drug-policy-reform abstract: $847B 'net societal savings' vs the HTML table's net social value of $5.0T (PDF: $4.7T). Same fix as B003/C23. |
| B022 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework 5.4: 'proves optimal' with no criterion and no published sweep. Restate as design choices; a sweep is S32's job. |
| B026 | community-monetary-development.html | community-monetary-development 7.2: break-even year 4-5 vs year 6 and ROI 250% without derivation. Derive or label as illustrative. |
| B028 | drug-policy-reform.html | drug-policy-reform 2.2: Portugal 'deaths fell by 95%', 'crime dropped by 50%'; the audit reads Greenwald as 131 -> 20 deaths (85%) and the 50% as prisoners held on drug charges. Open Greenwald (2009) in S23 and correct. |
| B033 | dual-currency-inflation.html | dual-currency-inflation conclusion: '65% lower inflation' is in no table: the PDF's Table 5.2 gives 51-54% (total) or 78-86% (excess); the HTML's 5.2 states 65% with no UBI comparison (recompute.py). Correct or remove; S23. |
| B036 (partly) | economic-modeling-simulation.html | economic-modeling-simulation 11.2: +41% engagement, +67% innovation have no formula or interval. 4.x names the outcome categories ('community engagement metrics'; 'patents, startups, cultural output') but gives no formula; the audit's 'rigorously defined ... weighted index' overstates it. Label as illustrative or remove (S23). |
| B044 | drug-policy-reform.html | drug-policy-reform 9.1: no single set of dollar values for deaths and incarceration-years gives both net values (one needs a negative value per incarceration-year; recompute.py). Publish the valuation or remove the net figures. |
| B048 | economic-modeling-simulation.html | economic-modeling-simulation 6.1: ABM effects (23%, 31%, 41%) with no interval and no published run. Label as illustrative or remove (S23). |
| B052 | pth-government-integration.html | pth-government-integration abstract: '2.5x greater efficiency' is the wealth-building column; with the 40% cost cut it would be 4.2x (recompute.py). Name the metric. |
| B053 | community-monetary-development.html, papers/index.html, research-summary.html | community-monetary-development abstract and the research summary: 'below 5% within 15 years'. With p* = 11.8% the rate never reaches 5%; the 15-year formula implies a start rate of 82% (recompute.py). The audit's 'passes through 5%' is also wrong. Remove (S23). |
| B058 | democratic-governance-pth.html | democratic-governance-pth 8.1: cooperative vs HOA statistics have no source. Cite or remove (S23). |
| B061 | dual-currency-inflation.html | dual-currency-inflation abstract: '65% lower'. See B033 (56-61% for CCO+PTF in the PDF table; recompute.py). |
| B062 | economic-modeling-simulation.html | economic-modeling-simulation 9.x: -45% total from -31/-18/-24/-19: no weighting gives 45% (a weighted average is at most 31%, compounding gives 65%; recompute.py). Show the weights or remove. |
| B066 | - | $70,000 over 20 years (us-real-estate-transformation, corporate-transformation, integrated-digital-governance 'target') vs $57,600 in 5 years (pth-independent-financing) and $70-140k in 10 years (pth-government-integration PDF). C24 restates the summary; say which figure is which scenario in each paper. |
| B071 | economic-modeling-simulation.html | economic-modeling-simulation 8.1/8.3: 2.8% productivity vs 3.5% GDP growth with no bridge; neither comes from a published run. Label as illustrative (S23). |
| B075 (partly) | economic-modeling-simulation.html, integrated-digital-governance.html | economic-modeling-simulation and integrated-digital-governance: 'wealth effects 180% higher' vs 122% in 5.1. The audit's reconciliation (median flow vs 25-year average) is its own reading. No run produced either: S23/S30. |
| B084 | drug-policy-reform.html | drug-policy-reform conclusion: '100,000 preventable deaths, 500,000 unnecessary incarcerations' a year, not in the body. Source or remove (S23). |
| B093 | data/optimal-parameters.json | data/optimal-parameters.json: median_wealth_accumulation 82,000 sits among inputs, and the papers report $82,000 as a result with a 95% CI. The audit's rescue ('calibration target') is not in the file; its header says 'optimal parameters'. Traced in S30. |
| B096 | pth-government-integration.html | pth-government-integration abstract: see B052. |
| B097 (partly) | community-monetary-development.html, papers/index.html, research-summary.html | community-monetary-development 4.2: NPV $1,847 vs $2,046 from the printed formula. The audit's explanation gives $1,832, and its '$2.04 million' should be $2,046 (recompute.py). Already C25 for the summary ('ROI'); the paper body needs the same. |
| B098 | economic-modeling-simulation.html | economic-modeling-simulation: '85% poverty reduction' is the share of scenarios reaching < 2%. Say so where 85% appears (abstracts, cco-ptf-integrated-framework). |
| B103 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework discussion: 85% -> 98% is 13 points, not 15 (recompute.py). |
| B127 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework: second '15 percentage point' (recompute.py). See B103. |

## Valid and live: changes a derivation or table (23)

| Id | Page | Correction needed |
|---|---|---|
| A04 | dual-currency-inflation.html, optimal-transfer-design.html | Lemma 2 (optimal-transfer-design and dual-currency-inflation) is a one-market argument with p, D, S undefined. Name the market and the conditions, or call it a sector-level result (S46). |
| A06 | optimal-transfer-design.html | Lemma 1 claims strict monotonicity; with the cap (HTML: min(B, Cap)) it is only weakly increasing, and the lemma's B0*2^O*R is not the HTML model's M(q)*min(B, Cap). Restate for the HTML model (S46). |
| B002 | economic-modeling-simulation.html | economic-modeling-simulation Table 5.4: every elasticity is about half the arc elasticity of its own row (-1.60, -2.04, -1.20, -0.57, -0.38; recompute.py). Recompute or drop the column; no run produced the table (S30). |
| B007 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework 3.4: the example (ratio 3 -> 3x) needs alpha = 1 if Base Rate = 1, or alpha = 0 if Base Rate = 3, not 0.3-0.5 (recompute.py). Define the variables and fix the example. |
| B008 | drug-policy-reform.html, economic-modeling-simulation.html | economic-modeling-simulation 11.3: $2.1T (stock plus five years of flows) sits beside annual costs. Split or footnote. |
| B010 | pth-independent-financing.html | pth-independent-financing 5.4: at 200-1,000 credits a month, 100 credits take under a month, not 2-4 months (recompute.py). Fix the rates or the timeline. |
| B012 | economic-modeling-simulation.html | economic-modeling-simulation phases: 73/85/95% and 89-97% not mapped to scenarios. Add a mapping table or label as targets. |
| B013 | dual-currency-inflation.html | dual-currency-inflation 3.x: budget identity has no source of P_t and P_convert's use is unstated. Complete it (S46). |
| B019 | economic-modeling-simulation.html | economic-modeling-simulation 3.1: u(c, l, s) has no functional form. State it (S46). |
| B023 | economic-modeling-simulation.html | economic-modeling-simulation 7.1: 'diminishing returns above 80%' while V(n) is convex everywhere (recompute.py). Add the cost term or drop the claim. |
| B030 | pth-government-integration.html | pth-government-integration 3.1: items sum to $12.0B, headline $12.5B (recompute.py). Add the missing $0.5B line or correct the headline. |
| B032 | dual-currency-inflation.html | dual-currency-inflation sec 1: $3T is about 11% of 2023 GDP, not 14% (recompute.py). Correct to 'about 11%' with the BEA source. |
| B034 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework: 'without reducing merchant income' needs alpha = 0 in the example (recompute.py). See B007. |
| B035 | optimal-transfer-design.html | Same as A04: call Lemma 2 a single-market result (S46). |
| B038 | pth-independent-financing.html | pth-independent-financing 9.2 vs 2.2: same five families, different principal, rate, payment and savings (recompute.py). Align with 2.2 or label as a separate example. |
| B045 | pth-independent-financing.html | pth-independent-financing 5.3: '$1,000-1,500 net improvement' needs a mortgage payment the example does not state. State the pre-sale costs. |
| B060 | pth-independent-financing.html | pth-independent-financing 9.3: 200 households -> '500+ served', $35M, with no growth assumptions. State them or label as illustrative. |
| B067 | dual-currency-inflation.html | dual-currency-inflation 3.2: no rule aggregating C_{i,j,t} into C_{i,t}. State it (S46). |
| B070 | optimal-transfer-design.html | Same as A04 and B035 (S46). |
| B072 | integrated-digital-governance.html | integrated-digital-governance 4.4: V(n) = 0.3n^2 + 0.7n log n is assumed, not derived. Label the weights as assumed (design parameter). |
| B076 | economic-modeling-simulation.html | economic-modeling-simulation Appendix A: Stability = 1 - Var/Mean is not unit-free (recompute.py). Use the coefficient of variation. |
| B079 | pth-government-integration.html | pth-government-integration 3.3-3.4: buy-in grows 2.67x while the others double (recompute.py). State why or correct. |
| B108 | integrated-digital-governance.html | integrated-digital-governance 4.3: g(C_k) undefined; say outflow is proportional to Z_k. |

## Valid and live: wording, labels and citations (43)

| Id | Page | Correction needed |
|---|---|---|
| A07 | economic-modeling-simulation.html, optimal-transfer-design.html | gamma is the leisure weight in the HTML utility (4.1) and risk aversion in Appendix A. Rename one. |
| A10 | optimal-transfer-design.html | Abstract: say in a clause how 'productive beauty' is judged (peer panels, sec 4.2). |
| A11 | optimal-transfer-design.html | Add one linking sentence per literature subsection (optional). |
| A13 | optimal-transfer-design.html | 'Eliminates benefit reduction entirely' -> 'eliminates income-based phase-outs'; conversions are still capped. |
| B015 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework 2.4: the phi bonus rests on non-mainstream sources. Present phi as a design parameter, not a derived optimum. |
| B020 | cultural-value-integration.html | cultural-value-integration: 'objective foundation' for phi vs peer panels. Say panels judge eligibility. |
| B021 | democratic-governance-pth.html, public-trust-financial.html | International precedents listed without the lesson drawn. One sentence each (optional). |
| B024 | cultural-value-integration.html | cultural-value-integration: say what 'no downward mobility' locks (octave) and what is reassessed (multiplier). |
| B042 | economic-modeling-simulation.html | economic-modeling-simulation Appendix A: 'conversion_rate' names two things. Rename the scenario key. |
| B043 | integrated-implementation-roadmap.html | The country comparison table is gone; 'Democratic Participation' is still an undefined KPI in integrated-implementation-roadmap Appendix I. Define it (turnout, CIP engagement). |
| B046 | pth-independent-financing.html | pth-independent-financing 7.2-7.3: say Phase 3 adds sell-in and earn-in. |
| B047 | dual-currency-inflation.html | dual-currency-inflation sec 1: the cited 0.1%/1% GDP implies about 1% at $3T (recompute.py). Explain why the paper still calls it significant. |
| B049 | cultural-value-integration.html | cultural-value-integration: 'save and trade expired basic units' vs expiry. Say what is saved: the conversion right. |
| B051 | integrated-digital-governance.html | integrated-digital-governance 2.2: OECD/UN frameworks do not 'validate' the architecture. Limit to the digital components. |
| B057 | risk-mitigation-framework.html | risk-mitigation-framework: say what the 50/75/100% conversion capacity is a share of. |
| B059 | democratic-governance-pth.html, integrated-digital-governance.html | democratic-governance-pth Appendix A: define 'Efficiency' in the matrix. |
| B063 | risk-mitigation-framework.html | risk-mitigation-framework: threat_matrix indexed by strings. Add a mapping or call it pseudo-code. |
| B073 | drug-policy-reform.html | drug-policy-reform conclusion: 85% is incarceration-years (38M of 45M), 69% is the rate (recompute.py). Label the metric. |
| B077 | risk-mitigation-framework.html | risk-mitigation-framework 12.2: say the class is a control-flow sketch and point to the sections. |
| B078 | democratic-governance-pth.html | democratic-governance-pth 3.2: say when square-footage weighting and when quadratic voting apply. |
| B080 | risk-mitigation-framework.html | risk-mitigation-framework: define x_cents (link the X-cents paper, S4). |
| B081 | democratic-governance-pth.html | democratic-governance-pth intro: soften 'not through compromise but through synergy' or point to sec 2. |
| B083 (partly) | integrated-digital-governance.html | integrated-digital-governance 4.1: W_CCO sums basic units and conversions; say whether B_i is a balance (stock). The audit's reading is plausible, not stated in the paper. |
| B089 | risk-mitigation-framework.html | risk-mitigation-framework conclusion: 'research demonstrates ridicule can be more effective' needs a citation. |
| B090 | democratic-governance-pth.html | democratic-governance-pth: say who oversees opt-in programs for non-members. |
| B091 | cultural-value-integration.html | cultural-value-integration: 'Theorem 1' is an eligibility rule. Rename to Rule or Definition. |
| B100 | democratic-governance-pth.html | democratic-governance-pth 2.2: add one or two further studies on over-delegation (optional). |
| B104 | economic-modeling-simulation.html | economic-modeling-simulation 3.2: the Acre Equity function is in dollars; say how dollars become credits. |
| B105 | risk-mitigation-framework.html | risk-mitigation-framework: PTFSafeguards is invalid Python. Use literals. |
| B106 | risk-mitigation-framework.html | risk-mitigation-framework 3.5: say how Youth CCO Accounts resist parental coercion. |
| B107 | democratic-governance-pth.html | democratic-governance-pth: 'independent judiciary through elected grievance committees'. Reword. |
| B111 | basic-living-economic-index.html, economic-modeling-simulation.html, optimal-transfer-design.html | economic-modeling-simulation, optimal-transfer-design, basic-living-economic-index: Hoynes & Rothstein (2019) is a review; 'employing Monte Carlo methods' -> 'reviewing'. |
| B112 | economic-modeling-simulation.html | economic-modeling-simulation 3.1: index the sum (i in M_k) and use a superscript. |
| B113 | economic-modeling-simulation.html | economic-modeling-simulation Appendix A: 'poverty_elimination' filled with poverty_rate. Rename. |
| B116 | papers/index.html, pth-independent-financing.html | pth-independent-financing abstract: 'break-even in 6-12 months' needs the $500K-1M seed capital in the same sentence. |
| B117 | pth-independent-financing.html | pth-independent-financing 4.1: say the $400,000 is non-acquisition support. |
| B118 | cco-ptf-integrated-framework.html | cco-ptf-integrated-framework abstract: '2^n' vs 2^(n-1); say where counting starts. |
| B119 | risk-mitigation-framework.html | risk-mitigation-framework evolution table: '50% cost reduction' target has no reference. Label as a target. |
| B120 | economic-modeling-simulation.html | economic-modeling-simulation: point to where calculate_outcome is defined (it is not on the Hub; cco-ptf-simulation-replication.html now redirects to the engine's replication page). |
| B125 | pth-government-integration.html, pth-independent-financing.html | pth-government-integration and pth-independent-financing: NotebookLM credited with the Acre Equity 'conceptual framework' while Duke conceived it. Reword the acknowledgment. |
| B128 | optimal-transfer-design.html | optimal-transfer-design Appendix B: say O is the octave index here. |
| B129 | democratic-governance-pth.html | democratic-governance-pth abstract: 'strong evidence' for an untried system. Say 'suggestive precedents'. |
| B131 | cultural-value-integration.html | cultural-value-integration: freelancer projected outcomes (45%, 32%, 58%, 67%) have no source. Label as illustrative. |

## Changed on the HTML page, still in the PDF (36)

These need no new text: rebuilding each PDF from its current HTML page (S24) removes them.

| Id | PDF | Verdict | Note |
|---|---|---|---|
| A02 | optimal-transfer-design.pdf | valid | PDF only: first-order conditions mis-stated (ratio inverted, sign dropped; p(quality|h) undefined). The HTML model replaced them; rebuild the PDF. |
| A03 | optimal-transfer-design.pdf | valid | PDF only: budget constraint adds B0 and P_convert from the same units. The HTML model splits basic units (min(B, Cap)); rebuild the PDF. |
| A05 | optimal-transfer-design.pdf | valid | PDF only: table promises standard errors it does not show and does not say which parameter moves. Rebuild the PDF from the HTML; no run produced these numbers (S23/S30). |
| A08 | community-monetary-development.html, dual-currency-inflation.html | valid | PDF only: welfare decomposition 0.42/0.28/0.18/0.12 has no method and no run behind it. Gone from the HTML; rebuild the PDF; S23 classes it 'no basis'. |
| A09 | economic-modeling-simulation.html, optimal-transfer-design.html | moot | PDF only: the HTML model no longer uses delta for a housing share. Rebuild the PDF. |
| A12 | optimal-transfer-design.pdf | valid | PDF only: R_i used for both the multiplier and 'reciprocal relationships'. Rebuild the PDF. |
| B006 | dual-currency-inflation.pdf | valid | PDF only: Welfare Index table (142 vs 138) is gone from the HTML. Rebuild the PDF. |
| B011 | cco-ptf-integrated-framework.pdf | valid | PDF only (cco-ptf-integrated-framework): Bristol Pound 'GBP 5 billion' (GBP 2.5M per participant; recompute.py). The HTML no longer gives the figure. Rebuild the PDF; S23 opens the source. |
| B014 | dual-currency-inflation.pdf | valid | PDF only: the code caps the converted amount, the formula caps the octave. Rebuild the PDF; S46 states one rule. |
| B017 | integrated-digital-governance.pdf | valid | PDF only: items sum to $8.8B, total says $8.5B (recompute.py); the audit's ramp is not in the paper. The HTML has a new budget table; rebuild the PDF. |
| B025 | economic-modeling-simulation.pdf | valid | PDF only (economic-modeling-simulation): multiplier 2.86 vs 1.95 from the printed formula (recompute.py). Gone from the HTML; rebuild the PDF; check summaries for 2.86 (none found). |
| B027 | cco-ptf-integrated-framework.pdf | valid | PDF only: O is a dollar amount in Equation 1 and an index in Lemma 1. Rebuild the PDF; the HTML uses n. |
| B031 | community-monetary-development.pdf | valid | PDF only (community-monetary-development): half-life 4.1 vs 3.72 from the printed formula (recompute.py). Gone from the HTML; rebuild the PDF. |
| B037 | economic-modeling-simulation.pdf | valid | PDF only: participation_rate uniform(0.6, 0.95) vs beta(3, 2). The HTML snippet uses uniform(0.55, 0.95); Appendix A should match it. Rebuild the PDF. |
| B039 | dual-currency-inflation.pdf | valid | PDF only: R_i and f() undefined in the conversion line. Rebuild the PDF. |
| B040 | dual-currency-inflation.pdf | valid | PDF only: '1.3% annual' is the year-1 increment over baseline (recompute.py). Rebuild the PDF. |
| B041 | cco-ptf-integrated-framework.pdf | valid | PDF only: PTF '15% of local activity' has no tax base. Rebuild the PDF; S46 names the base. |
| B050 | economic-modeling-simulation.pdf | valid | PDF only: second instance of 2.86 (economic-modeling-simulation PDF). See B025. |
| B054 | community-monetary-development.pdf | valid | PDF only: policy bullets without signposts. Rebuild the PDF. |
| B055 | dual-currency-inflation.pdf | valid | PDF only: PTF_Supply undefined in the housing regression. Rebuild the PDF; no estimate is published (S30). |
| B056 | dual-currency-inflation.pdf | partly valid | PDF only: Delta M_B is ambiguous (the audit concedes it may be correct). Rebuild the PDF. |
| B068 | dual-currency-inflation.pdf | valid | PDF only: 'expiration creates natural velocity ceiling' (expiry raises velocity). Rebuild the PDF. |
| B069 | cco-ptf-integrated-framework.pdf | valid | PDF only: exchange-rate models cited but not used. Rebuild the PDF. |
| B074 | cco-ptf-integrated-framework.pdf | valid | PDF only: '68% of participants advance an octave a year' (cco-ptf-integrated-framework PDF); no run. Rebuild the PDF; S23. |
| B085 | us-real-estate-transformation.pdf | valid | PDF only (us-real-estate-transformation): Acre Equity in credits vs dollars. Rebuild the PDF; the HTML should say dollar figures are reference values. |
| B086 | - | moot | HTML fixed: '2.5 jobs per unit' is only in the public-trust-financial PDF. Rebuild the PDF. |
| B088 | pth-government-integration.pdf | valid | PDF only (pth-government-integration): 'wealth built $70,000-140,000' in 10 years. Rebuild the PDF; see B066. |
| B092 | economic-modeling-simulation.pdf | valid | PDF only (economic-modeling-simulation): Gini decay formula vs the ABM. Rebuild the PDF. |
| B094 | drug-policy-reform.pdf | valid | PDF only (drug-policy-reform 5.1): $385B vs $390B by the paper's own method (recompute.py). The HTML 7.1 has new tables; rebuild the PDF. |
| B101 | pth-government-integration.pdf | valid | PDF only (pth-government-integration 6.2): 'time to scale' 2-5 years vs full scale in years 6-10. Rebuild the PDF. |
| B102 | - | moot | HTML fixed: Equation 2 (phi^Participation_Index) is only in the cco-ptf-integrated-framework PDF. Rebuild the PDF. |
| B109 | drug-policy-reform.pdf | valid | PDF only (drug-policy-reform): author order reversed. Rebuild the PDF; attribution per compassionism-simulation's CLAUDE.md. |
| B114 | integrated-digital-governance.pdf | valid | PDF only (integrated-digital-governance conclusion). Rebuild the PDF. |
| B115 | drug-policy-reform.pdf | valid | PDF only (drug-policy-reform 2.3). Rebuild the PDF. |
| B122 | drug-policy-reform.pdf | valid | PDF only (drug-policy-reform 5.2). Rebuild the PDF. |
| B126 | cco-ptf-integrated-framework.pdf | valid | PDF only: Ulanowicz phi vs golden phi. Rebuild the PDF. |

## Moot: gone from the Hub, or nothing to fix (13)

| Id | Note |
|---|---|
| B029 | Gone: the '$0-10,000' down payment row is no longer on the Hub (public-trust-financial PDF says $0). |
| B064 | Gone: the 0.41 baseline table is no longer on the Hub. |
| B065 | Gone: quality_assessment_accuracy is no longer in data/optimal-parameters.json. |
| B082 | Gone: '10-fold cross-validation' is no longer on the Hub. |
| B087 | Gone: the 20% pilot target is no longer on the Hub. |
| B095 | Gone: '$6,000-10,000/year' is no longer on the Hub (the audit's arithmetic, 6,720-13,440, is right; its '60% net' rescue is not in the paper). |
| B099 | The Hub serves each paper as its own page; the boundary problem was in the audit's merged export. |
| B110 | Gone: the $23,280 example is no longer on the Hub. |
| B121 | Gone: 'minimum viable: 75%' is no longer on the Hub (see B016 for the live 30% vs 55%). |
| B123 | Fixed: the references cite Johnson (2017) and the '2017, updated 2025' wording is gone. |
| B124 | Gone: the revenue bands the audit quotes are no longer on the Hub; the live bands (70-80% primary, 10-15% secondary) are coherent. |
| B130 | Each paper is its own page on the Hub; the abrupt transition was in the merged export. |
| B132 | Fixed: the strategy cell now reads 'Diversified participant base'. |
