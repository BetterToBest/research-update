#!/usr/bin/env python3
"""S29 triage of the refine.ink audit comments: adds Claude's judgments to triage.csv.

Usage: python3 triage.py <research-hub checkout>
  1. runs presence_check.py (where each quoted passage is now), then
  2. joins the judgments below and rewrites triage.csv with these columns:
     hub      live    = the passage (or the same claim) is on a live HTML page or data file
              pdf     = changed or removed on the HTML page, still in that paper's PDF
              gone    = no longer anywhere on the Hub
     verdict  valid / partly valid / wrong / moot (moot: the passage is gone, or there is nothing to fix)
     severity headline   = changes a figure stated as a result in an abstract, summary or headline
              derivation = changes a derivation, a table or a model statement in a paper body
              wording    = labels, definitions, cross-references, citations
     action   the correction needed (for pdf rows: rebuild the PDF from the HTML, S24)
Recomputed arithmetic is in recompute.py (the ids in the action text say "recompute.py").
"""
import csv, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent

# hub-state overrides where the locator matches a different passage than the audit's
HUB = {
    "A08": "pdf",   # "Direct transfers" also matches unrelated text; the 0.42/0.28/... decomposition is PDF-only
    "A09": "pdf",   # the HTML model no longer uses delta for a housing share; the clash is PDF-only
    "B006": "pdf",  # comedy.md hit is unrelated
    "B043": "live", # the country table is gone; the undefined metric remains in the roadmap KPIs
    "B066": "live", # the quoted sentence moved; the $70,000-over-20-years claim is on several live pages
    "B086": "pdf",  # "2.5 jobs per unit" (public-trust-financial PDF only)
    "B102": "pdf",  # Equation 2, phi^Participation_Index (cco-ptf-integrated-framework PDF only)
}

V, P, W, M = "valid", "partly valid", "wrong", "moot"
H, D, L, N = "headline", "derivation", "wording", "-"

J = {  # id: (verdict, severity, action)
 "A01": (V, H, "The HTML (sec 9) still says 'mathematical analysis confirms Pareto improvements' but no longer contains a proof; the PDF's proof assumes c_CCO >= c_TRAD for everyone. Restate as a conjecture, or state the condition (B0 at least the traditional transfer) under which it holds (S46)."),
 "A02": (V, D, "PDF only: first-order conditions mis-stated (ratio inverted, sign dropped; p(quality|h) undefined). The HTML model replaced them; rebuild the PDF."),
 "A03": (V, D, "PDF only: budget constraint adds B0 and P_convert from the same units. The HTML model splits basic units (min(B, Cap)); rebuild the PDF."),
 "A04": (V, D, "Lemma 2 (optimal-transfer-design and dual-currency-inflation) is a one-market argument with p, D, S undefined. Name the market and the conditions, or call it a sector-level result (S46)."),
 "A05": (V, D, "PDF only: table promises standard errors it does not show and does not say which parameter moves. Rebuild the PDF from the HTML; no run produced these numbers (S23/S30)."),
 "A06": (V, D, "Lemma 1 claims strict monotonicity; with the cap (HTML: min(B, Cap)) it is only weakly increasing, and the lemma's B0*2^O*R is not the HTML model's M(q)*min(B, Cap). Restate for the HTML model (S46)."),
 "A07": (V, L, "gamma is the leisure weight in the HTML utility (4.1) and risk aversion in Appendix A. Rename one."),
 "A08": (V, H, "PDF only: welfare decomposition 0.42/0.28/0.18/0.12 has no method and no run behind it. Gone from the HTML; rebuild the PDF; S23 classes it 'no basis'."),
 "A09": (M, L, "PDF only: the HTML model no longer uses delta for a housing share. Rebuild the PDF."),
 "A10": (V, L, "Abstract: say in a clause how 'productive beauty' is judged (peer panels, sec 4.2)."),
 "A11": (V, L, "Add one linking sentence per literature subsection (optional)."),
 "A12": (V, L, "PDF only: R_i used for both the multiplier and 'reciprocal relationships'. Rebuild the PDF."),
 "A13": (V, L, "'Eliminates benefit reduction entirely' -> 'eliminates income-based phase-outs'; conversions are still capped."),
 "B001": (V, H, "community-monetary-development sec 3.3: the theorem says p* < 0.05, the proof gives 0.118 and 0.074 (recompute.py). Restate the theorem with the computed steady states (S46)."),
 "B002": (V, D, "economic-modeling-simulation Table 5.4: every elasticity is about half the arc elasticity of its own row (-1.60, -2.04, -1.20, -0.57, -0.38; recompute.py). Recompute or drop the column; no run produced the table (S30)."),
 "B003": (V, H, "$847B: already C23 (retire in the summary). The paper body (abstract, conclusion) also needs it: it is one line of Scenario 2, not the integrated net."),
 "B004": (V, H, "pth-government-integration 3.1: $12-20B a year of 'community wealth' on a $12.5B one-time outlay (96-160% a year) has no derivation. Derive or label as an illustrative projection."),
 "B005": (V, H, "pth-independent-financing 2.2-2.3: the payments do not amortize the stated balances; with the table's own payments the avalanche takes 18.3 years and saves about $900, not 10 years and $85,000+ (recompute.py). C26 retires $85,000 in the summary; the paper body needs the same."),
 "B006": (V, D, "PDF only: Welfare Index table (142 vs 138) is gone from the HTML. Rebuild the PDF."),
 "B007": (V, D, "cco-ptf-integrated-framework 3.4: the example (ratio 3 -> 3x) needs alpha = 1 if Base Rate = 1, or alpha = 0 if Base Rate = 3, not 0.3-0.5 (recompute.py). Define the variables and fix the example."),
 "B008": (V, D, "economic-modeling-simulation 11.3: $2.1T (stock plus five years of flows) sits beside annual costs. Split or footnote."),
 "B009": (V, H, "drug-policy-reform abstract/sec 1: $1.52T vs the table's $4,616B (recompute.py). Already C23 for the summary; the paper body needs it too."),
 "B010": (V, D, "pth-independent-financing 5.4: at 200-1,000 credits a month, 100 credits take under a month, not 2-4 months (recompute.py). Fix the rates or the timeline."),
 "B011": (V, H, "PDF only (cco-ptf-integrated-framework): Bristol Pound 'GBP 5 billion' (GBP 2.5M per participant; recompute.py). The HTML no longer gives the figure. Rebuild the PDF; S23 opens the source."),
 "B012": (V, D, "economic-modeling-simulation phases: 73/85/95% and 89-97% not mapped to scenarios. Add a mapping table or label as targets."),
 "B013": (V, D, "dual-currency-inflation 3.x: budget identity has no source of P_t and P_convert's use is unstated. Complete it (S46)."),
 "B014": (V, D, "PDF only: the code caps the converted amount, the formula caps the octave. Rebuild the PDF; S46 states one rule."),
 "B015": (V, L, "cco-ptf-integrated-framework 2.4: the phi bonus rests on non-mainstream sources. Present phi as a design parameter, not a derived optimum."),
 "B016": (V, H, "30% viability (cco-ptf-integrated-framework) vs 55% minimum (economic-modeling-simulation). The audit's reconciliation (two definitions) is its own guess, not in either paper. One threshold, from a run: S5."),
 "B017": (V, D, "PDF only: items sum to $8.8B, total says $8.5B (recompute.py); the audit's ramp is not in the paper. The HTML has a new budget table; rebuild the PDF."),
 "B018": (V, H, "drug-policy-reform abstract: $847B 'net societal savings' vs the HTML table's net social value of $5.0T (PDF: $4.7T). Same fix as B003/C23."),
 "B019": (V, D, "economic-modeling-simulation 3.1: u(c, l, s) has no functional form. State it (S46)."),
 "B020": (V, L, "cultural-value-integration: 'objective foundation' for phi vs peer panels. Say panels judge eligibility."),
 "B021": (V, L, "International precedents listed without the lesson drawn. One sentence each (optional)."),
 "B022": (V, H, "cco-ptf-integrated-framework 5.4: 'proves optimal' with no criterion and no published sweep. Restate as design choices; a sweep is S32's job."),
 "B023": (V, D, "economic-modeling-simulation 7.1: 'diminishing returns above 80%' while V(n) is convex everywhere (recompute.py). Add the cost term or drop the claim."),
 "B024": (V, L, "cultural-value-integration: say what 'no downward mobility' locks (octave) and what is reassessed (multiplier)."),
 "B025": (V, H, "PDF only (economic-modeling-simulation): multiplier 2.86 vs 1.95 from the printed formula (recompute.py). Gone from the HTML; rebuild the PDF; check summaries for 2.86 (none found)."),
 "B026": (V, H, "community-monetary-development 7.2: break-even year 4-5 vs year 6 and ROI 250% without derivation. Derive or label as illustrative."),
 "B027": (V, D, "PDF only: O is a dollar amount in Equation 1 and an index in Lemma 1. Rebuild the PDF; the HTML uses n."),
 "B028": (V, H, "drug-policy-reform 2.2: Portugal 'deaths fell by 95%', 'crime dropped by 50%'; the audit reads Greenwald as 131 -> 20 deaths (85%) and the 50% as prisoners held on drug charges. Open Greenwald (2009) in S23 and correct."),
 "B029": (M, N, "Gone: the '$0-10,000' down payment row is no longer on the Hub (public-trust-financial PDF says $0)."),
 "B030": (V, D, "pth-government-integration 3.1: items sum to $12.0B, headline $12.5B (recompute.py). Add the missing $0.5B line or correct the headline."),
 "B031": (V, D, "PDF only (community-monetary-development): half-life 4.1 vs 3.72 from the printed formula (recompute.py). Gone from the HTML; rebuild the PDF."),
 "B032": (V, D, "dual-currency-inflation sec 1: $3T is about 11% of 2023 GDP, not 14% (recompute.py). Correct to 'about 11%' with the BEA source."),
 "B033": (V, H, "dual-currency-inflation conclusion: '65% lower inflation' is in no table: the PDF's Table 5.2 gives 51-54% (total) or 78-86% (excess); the HTML's 5.2 states 65% with no UBI comparison (recompute.py). Correct or remove; S23."),
 "B034": (V, D, "cco-ptf-integrated-framework: 'without reducing merchant income' needs alpha = 0 in the example (recompute.py). See B007."),
 "B035": (V, D, "Same as A04: call Lemma 2 a single-market result (S46)."),
 "B036": (P, H, "economic-modeling-simulation 11.2: +41% engagement, +67% innovation have no formula or interval. 4.x names the outcome categories ('community engagement metrics'; 'patents, startups, cultural output') but gives no formula; the audit's 'rigorously defined ... weighted index' overstates it. Label as illustrative or remove (S23)."),
 "B037": (V, D, "PDF only: participation_rate uniform(0.6, 0.95) vs beta(3, 2). The HTML snippet uses uniform(0.55, 0.95); Appendix A should match it. Rebuild the PDF."),
 "B038": (V, D, "pth-independent-financing 9.2 vs 2.2: same five families, different principal, rate, payment and savings (recompute.py). Align with 2.2 or label as a separate example."),
 "B039": (V, L, "PDF only: R_i and f() undefined in the conversion line. Rebuild the PDF."),
 "B040": (V, L, "PDF only: '1.3% annual' is the year-1 increment over baseline (recompute.py). Rebuild the PDF."),
 "B041": (V, L, "PDF only: PTF '15% of local activity' has no tax base. Rebuild the PDF; S46 names the base."),
 "B042": (V, L, "economic-modeling-simulation Appendix A: 'conversion_rate' names two things. Rename the scenario key."),
 "B043": (V, L, "The country comparison table is gone; 'Democratic Participation' is still an undefined KPI in integrated-implementation-roadmap Appendix I. Define it (turnout, CIP engagement)."),
 "B044": (V, H, "drug-policy-reform 9.1: no single set of dollar values for deaths and incarceration-years gives both net values (one needs a negative value per incarceration-year; recompute.py). Publish the valuation or remove the net figures."),
 "B045": (V, D, "pth-independent-financing 5.3: '$1,000-1,500 net improvement' needs a mortgage payment the example does not state. State the pre-sale costs."),
 "B046": (V, L, "pth-independent-financing 7.2-7.3: say Phase 3 adds sell-in and earn-in."),
 "B047": (V, L, "dual-currency-inflation sec 1: the cited 0.1%/1% GDP implies about 1% at $3T (recompute.py). Explain why the paper still calls it significant."),
 "B048": (V, H, "economic-modeling-simulation 6.1: ABM effects (23%, 31%, 41%) with no interval and no published run. Label as illustrative or remove (S23)."),
 "B049": (V, L, "cultural-value-integration: 'save and trade expired basic units' vs expiry. Say what is saved: the conversion right."),
 "B050": (V, H, "PDF only: second instance of 2.86 (economic-modeling-simulation PDF). See B025."),
 "B051": (V, L, "integrated-digital-governance 2.2: OECD/UN frameworks do not 'validate' the architecture. Limit to the digital components."),
 "B052": (V, H, "pth-government-integration abstract: '2.5x greater efficiency' is the wealth-building column; with the 40% cost cut it would be 4.2x (recompute.py). Name the metric."),
 "B053": (V, H, "community-monetary-development abstract and the research summary: 'below 5% within 15 years'. With p* = 11.8% the rate never reaches 5%; the 15-year formula implies a start rate of 82% (recompute.py). The audit's 'passes through 5%' is also wrong. Remove (S23)."),
 "B054": (V, L, "PDF only: policy bullets without signposts. Rebuild the PDF."),
 "B055": (V, D, "PDF only: PTF_Supply undefined in the housing regression. Rebuild the PDF; no estimate is published (S30)."),
 "B056": (P, L, "PDF only: Delta M_B is ambiguous (the audit concedes it may be correct). Rebuild the PDF."),
 "B057": (V, L, "risk-mitigation-framework: say what the 50/75/100% conversion capacity is a share of."),
 "B058": (V, H, "democratic-governance-pth 8.1: cooperative vs HOA statistics have no source. Cite or remove (S23)."),
 "B059": (V, L, "democratic-governance-pth Appendix A: define 'Efficiency' in the matrix."),
 "B060": (V, D, "pth-independent-financing 9.3: 200 households -> '500+ served', $35M, with no growth assumptions. State them or label as illustrative."),
 "B061": (V, H, "dual-currency-inflation abstract: '65% lower'. See B033 (56-61% for CCO+PTF in the PDF table; recompute.py)."),
 "B062": (V, H, "economic-modeling-simulation 9.x: -45% total from -31/-18/-24/-19: no weighting gives 45% (a weighted average is at most 31%, compounding gives 65%; recompute.py). Show the weights or remove."),
 "B063": (V, L, "risk-mitigation-framework: threat_matrix indexed by strings. Add a mapping or call it pseudo-code."),
 "B064": (M, N, "Gone: the 0.41 baseline table is no longer on the Hub."),
 "B065": (M, N, "Gone: quality_assessment_accuracy is no longer in data/optimal-parameters.json."),
 "B066": (V, H, "$70,000 over 20 years (us-real-estate-transformation, corporate-transformation, integrated-digital-governance 'target') vs $57,600 in 5 years (pth-independent-financing) and $70-140k in 10 years (pth-government-integration PDF). C24 restates the summary; say which figure is which scenario in each paper."),
 "B067": (V, D, "dual-currency-inflation 3.2: no rule aggregating C_{i,j,t} into C_{i,t}. State it (S46)."),
 "B068": (V, L, "PDF only: 'expiration creates natural velocity ceiling' (expiry raises velocity). Rebuild the PDF."),
 "B069": (V, L, "PDF only: exchange-rate models cited but not used. Rebuild the PDF."),
 "B070": (V, D, "Same as A04 and B035 (S46)."),
 "B071": (V, H, "economic-modeling-simulation 8.1/8.3: 2.8% productivity vs 3.5% GDP growth with no bridge; neither comes from a published run. Label as illustrative (S23)."),
 "B072": (V, D, "integrated-digital-governance 4.4: V(n) = 0.3n^2 + 0.7n log n is assumed, not derived. Label the weights as assumed (design parameter)."),
 "B073": (V, L, "drug-policy-reform conclusion: 85% is incarceration-years (38M of 45M), 69% is the rate (recompute.py). Label the metric."),
 "B074": (V, H, "PDF only: '68% of participants advance an octave a year' (cco-ptf-integrated-framework PDF); no run. Rebuild the PDF; S23."),
 "B075": (P, H, "economic-modeling-simulation and integrated-digital-governance: 'wealth effects 180% higher' vs 122% in 5.1. The audit's reconciliation (median flow vs 25-year average) is its own reading. No run produced either: S23/S30."),
 "B076": (V, D, "economic-modeling-simulation Appendix A: Stability = 1 - Var/Mean is not unit-free (recompute.py). Use the coefficient of variation."),
 "B077": (V, L, "risk-mitigation-framework 12.2: say the class is a control-flow sketch and point to the sections."),
 "B078": (V, L, "democratic-governance-pth 3.2: say when square-footage weighting and when quadratic voting apply."),
 "B079": (V, D, "pth-government-integration 3.3-3.4: buy-in grows 2.67x while the others double (recompute.py). State why or correct."),
 "B080": (V, L, "risk-mitigation-framework: define x_cents (link the X-cents paper, S4)."),
 "B081": (V, L, "democratic-governance-pth intro: soften 'not through compromise but through synergy' or point to sec 2."),
 "B082": (M, N, "Gone: '10-fold cross-validation' is no longer on the Hub."),
 "B083": (P, L, "integrated-digital-governance 4.1: W_CCO sums basic units and conversions; say whether B_i is a balance (stock). The audit's reading is plausible, not stated in the paper."),
 "B084": (V, H, "drug-policy-reform conclusion: '100,000 preventable deaths, 500,000 unnecessary incarcerations' a year, not in the body. Source or remove (S23)."),
 "B085": (V, L, "PDF only (us-real-estate-transformation): Acre Equity in credits vs dollars. Rebuild the PDF; the HTML should say dollar figures are reference values."),
 "B086": (M, N, "HTML fixed: '2.5 jobs per unit' is only in the public-trust-financial PDF. Rebuild the PDF."),
 "B087": (M, N, "Gone: the 20% pilot target is no longer on the Hub."),
 "B088": (V, H, "PDF only (pth-government-integration): 'wealth built $70,000-140,000' in 10 years. Rebuild the PDF; see B066."),
 "B089": (V, L, "risk-mitigation-framework conclusion: 'research demonstrates ridicule can be more effective' needs a citation."),
 "B090": (V, L, "democratic-governance-pth: say who oversees opt-in programs for non-members."),
 "B091": (V, L, "cultural-value-integration: 'Theorem 1' is an eligibility rule. Rename to Rule or Definition."),
 "B092": (V, D, "PDF only (economic-modeling-simulation): Gini decay formula vs the ABM. Rebuild the PDF."),
 "B093": (V, H, "data/optimal-parameters.json: median_wealth_accumulation 82,000 sits among inputs, and the papers report $82,000 as a result with a 95% CI. The audit's rescue ('calibration target') is not in the file; its header says 'optimal parameters'. Traced in S30."),
 "B094": (V, D, "PDF only (drug-policy-reform 5.1): $385B vs $390B by the paper's own method (recompute.py). The HTML 7.1 has new tables; rebuild the PDF."),
 "B095": (M, N, "Gone: '$6,000-10,000/year' is no longer on the Hub (the audit's arithmetic, 6,720-13,440, is right; its '60% net' rescue is not in the paper)."),
 "B096": (V, H, "pth-government-integration abstract: see B052."),
 "B097": (P, H, "community-monetary-development 4.2: NPV $1,847 vs $2,046 from the printed formula. The audit's explanation gives $1,832, and its '$2.04 million' should be $2,046 (recompute.py). Already C25 for the summary ('ROI'); the paper body needs the same."),
 "B098": (V, H, "economic-modeling-simulation: '85% poverty reduction' is the share of scenarios reaching < 2%. Say so where 85% appears (abstracts, cco-ptf-integrated-framework)."),
 "B099": (M, N, "The Hub serves each paper as its own page; the boundary problem was in the audit's merged export."),
 "B100": (V, L, "democratic-governance-pth 2.2: add one or two further studies on over-delegation (optional)."),
 "B101": (V, D, "PDF only (pth-government-integration 6.2): 'time to scale' 2-5 years vs full scale in years 6-10. Rebuild the PDF."),
 "B102": (M, N, "HTML fixed: Equation 2 (phi^Participation_Index) is only in the cco-ptf-integrated-framework PDF. Rebuild the PDF."),
 "B103": (V, H, "cco-ptf-integrated-framework discussion: 85% -> 98% is 13 points, not 15 (recompute.py)."),
 "B104": (V, L, "economic-modeling-simulation 3.2: the Acre Equity function is in dollars; say how dollars become credits."),
 "B105": (V, L, "risk-mitigation-framework: PTFSafeguards is invalid Python. Use literals."),
 "B106": (V, L, "risk-mitigation-framework 3.5: say how Youth CCO Accounts resist parental coercion."),
 "B107": (V, L, "democratic-governance-pth: 'independent judiciary through elected grievance committees'. Reword."),
 "B108": (V, D, "integrated-digital-governance 4.3: g(C_k) undefined; say outflow is proportional to Z_k."),
 "B109": (V, L, "PDF only (drug-policy-reform): author order reversed. Rebuild the PDF; attribution per compassionism-simulation's CLAUDE.md."),
 "B110": (M, N, "Gone: the $23,280 example is no longer on the Hub."),
 "B111": (V, L, "economic-modeling-simulation, optimal-transfer-design, basic-living-economic-index: Hoynes & Rothstein (2019) is a review; 'employing Monte Carlo methods' -> 'reviewing'."),
 "B112": (V, L, "economic-modeling-simulation 3.1: index the sum (i in M_k) and use a superscript."),
 "B113": (V, L, "economic-modeling-simulation Appendix A: 'poverty_elimination' filled with poverty_rate. Rename."),
 "B114": (V, L, "PDF only (integrated-digital-governance conclusion). Rebuild the PDF."),
 "B115": (V, L, "PDF only (drug-policy-reform 2.3). Rebuild the PDF."),
 "B116": (V, L, "pth-independent-financing abstract: 'break-even in 6-12 months' needs the $500K-1M seed capital in the same sentence."),
 "B117": (V, L, "pth-independent-financing 4.1: say the $400,000 is non-acquisition support."),
 "B118": (V, L, "cco-ptf-integrated-framework abstract: '2^n' vs 2^(n-1); say where counting starts."),
 "B119": (V, L, "risk-mitigation-framework evolution table: '50% cost reduction' target has no reference. Label as a target."),
 "B120": (V, L, "economic-modeling-simulation: point to where calculate_outcome is defined (it is not on the Hub; cco-ptf-simulation-replication.html now redirects to the engine's replication page)."),
 "B121": (M, N, "Gone: 'minimum viable: 75%' is no longer on the Hub (see B016 for the live 30% vs 55%)."),
 "B122": (V, L, "PDF only (drug-policy-reform 5.2). Rebuild the PDF."),
 "B123": (M, N, "Fixed: the references cite Johnson (2017) and the '2017, updated 2025' wording is gone."),
 "B124": (M, N, "Gone: the revenue bands the audit quotes are no longer on the Hub; the live bands (70-80% primary, 10-15% secondary) are coherent."),
 "B125": (V, L, "pth-government-integration and pth-independent-financing: NotebookLM credited with the Acre Equity 'conceptual framework' while Duke conceived it. Reword the acknowledgment."),
 "B126": (V, L, "PDF only: Ulanowicz phi vs golden phi. Rebuild the PDF."),
 "B127": (V, H, "cco-ptf-integrated-framework: second '15 percentage point' (recompute.py). See B103."),
 "B128": (V, L, "optimal-transfer-design Appendix B: say O is the octave index here."),
 "B129": (V, L, "democratic-governance-pth abstract: 'strong evidence' for an untried system. Say 'suggestive precedents'."),
 "B130": (M, N, "Each paper is its own page on the Hub; the abrupt transition was in the merged export."),
 "B131": (V, L, "cultural-value-integration: freelancer projected outcomes (45%, 32%, 58%, 67%) have no source. Label as illustrative."),
 "B132": (M, N, "Fixed: the strategy cell now reads 'Diversified participant base'."),
}

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    csv_path = HERE / "triage.csv"
    subprocess.run([sys.executable, "-I", str(HERE / "presence_check.py"), sys.argv[1], "--csv", str(csv_path)], check=True)
    rows = list(csv.DictReader(open(csv_path)))
    missing = [r["id"] for r in rows if r["id"] not in J]
    if missing:
        sys.exit(f"no judgment for: {missing}")
    for r in rows:
        files = r["files"].split()
        live = [f for f in files if not f.endswith(".pdf") and f.endswith((".html", ".json"))]
        hub = "live" if live else ("pdf" if any(f.endswith(".pdf") for f in files) else "gone")
        hub = HUB.get(r["id"], hub)
        v, s, a = J[r["id"]]
        r.update(hub=hub, verdict=v, severity=s, action=a)
    fields = ["id", "title", "hub", "verdict", "severity", "action", "files", "locator", "status", "check"]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows({k: r[k] for k in fields} for r in rows)
    from collections import Counter
    print("hub:", dict(Counter(r["hub"] for r in rows)))
    print("verdict:", dict(Counter(r["verdict"] for r in rows)))
    print("live valid by severity:", dict(Counter(r["severity"] for r in rows if r["hub"] == "live" and r["verdict"] in (V, P))))
    print("pdf-only valid:", sum(r["hub"] == "pdf" and r["verdict"] in (V, P) for r in rows))
    write_md(rows)

MARK = "<!-- generated by triage.py: everything below this line is rewritten on each run -->"

def page(r):
    files = r["files"].split()
    html_ = [f for f in files if f.endswith((".html", ".json"))]
    return ", ".join(html_[:3]) + (" ..." if len(html_) > 3 else "") if html_ else ", ".join(files) or "-"

def write_md(rows):
    md = HERE / "triage.md"
    head = md.read_text().split(MARK)[0] if md.exists() else "# refine.ink audit triage\n\n"
    out = [head.rstrip() + "\n\n" + MARK + "\n"]
    live = [r for r in rows if r["hub"] == "live" and r["verdict"] in (V, P)]
    for sev, name in ((H, "Changes a headline figure"), (D, "Changes a derivation or table"), (L, "Wording, labels and citations")):
        sel = [r for r in live if r["severity"] == sev]
        out.append(f"\n## Valid and live: {name.lower()} ({len(sel)})\n\n| Id | Page | Correction needed |\n|---|---|---|\n")
        out += [f"| {r['id']}{' (partly)' if r['verdict'] == P else ''} | {page(r)} | {r['action']} |\n" for r in sel]
    sel = [r for r in rows if r["hub"] == "pdf"]
    out.append(f"\n## Changed on the HTML page, still in the PDF ({len(sel)})\n\nThese need no new text: rebuilding each PDF from its current HTML page (S24) removes them.\n\n| Id | PDF | Verdict | Note |\n|---|---|---|---|\n")
    out += [f"| {r['id']} | {page(r).replace('papers/pdfs/', '')} | {r['verdict']} | {r['action']} |\n" for r in sel]
    sel = [r for r in rows if r["verdict"] == M and r["hub"] != "pdf"]
    out.append(f"\n## Moot: gone from the Hub, or nothing to fix ({len(sel)})\n\n| Id | Note |\n|---|---|\n")
    out += [f"| {r['id']} | {r['action']} |\n" for r in sel]
    md.write_text("".join(out))
    write_additions(rows)

def write_additions(rows):
    """audits/corrections-additions.md: the items S24 lands, appended to the main corrections list."""
    out = ["# Corrections additions from the refine.ink triage (S29)\n\n",
           "Generated by `audits/refine/triage.py`; do not edit by hand. The main corrections package (C01-C22) is not in these ",
           "repositories, so S24 merges this list with it and with `corrections-package-s5.md` (C23-C30). Each item is a ",
           "valid refine.ink critique of a passage still on a live Hub page. Ids are the audit's (`audits/refine/triage.csv`); ",
           "arithmetic is in `audits/refine/recompute.py`. Wording-only items (labels, definitions, citations) are listed in ",
           "`audits/refine/triage.md`, and PDF-only items go away when the PDFs are rebuilt from the current HTML.\n"]
    for sev, name in ((H, "Headline figures"), (D, "Derivations and tables")):
        sel = [r for r in rows if r["hub"] == "live" and r["verdict"] in (V, P) and r["severity"] == sev]
        out.append(f"\n## {name} ({len(sel)})\n\n")
        out += [f"- **S29-{r['id']}** ({page(r)}). {r['action']}\n" for r in sel]
    (HERE.parent / "corrections-additions.md").write_text("".join(out))

if __name__ == "__main__":
    main()
