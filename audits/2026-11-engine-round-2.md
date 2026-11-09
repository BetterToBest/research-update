# Engine round 2: six improvements after S39 and S55 (Nov 9, 2026)

Raised by Duke in Chat on Nov 8, after the S39 and S55 reports. This note says why the round is needed, what each step builds, the order, and how the outside reviews feed in. Steps S56-S65 in `PLAN.md`; decision D18 in the ledger.

## Why

Three findings from the latest studies point at the same gaps:

- **The price rule decides the wealth results.** The engine passes all new money not matched by output into prices (pass-through 1, a labelled placeholder). S39 showed an outside model (BeforeIT.jl) gives pass-through 0, but by its own rule, so the check bounds the question without answering it. (Correction, Nov 9, S56: 0 and 1 are the two engines' assumptions, not bounds on the real pass-through, which could lie outside them.) Under C2.2 the engine's prices run about 35% a year, and that inflation is what erodes savings in every wealth result, including S55's open-access gain.
- **A falling Gini can mislead.** Under C2.2 (Reference, 10,000 adults, 20 years) the wealth Gini falls from 0.728 to 0.346, while median real wealth falls from about $212,000 to $43,000. The gap narrows from both ends: debt nearly disappears, but savings above the bottom lose their value to modelled inflation. The Gini alone cannot tell readers which.
- **The model cannot see concentration.** Starting wealth stops at the SCF's 99.5th percentile (about $10.8 million); savings earn no return; there is no business or property income; the only labour response is hours. So the model cannot show fortunes large enough to give leverage over wages, prices or politics, or whether the programme changes that. Duke's question (Nov 8): one person holding a billion while everyone else holds under $10,000 is very different from everyone else holding $500 million to $999 million, and the Gini does not separate them well.

## The six improvements (in the order they are built)

1. **Distribution measures (S57).** Reporting only, no rule change: top 1% and top 10% wealth shares, the Palma ratio, real wealth and income percentiles (P10 to P99.9), a growth-incidence curve (each percentile's gain or loss against no programme), mobility between wealth fifths, labour's share of income, and debt. Built first so every later step is measured with them. Guard: every published figure unchanged.
2. **A price rule that answers demand and capacity (S58).** Opened sources on the pass-through of large cash transfers and money-financed spending; a rule where prices respond to demand relative to capacity and output responds where there is slack; behind a switch (today's rule the default, bit-identical); its parameters sourced or labelled and swept. Also settles the conversion tax that is not netted from the unmatched money (S39 open item b).
3. **A top tail and returns on capital (S59).** A weighted top tail (a Pareto tail fitted to the SCF's top and the Forbes 400) so concentration can be measured without breaking the paired design; returns on savings that rise with wealth and business ownership, from opened sources; checked against the SCF and the Fed's Distributional Financial Accounts, never tuned to them.
4. **Bargaining power (S60).** A worker's outside option and an employer markdown (monopsony), so a Basic Unit can raise reservation wages, with sourced magnitudes; one wage elasticity for every change in the return to work (guardrail 7).
5. **Baseline scope (S61).** Adults outside the labour force (caregivers, disability, students, early retirees) at CPS shares; a spending rule that stops the debt drift (S34; issue I15), chosen by a preregistered criterion from sourced behaviour.
6. **PTF realism (S62).** Sourced cost structures for not-for-profit grocers, utilities and childcare (the operations limit); PTF jobs and wages, including the conversion bonus the Hub gives to PTF workers.

Every mechanism follows the engine's guardrails: behind a switch, off = bit-identical (guard test), CRN-paired on seeds 1-500 in all three environments, the eight-draws-per-agent-year guarantee kept, no constant tuned to a target, limits reported.

## Then

- **S63 · Preregister and freeze round 2.** Each new switch first appears as a labelled reading beside the main row. Which readings join the main row is fixed before any result (ledger decision). Outcomes include S57's measures. Dry run at 2 seeds; run manifest amendment.
- **S64 · Run and report round 2** on GitHub Actions (free), one report per preregistered question, nulls included.
- **S65 · Release 2:** tag, hashes, changelog, findings page; S40's generator refreshes every Hub figure from the new release.

## How the outside reviews feed in

The audit prompt (`audits/2026-11-s39-s55-audit-prompt.md`, also a Project doc) asks outside AI systems to review S39, S55 and the inequality measures, and to help with each of the six improvements: evidence, sources, parameter ranges, model designs. **S56 is Duke's step:** run the prompt in two or more systems and paste the replies back, in Chat in this Project or in a Claude Code session started with `/start-session S56`. Claude then triages every point (accept, adapt or decline, each with a reason) into `audits/2026-11-s39-s55-review-triage.md`, edits the S57-S65 plan, and files a ledger decision for anything that would change the design rather than the model of it. S58-S62 wait on S56 so their designs can use the reviews; S57 does not.

**Done Nov 9 (S56):** Grok and ChatGPT replied; the triage is `audits/2026-11-s39-s55-review-triage.md`. It adds S66 (trace the low end of S55's fixed-share curve), moves S60 after S61, folds the reviews' sources and tests into S57-S63, and files D19 and D20. D18 was answered Nov 9: everything on the Hub that cites simulation figures waits for S65.

If Duke would rather not wait for the reviews, he writes "start round 2 without the reviews" in the ledger's message box, and S58 starts.

## The order against the release (D18)

S7 (the release of today's engine) goes ahead as planned: it carries S36-S39, S5 and S55, with the D17 wording on inflation. The question for Duke is what waits for round 2. Default (D18): the Hub's corrections (S24), abstracts and bodies (S25) and generated figures (S40) proceed on the S7 release, since S40's blocks regenerate by release tag; the Hub v2 fresh-eyes review (S44), the advocacy kit (S45) and the hand-back to NEEC (S8) wait for release 2 (S65), so nothing is launched as Hub v2 on the placeholder price rule.
