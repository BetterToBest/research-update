# Grok, general audit of the Simulation (v5.9.9), Nov 17, 2026

Pasted by Duke in the S13 part 1 session. It answers a general request, not the prompt in `audits/2026-11-17-release-audit-prompt.md`. Grok's prompted reply is still to come and stays separate. Saved word for word below the line, with one change: Grok's three source links, which had empty link text, are printed as `(source: URL)` so the repository's link check can read the file. Not yet triaged: S13 part 2 does that, with the prompted replies and the Nemotron reading (`audits/2026-11-17-release-review-nemotron.md`).

Points for the triage, noted on saving (not checked):
- "too little wealth (often higher under the programme because of the price rule + zero real return on savings)" describes the v5.6 model. In v5.9 wealth is held by asset class with returns, and wealth poverty falls under both designs.
- "no full government budget constraint outside the programme": v5.9 has a government account (`gv`) as a reading, not on the main row.
- Its suggestions 2 (a model card), 3 (a simpler default view), 6 (the engine as a module) and 8 (a "what this model is not" box) overlap the Nov 9 audit's finding 7, which the in-house pass found still open.

---

**Clarity, rigor, and technical audit of the Compassionism Simulation (v5.9.9)**

This is a high-quality, unusually transparent research-oriented agent-based model (ABM). It is browser-based, fully open (Apache-2.0 code / CC BY 4.0 docs), BLEI-calibrated against US CES and related data, and maintained with exceptional process discipline: preregistration language, frozen engines, common-random-numbers pairing, extensive unit/DOM/guard tests, detailed MODEL_SPEC.md / ODD.md / TESTBED_SPEC.md, plain-language reports in `dev/reports/`, decision logs, and a replication framework that tracks every figure back to data files and commands. (source: https://bettertobest.github.io/compassionism-simulation/replication.html)

The project explicitly states that the math/code was engineered by Claude from Duke Johnson’s concepts and has **not yet been reviewed by an independent economist**. That disclaimer is correctly prominent on the main pages, README, and replication materials. (source: https://bettertobest.github.io/compassionism-simulation/)

v5.9.9 (released 17 Nov 2026) is a presentation/weighting polish on the v5.9 model generation (full-coverage design meeting NEEC C2.2 criterion + opt-in design; central-bank switch; full-backing main row). Recent micro-releases (v5.9.x) correctly fixed weighting artifacts from the 18 high-wealth representative agents, Gini calculation, chart construction, sticky navigation, and reader-facing terminology (eliminating internal ledger/step codes from public pages). (source: https://raw.githubusercontent.com/BetterToBest/compassionism-simulation/main/CHANGELOG.md)

### Clarity
**Strengths**
- Excellent progressive disclosure: “answer in ten seconds,” guided sections, glossary with hover/tap definitions, findings explorer with per-release data files, and clear separation of v5.9 (newest) vs v5.6 (earlier panel).
- Strong emphasis on paired differences, 95% intervals on the differences (not separate means), 10th–90th percentile bands, and explicit statements that results are implications of assumptions, not forecasts.
- Recent reader-wording passes (v5.9.6–v5.9.7) replaced internal codes with plain names (“full-coverage design,” “opt-in design,” “central-bank study,” etc.). Automated checks (`reader_codes.py`, `reader_check.js`) enforce this.
- Limits and decisive unknowns (especially the degree of output backing for Source payouts) are stated early and repeatedly.
- Reproduction commands, data provenance, and version history are first-class.

**Weaknesses / residual friction**
- Cognitive load remains high. Multiple model generations (v5.6 vs v5.9), two designs, multiple environments (Reference / Adverse / Stress), horizons (20/40), backing/financing readings, central-bank switch, and two BLEI readings create a combinatorial explosion. Even with good labeling, first-time or non-specialist readers can get lost.
- Terminology density (CCO, PTF, PTH, SZH, CIP, BLEI, EDC, FBS, OEIAS, basket poverty, wealth poverty, programme inflation, Acre Equity, etc.) is unavoidable given the framework but still requires frequent glossary use.
- Some pages and the replication framework are very long; the “what is being replicated” summary helps, but a single one-page “executive model card” (purpose, key assumptions, headline estimands, known limits, how to reproduce the main table) would still be useful.
- The “too little wealth” result (often higher under the programme because of the price rule + zero real return on savings) is carefully framed, yet the framing itself is long and could be tightened.

### Rigor
**Strengths**
- Common random numbers, 500 paired seeds, reporting of paired differences and intervals on those differences is methodologically sound.
- Clear separation of endogenous vs exogenous variables, fixed order of events within a year, and explicit random streams (construction, recession path, main stream, etc.) documented in MODEL_SPEC.md.
- Multiple poverty concepts (BLEI days, cost-of-living / MIT basket, official FPL, wealth threshold) plus severity, children’s outcomes, and household measures.
- Safety-net (SNAP + EITC + refundable CTC) included in both arms since v5.6, removing a major fairness critique of earlier “against no programme” comparisons.
- Preregistration language, frozen engines, second independent implementation checks, gap-closing appendices, and extensive sensitivity / study infrastructure.
- Explicit acknowledgment that the model measures material poverty, cost, work, and prices—not the cultural / flourishing claims of the broader framework.
- ODD protocol (Grimm et al. 2020 style) and detailed parameter provenance tables distinguishing sourced / derived / design / assumed.

**Weaknesses / areas needing independent scrutiny**
- **Price formation** remains the single largest modeling choice. Unmatched new money moves the general price level by a simple rule; essentials respond to excess demand relative to capacity. The main v5.9 row assumes full output backing (a design parameter). Without that assumption, programme inflation is large and erodes wealth. The model correctly flags this as the decisive unknown and shows alternatives, but the functional form itself is a strong assumption that an independent economist would examine closely.
- Central-bank module (Taylor-rule policy rate, QE floor, asset-price and forced-sale channels) is a useful addition but is itself a stylized formula, not a full institutional representation. It does not affect the price of essentials (explicitly noted as a model limit).
- Wealth threshold ($25k, moved with prices) is a design choice whose original provenance is undocumented (now flagged). Household reading uses six months of own costs—an improvement, but still conventional.
- Labour response uses literature elasticities (Chetty, Vivalt et al.), but the permanent job-loss pay cut is a design parameter and drives important results.
- No spatial structure beyond aggregate SZH coherence/density thresholds; no firm-level behavior beyond aggregate ESP pools and capacity; no full government budget constraint outside the programme; fixed household structure in the main row (ageing is a reading).
- Calibration of some parameters (especially living-wage basket weighting, starting wealth distribution relative to SCF, PTF adoption dynamics) still has open items listed in CONTRIBUTING.md.
- The model has not undergone formal external economic review. Internal accounting checks, unit tests, and a second implementation are strong process safeguards, but they are not a substitute.

### Technical
**Strengths**
- Single source of truth for the release engine (extracted from `index.html` into the harness). Browser + Node execution paths, extensive unit suite (hundreds of tests), DOM tests, figure-check scripts, guard tests that keep released numbers bit-identical under default settings, and CI on every push.
- Data architecture is clean: one data file per release under `data/releases/`, manifest, tools for adding a release, suite regeneration scripts that enforce consistency between plain and weighted statistics.
- Recent weighting fixes for the high-wealth representative agents (v5.9.5–v5.9.9) were necessary and correctly implemented; medians and weighted averages are now shown where appropriate.
- Seeded PRNG (mulberry32) with fully documented draw order and samplers; common-random-numbers discipline is enforced by fixed draw counts per adult per year.
- Clear separation of the earlier engine (`earlier-engine.html`) from the release model.

**Weaknesses / technical debt**
- The engine lives inside a large HTML file. While this enables zero-install browser use, it makes pure-code review, diffing, and modular testing harder than a conventional TypeScript/Python package would be. The extraction approach mitigates this but does not eliminate it.
- Combinatorial growth of studies, readings, and switches increases the surface area that must stay consistent across pages, data files, and checks.
- Visual-suite and findings pages are data-driven and therefore robust, but the sheer number of charts/tables raises the cost of any future metric change.
- Some older documentation still refers to earlier engine details; the project has been systematically cleaning this, but residual historical text remains in places.

### Suggestions for improvements (prioritized for a prospective next major step after v5.9.9)

1. **Independent economic review (highest priority)**  
   Commission a formal review focused on (a) the price rule and backing assumption, (b) labour-supply and job-loss modules, (c) wealth dynamics under zero real return, and (d) comparison with existing UBI / guaranteed-income / cooperative literature. Publish the review and any resulting model changes.

2. **Model-card / one-page summary**  
   Add a concise, citable “Model Card” (purpose, population, key mechanisms, estimands, main assumptions, known limits, reproduction command for the headline table) linked from the top of the simulation and findings pages.

3. **Further reduce cognitive load**  
   - Default the public-facing view even more aggressively to the single most policy-relevant design + environment + horizon.  
   - Make alternative designs/readings secondary (tabs or collapsible “Explore alternatives”).  
   - Shorten the framing text around the wealth result while keeping the intellectual honesty.

4. **Price-module robustness**  
   - Add at least one additional, literature-grounded price-response specification as a labeled reading.  
   - Explicitly test sensitivity of headline poverty and wealth results to the backing share on a finer grid and surface the results more prominently.

5. **Calibration hygiene**  
   - Resolve or formally freeze the open items in CONTRIBUTING.md (especially living-wage basket population weighting and the wealth-threshold provenance).  
   - Consider a short “Calibration appendix” that maps every major constant to its source or to “design choice – swept.”

6. **Technical architecture**  
   - Extract the release engine into a pure JS module that both the browser page and the harness import (or compile to a single file for the browser). This would improve reviewability without sacrificing the zero-install property.  
   - Continue the excellent automated reader-code and figure-consistency checks; extend them to any new public pages.

7. **Communication of uncertainty**  
   - Keep the current practice of showing intervals and percentile bands.  
   - Consider a simple “how much does this result depend on X?” call-out for the two or three most influential assumptions (backing share, price rule, job-loss pay cut).

8. **Minor polish**  
   - Ensure every public page that still mentions internal history is fully migrated to the plain-language regime already enforced by the reader checks.  
   - Re-record the narrated walk-through once the model is considered settled.  
   - Add a short “What this model is *not*” box near the top of the main page.

### Overall assessment
The project is already at a high standard of transparency, process rigor, and technical hygiene for an exploratory policy ABM. The recent v5.9.x series demonstrates disciplined incremental improvement (weighting correctness, terminology hygiene, navigation, visual suite parity). The largest remaining gaps are (1) independent domain-expert review of the core economic mechanisms—especially price formation and the backing assumption—and (2) further reduction of the cognitive burden on non-specialist readers while preserving the model’s honest complexity.

These are addressable without discarding the substantial investment already made. The open codebase, extensive documentation, and automated guardrails put the project in a strong position to incorporate external feedback productively.
