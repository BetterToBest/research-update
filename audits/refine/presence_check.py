#!/usr/bin/env python3
"""Presence check for the refine.ink audit comments against the live Research Hub.

Usage: python3 presence_check.py <path to a research-hub checkout> [--csv out.csv]

Builds a text corpus from every HTML page (tags stripped), every PDF in papers/pdfs
(pdftotext -layout) and every JSON file, then searches each comment's locator
(a case-insensitive regular expression taken from the passage the audit quotes).
"present" means the quoted passage, or its key figure, is still on the Hub; it does
NOT mean the critique is right. Step S29 checks each critique and fills the rest.

Ids: A01-A13 are the 13 comments on the CCO-PTF mechanism-design paper
(refine-feedback-priority-sorted.md); B001-B132 are the 132 comments on the
Oct 10, 2025 compendium review (the "integrated-digital-governance" and
"refine-feedback-priority" files hold the same 132 comments).
`check` notes are Claude's recomputations from Oct 28, 2026 (Chat), to be confirmed in S29.
"""
import csv, html, json, pathlib, re, subprocess, sys

C = [  # (id, short title, locator regex, check note)
 ("A01","Pareto dominance proof rests on unproven premises",r"Pareto[ -]dominat|Pareto efficien",""),
 ("A02","First-order conditions mis-stated",r"First[- ]order conditions",""),
 ("A03","Budget constraint counts Basic Units twice",r"dynamic budget constraint",""),
 ("A04","Equilibrium proof (App. B.2) is a one-market argument",r"excess demand function",""),
 ("A05","Monte Carlo table promises standard errors it lacks",r"standard errors in parentheses",""),
 ("A06","Monotonicity only weak where the cap binds",r"strictly increasing in both arguments",""),
 ("A07","gamma reused (housing share vs risk aversion)",r"Risk aversion",""),
 ("A08","Welfare decomposition 0.42/0.28/0.18/0.12 has no method",r"Direct transfers",""),
 ("A09","delta reused (housing share vs time preference)",r"Time preference",""),
 ("A10","Phi enhancement unexplained in abstract",r"phi enhancement for productive beauty",""),
 ("A11","Literature review not tied to mechanism design",r"Welfare Cliffs and Work Disincentives",""),
 ("A12","R_i defined twice",r"reciprocal community relationships",""),
 ("A13","'Eliminates benefit reduction entirely' overstated",r"eliminates benefit reduction entirely",""),
 ("B001","Convergence theorem p*<0.05 contradicted by its proof",r"converges to steady state","p* = 0.02/0.17 = 11.8% (CCO), 0.02/0.27 = 7.4% (PTF): audit right"),
 ("B002","Elasticity column wrong (Table 5.4)",r"[-−]0\.71","midpoint elasticity from 2.8%/1.2% at +/-25% = -1.60: audit right"),
 ("B003","$847B net savings has no derivation",r"847 billion",""),
 ("B004","$12-20B/yr community wealth unexplained",r"12-20B|12–20B",""),
 ("B005","Avalanche example payments do not amortize",r"Five-Homeowner",""),
 ("B006","Welfare index 142 vs 138 contradicts 9.2",r"Welfare Index",""),
 ("B007","Merchant multiplier variables/alpha inconsistent",r"Merchant Multiplier",""),
 ("B008","$2.1T mixes stock and flow",r"\$2\.1 ?T",""),
 ("B009","$1.52T prose vs $4,616B table",r"1\.52 trillion","table sums to 4,616: audit right"),
 ("B010","Earn-in credits timeline contradicts rates",r"Entry level \(100 credits\)",""),
 ("B011","Bristol Pound GBP 5 billion (should be ~5 million)",r"Bristol Pound.{0,120}billion",""),
 ("B012","Poverty-reduction percentages not mapped to scenarios",r"73% poverty reduction",""),
 ("B013","Household budget identity incomplete",r"Household Budget Constraints",""),
 ("B014","Industry cap in code vs formula",r"industry_cap",""),
 ("B015","Phi justified by fringe sources",r"Financial Gravity",""),
 ("B016","30% vs 55% participation threshold",r"30% population|beginning at 30%",""),
 ("B017","Five-year cost total needs ramp note",r"Total Five-Year Cost",""),
 ("B018","$847B vs $4.7T net social value",r"net societal savings",""),
 ("B019","Utility function u() unspecified",r"SocialStatus",""),
 ("B020","'Objective' phi vs peer panels",r"Phi rate recognition",""),
 ("B021","International models: lessons not drawn",r"Vienna",""),
 ("B022","'Optimal' parameters with no criterion",r"proves optimal",""),
 ("B023","Diminishing returns vs convex V(n)",r"coordination complexity",""),
 ("B024","'No downward mobility' unclear",r"No downward mobility",""),
 ("B025","GDP multiplier 2.86 vs formula",r"2\.86","1/(1-0.85*0.75+0.15) = 1.95: audit right"),
 ("B026","Break-even and 250% ROI not derived",r"250% over 10 years|ROI: 250%",""),
 ("B027","Symbol O switches meaning",r"Octave Level \(O\)",""),
 ("B028","Portugal figures overstated (Greenwald)",r"deaths fell by 95%",""),
 ("B029","PTH down payment $0-10,000 vs none",r"\$0[-–]10,000",""),
 ("B030","$12.0B items vs $12.5B headline",r"250 local trusts",""),
 ("B031","Half-life 4.1 vs discrete formula",r"Half-life","discrete 3.72 y; 4.1 matches continuous ln2/0.17 = 4.08: audit right"),
 ("B032","$3T = 14% of 2023 GDP (should be ~11%)",r"14% of 2023","3/27.4 = 11%: audit right"),
 ("B033","'65% lower inflation' not in the tables",r"65% lower",""),
 ("B034","Revenue neutrality needs alpha = 0",r"without reducing merchant income",""),
 ("B035","Lemma 2 is partial equilibrium",r"Lemma 2",""),
 ("B036","Engagement +41% / innovation +67% definitions",r"innovation output by 67",""),
 ("B037","participation_rate uniform vs beta(3,2)",r"uniform\(0\.6, ?0\.95\)",""),
 ("B038","Suburban cooperative numbers vs 2.2",r"Suburban Cooperative",""),
 ("B039","R_i and f() undefined in conversion",r"B_expired",""),
 ("B040","'1.3% annual' inflation ambiguous",r"1\.3% annual",""),
 ("B041","PTF '15% of local activity' base unclear",r"15% of local economic activity",""),
 ("B042","conversion_rate name used twice",r"'conversion_rate': random",""),
 ("B043","'Democratic Participation' row undefined",r"Democratic Participation",""),
 ("B044","Net social value derivation missing",r"Net social value",""),
 ("B045","Sell-in 'net improvement' needs mortgage",r"Net improvement: \$1,000",""),
 ("B046","Pathway rollout timeline contradiction",r"Add all four pathway options",""),
 ("B047","Inflation risk vs GiveDirectly evidence",r"0\.1 ?% inflation per 1 ?% of GDP",""),
 ("B048","ABM effects without intervals",r"Geographic clustering increases effectiveness",""),
 ("B049","'Save and trade expired basic units'",r"save and trade expired basic units",""),
 ("B050","Multiplier 2.86 (second instance)",r"propensity to consume with basic units","see B025"),
 ("B051","OECD/UN frameworks 'validate' CCO-PTF",r"validate the CCO-PTF-CIP-SZH architecture",""),
 ("B052","'2.5x greater efficiency' undefined",r"2\.5x greater efficiency",""),
 ("B053","'Below 5% within 15 years' vs p*",r"below 5 ?% within 15 years","see B001"),
 ("B054","Policy bullets need signposting",r"Poverty Reduction Strategy Paper",""),
 ("B055","PTF_Supply undefined",r"PTF_Supply",""),
 ("B056","Inflation bound: Delta M_B ambiguous",r"π_max|pi_max",""),
 ("B057","Risk-tier conversion percentages",r"Risk Score Range",""),
 ("B058","Cooperative housing statistics unsourced",r"Resident Participation",""),
 ("B059","Voting matrix 'Efficiency' ambiguous",r"Preference Expression",""),
 ("B060","Metropolitan case 200 to 500+ households",r"Mixed Metropolitan Program",""),
 ("B061","'Inflation rates 65% lower' (abstract)",r"inflation rates 65% lower","see B033"),
 ("B062","Carbon -45% aggregation",r"Total emissions reduction: 45%",""),
 ("B063","threat_matrix indexing error",r"threat_matrix",""),
 ("B064","Baseline Gini 0.41 vs 0.45-0.49",r"Gini Coefficient: 0\.41",""),
 ("B065","quality_assessment_accuracy distribution",r"quality_assessment_accuracy",""),
 ("B066","PTH wealth $70,000 / 20 years vs others",r"\$70,000 average per household",""),
 ("B067","Capacity aggregation rule missing",r"2\^?min\(O",""),
 ("B068","'Velocity ceiling' backwards",r"velocity ceiling",""),
 ("B069","Exchange-rate models not connected",r"International Flows Equilibrium",""),
 ("B070","Unique equilibrium lemma disconnected",r"Existence of Unique Equilibrium",""),
 ("B071","TFP 2.8% vs GDP 3.5% bridge",r"Total productivity growth: 2\.8%",""),
 ("B072","V(n) weights assumed, read as derived",r"0\.3n",""),
 ("B073","Incarceration 85% vs 69%",r"85% reduction in drug-related incarceration",""),
 ("B074","68% advance an octave each year",r"68% of participants advancing",""),
 ("B075","Wealth 180% vs 122%",r"180% higher",""),
 ("B076","Stability index not unit-free",r"Stability = 1 [-−] Var",""),
 ("B077","AdaptiveSecurity pseudo-code",r"class AdaptiveSecurity",""),
 ("B078","Square-footage weighting vs QV",r"Square footage weighted",""),
 ("B079","Buy-in scales 2.7x",r"750K buy-in",""),
 ("B080","x_cents undefined",r"x_cents",""),
 ("B081","'Not through compromise but synergy'",r"not through compromise but through synergy",""),
 ("B082","'10-fold cross-validation' unexplained",r"10-fold cross-validation",""),
 ("B083","W_total stock vs flow",r"W_\{?total",""),
 ("B084","500,000 incarcerations a year unsourced",r"500,000 unnecessary incarcerations",""),
 ("B085","Acre Equity credits vs dollars",r"dollar-for-dollar credit",""),
 ("B086","2.5 jobs per housing unit",r"2\.5 jobs per housing unit",""),
 ("B087","Pilot 20% vs 25-50% cost cut",r"20% cost reduction demonstrated",""),
 ("B088","Wealth built $70k-140k/10 yrs",r"Wealth built",""),
 ("B089","'Ridicule more effective' uncited",r"ridicule can be more effective",""),
 ("B090","Oversight of opt-in programs",r"Democratic oversight of benefit programs",""),
 ("B091","'Theorem 1' is an eligibility rule",r"Productive Beauty Integration",""),
 ("B092","Gini decay formula vs ABM",r"ρsynergy|rho_?synergy|ρ_synergy",""),
 ("B093","$82,000 listed as an input",r"median_wealth_accumulation","in data/optimal-parameters.json under pth_parameters as 'expected wealth building' (an input), yet papers report it as a result with a 95% CI: S30"),
 ("B094","Five-year savings $385B vs $390B",r"Cumulative savings: \$385B",""),
 ("B095","Equity $6-10k/yr vs 6,720-13,440",r"\$6,000[-–]10,000",""),
 ("B096","'2.5x efficiency' in abstract",r"reducing per-household costs by 40%","see B052"),
 ("B097","NPV $1,847 vs formula",r"\$1,847","printed formula gives 2,046; $180 growing after year 1 gives 1,832: neither the paper nor the audit's explanation matches"),
 ("B098","'85%' = share of scenarios, not reduction",r"85% of scenarios",""),
 ("B099","Paper boundaries in compendium",r"Recovery Procedures",""),
 ("B100","Liquid democracy: one citation",r"Gersbach",""),
 ("B101","Time to scale 2-5 y vs 6-10 y",r"PTH \+ CCO \+ Other",""),
 ("B102","Phi overlay vs tier",r"Participation_Index",""),
 ("B103","'15 percentage point' (85% to 98% is 13)",r"15 percentage point","98-85 = 13: audit right"),
 ("B104","Acre Equity formula monetary",r"Acre Equity Function",""),
 ("B105","PTFSafeguards invalid Python",r"max_daily_trades = 10",""),
 ("B106","Youth CCO accounts safeguards",r"Youth CCO Accounts",""),
 ("B107","'Elected judiciary' tension",r"elected grievance committees",""),
 ("B108","SZH outflow term g() undefined",r"dZ_k",""),
 ("B109","Author order reversed",r"Claude A\.I\. \(Anthropic\)",""),
 ("B110","$23,280 input vs output",r"\$23,280",""),
 ("B111","Hoynes & Rothstein is a review",r"Hoynes",""),
 ("B112","Collective capacity sum unindexed",r"Ck,t = |C_\{k,t\}",""),
 ("B113","poverty_elimination label",r"'poverty_elimination'",""),
 ("B114","Outcomes read as one-to-one",r"cohesion index improvement from 0\.65",""),
 ("B115","Oregon lessons mixes inference",r"16,000 of 38,000",""),
 ("B116","Break-even needs seed capital note",r"30-40 pay-in households",""),
 ("B117","$400,000 is non-acquisition",r"participant support: \$400,000",""),
 ("B118","2^n vs 2^(n-1)",r"octave doubling benefits",""),
 ("B119","50% cost reduction unreferenced",r"50% cost reduction",""),
 ("B120","calculate_outcome location",r"class MonteCarloAnalysis",""),
 ("B121","Participation 60-95% vs 75% viable",r"minimum viable: 75%",""),
 ("B122","5.2 lacks forward reference",r"CCO-PTF-CIP-SZH Integrated Model",""),
 ("B123","2017 vs 2025 citation",r"2017, updated 2025",""),
 ("B124","Budget bands over 100%",r"Expansion fund \(10-15%\)",""),
 ("B125","Acre Equity attribution (NotebookLM)",r"NotebookLM",""),
 ("B126","Ulanowicz phi vs golden phi",r"Ulanowicz",""),
 ("B127","15 vs 13 points (second instance)",r"15 percentage point improvement","see B103"),
 ("B128","O index vs value in Lemma 1",r"P_convert/∂O|dP_convert",""),
 ("B129","'Strong evidence' wording",r"successful precedents provide strong evidence",""),
 ("B130","Abrupt paper transition",r"Cultural Value Integration in Economic Systems",""),
 ("B131","Freelancer outcomes recap",r"Income stability: 45% improvement",""),
 ("B132","Risk table strategy cell blank",r"Hardship fund for temporary support",""),
]

def corpus(root):
    root = pathlib.Path(root); docs = {}
    skip = {".git", "v1"}  # the frozen v1 archive (S2) is not the live Hub
    for p in root.rglob("*"):
        if any(part in skip for part in p.relative_to(root).parts) or not p.is_file():
            continue
        rel = str(p.relative_to(root))
        if p.suffix == ".html":
            t = p.read_text(errors="ignore")
            t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
            docs[rel] = html.unescape(re.sub(r"<[^>]+>", " ", t))
        elif p.suffix in (".json", ".md"):
            docs[rel] = p.read_text(errors="ignore")
        elif p.suffix == ".pdf":
            r = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True)
            docs[rel] = r.stdout
    return {k: re.sub(r"\s+", " ", v) for k, v in docs.items()}

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    docs = corpus(sys.argv[1]); rows = []
    for cid, title, loc, note in C:
        rx = re.compile(loc, re.I)
        hits = sorted(k for k, v in docs.items() if rx.search(v))
        rows.append({"id": cid, "title": title, "locator": loc,
                     "status": "present" if hits else "not found",
                     "files": " ".join(hits), "check": note})
    out = sys.argv[sys.argv.index("--csv") + 1] if "--csv" in sys.argv else None
    if out:
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    n = sum(r["status"] == "present" for r in rows)
    print(f"{len(docs)} documents searched; {n} of {len(rows)} audit passages still present")
    for r in rows:
        if r["status"] != "present":
            print("not found:", r["id"], r["title"])

if __name__ == "__main__":
    main()
