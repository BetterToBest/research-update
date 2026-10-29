# What changed in the formal model (S46)

Oct 29, 2026. Edits to five Research Hub papers (research-hub branch `claude/s46-formal-model`), with their PDFs rebuilt from the HTML by `tools/build_pdf.js`. They answer the refine.ink audit of the mechanism-design paper (items A01-A07) and three compendium items from the S29 triage (B001/B053, B023/B072, B076).

## In plain words

The mechanism-design paper's math said more than it proved. Its budget counted the Basic Units a person converts twice. Its first-order conditions were mis-stated. Its main welfare claim, that the system is a Pareto improvement, rested on an assumption it never showed. Two lemmas claimed more than their proofs gave. The same Greek letter meant two different things. All of this is now fixed. The Pareto claim becomes a proposition that says exactly when no one would be worse off than under today's transfers. It also reports what the simulation's current release finds: every group has more real resources, but every group ends with less wealth (more adults under $25,000 of net wealth). So a Pareto improvement is not established, and the paper now says so.

In the companion papers:
- The development paper's theorem promised poverty below 5% within 15 years, while its own proof gives 11.8% and 7.4%. The theorem now states what the proof shows.
- The modelling paper's stability index is now unit-free.
- Its "diminishing returns above 80% participation" is marked as unsupported, because the network function the papers use is convex.
- The network weights are labelled as assumptions.
- The dual-currency paper's equilibrium theorem is scoped to one market.

## Changes, paper by paper

**Optimal Transfer Design** (`optimal-transfer-design.html`)
- 4.1: one basic-unit budget, b<sup>s</sup> + b<sup>c</sup> ≤ B₀ + E: units spent plus units converted, out of the allocation plus units received as payment. Conversion is capped at C(O), which doubles with each octave, and needs a recognised contribution. Essentials are bought with spent units; primary consumption is wage income plus M(q) × converted units. Each unit is counted once (A03).
  - *Modelling assumption (Claude's reading of the design):* the Hub describes converting one's own units "through productive activities" (glossary) and businesses converting units received as payment (front page). The model allows both. This differs from the plan's B<sub>spent</sub> + B<sub>conv</sub> ≤ B₀ only by counting units received as payment, which are zero for someone who sells nothing.
- 4.2: M(q) = min(9, max(1, 1 + q/10)). The Phi-rate multiplies it (M<sub>φ</sub> = 1.618 × M, top rate ≈ 14.56), replacing the undefined "quality_factor".
- 4.4 (new): first-order conditions for spending or converting a unit (β/c<sup>b</sup> = αM/c<sup>p</sup> while the cap is slack, ≤ when it binds), for paid work (αw/c<sup>p</sup> = γ/l) and for contribution time. Extra quality pays nothing above M = 9 or for someone who converts nothing (A02).
- 5.1: "Pareto Efficiency Conditions" becomes **Proposition 1**, with a proof (A01). If the program replaces today's means-tested transfers, and (a) the essentials the allocation buys, which each person would otherwise have paid for, are worth at least what those transfers give them at every earnings level, (b) conversion is optional and (c) financing lowers no one's after-tax income or prices, then no one is worse off. Condition (c) does not hold for any financing the Hub specifies.
- 5.1 also reports Compassionism Simulation v5.6.0 (commit `5bf5bcc`; 500 paired seeds, 20 years; its command). Every group has more real resources than under today's policy, and fewer adults fall below the cost of living (19.5% against 49.3%, Reference). But every group is worse off on wealth: 44.4% end with under $25,000 against 32.7%, and the same holds in all three environments. The release reports groups, not the share of individuals better off on every measure; the preregistered program should add that share (S32/S36).
- 6.2: the expected-wealth figure ($68,500 with an interval) is withdrawn; no run produced it (S23, S30).
- 9: "Mathematical analysis confirms Pareto improvements ... Monte Carlo simulations demonstrating robustness" now reads as the conditional result and the release finding.
- Appendix A.1: risk aversion renamed κ (γ is the leisure weight) (A07). The distributions are described as proposed, since no run with them exists (S30).
- B.1: Lemma 1 restated for this model's largest reachable conversion income, M(q) × min(B₀ + E, C(O)). It is weakly increasing, strictly in quality only for 0 < q < 80, and strictly in the octave only while the cap binds (A06).
- B.2: Lemma 2 scoped to one market in partial equilibrium, with its assumptions stated (A04).

**Community-Based Monetary Innovation** (`community-monetary-development.html`)
- 3.3: the theorem "poverty converges to p* < 0.05 within finite time" becomes a proposition that does follow from the proof. Poverty converges geometrically to p* = λ<sub>fall</sub>/(λ<sub>escape</sub> + λ<sub>fall</sub>). With the paper's assumed rates that is 11.8% (CCO) and 7.4% (with PTF), with half-lives of 3.72 and 2.20 years. A rate starting above p* never reaches 5% (B001). The "within 15 years" formula is shown to need a starting rate of 82% (B053).
- Abstract, meta description and conclusion: "below 5% within 15 years" replaced by the steady states, marked as conditional on assumed rates. (The NPV of $1,847, B097, is left for the corrections package, S24.)

**Economic Modeling and Simulation** (`economic-modeling-simulation.html`)
- Appendix A: Stability = 1 − SD/Mean (one minus the coefficient of variation). The old 1 − Var/Mean carries units (B076).
- 7.1: "80%+: diminishing returns" marked as produced by no model. V(n) = k₁n² + k₂n log n is convex (V″ = 2k₁ + k₂/n > 0), so it cannot give diminishing returns without a cost term no paper specifies (B023).

**Integrated Digital Governance** (`integrated-digital-governance.html`)
- 4.4: k₁ = 0.3 and k₂ = 0.7 labelled as assumed design parameters; V(n) is convex at every scale (B072).

**Dual Currency Systems and Inflation** (`dual-currency-inflation.html`)
- Appendix A.1: Theorem 1 scoped to one sector's market (partial equilibrium), with its assumptions. Capacity constraints alone do not make excess demand strictly decreasing (A04).

## PDFs

`node tools/build_pdf.js <page.html>` prints each page to `papers/pdfs/<page>.pdf` with headless Chromium and the page's own print styles; outside requests are blocked. All five PDFs were rebuilt. The old PDFs were earlier versions with errors that existed only in the PDFs (A02, A03, A05, A08). The rebuild drops their PDF-only material, as the claims ledger counts it: optimal-transfer-design 43 figures, community-monetary-development 77, economic-modeling-simulation 118, dual-currency-inflation 91, integrated-digital-governance 56. Most of it was already marked to correct or remove: the printed code, Monte Carlo tables with no run, and the welfare decomposition. The HTML page is the paper of record.

## Claims ledger

`data/claims.csv` was regenerated: 6,655 figures. The release figures quoted in Proposition 1 are classed "simulation", with their command. The new steady states are "derived" (recomputed). The correction notes are "corpus metadata".

## Not changed here (left to S24/S25)

- Wording items (A13 "eliminates benefit reduction entirely").
- The NPV of $1,847 (B097).
- The modelling paper's simulation results, which S30 found no code produced.
- The papers' other figures.
