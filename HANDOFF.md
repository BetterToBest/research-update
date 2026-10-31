# Handoff (Oct 31, 2026): S37 community and zone layer, done

## Step status
S37 **done**. The layer is built behind a switch (off by default, every earlier figure unchanged), and its preregistration addendum is committed. No study row with the layer has been run. Its rows run in the full batch (S48) after S47 freezes the design.

## What shipped
- compassionism-simulation [#52](https://github.com/BetterToBest/compassionism-simulation/pull/52), merged as `c9d5287`:
  - The switch `COMM` (study row option `cl`), with the reading `dev/reports/community-layer.md` and the decisions in `dev/DECISIONS.md` (S37).
  - A unit test (one community equals the layer off), and an engine lineage link (the 12-seed release panels unchanged).
- Earlier in this session: compassionism-simulation [#51](https://github.com/BetterToBest/compassionism-simulation/pull/51) (the S35 pilot report), merged with checks green.
- research-update (this repository):
  - `prereg/2026-11-community-layer.md`: the addendum, with studies G, G10, H, I and J, about 25 runner-hours, the headline at 10,000 adults.
  - Amendment 2 of `prereg/2026-11-study-program.md`, which points to the addendum.
  - `prereg/checks/s37_layer_checks.js`, and the S37, S38 and S47 sections of PLAN.md.

## What the layer is (Claude's reading of the design)
- **Why it was needed.** The Hub's BLEI paper puts the PTF density tests "in a given zone": the food price cut needs about 40% of residents to be members, and the synergy coefficient θ needs 55%. The engine read them on the share of all adults, 18% at the start, so they never passed. That is why the pilots found SZH inert.
- **What it does.** The layer reads the three tests (food price cut, θ, imitation) in each community of about k adults. With SZH on, it places the starting PTF members together in zones where members are a share f of the residents. Who is a member does not change.
- **Design parameters, each swept:** k 100 (50, 250); f 0.5 (2/3, 1; the Hub's survey majority); zones need CIP, no (yes); imitation local (population-wide).
- **CIP.** In the main reading zones form without CIP, so that any CIP and SZH synergy comes from a mechanism, not from a rule written in. The Hub's literal rule (zones only with CIP) is a sweep row, labelled as such.
- **Not modelled:** PTH density (the Hub gives only a household count, 30-40, which a sample of adults cannot show), moving between zones, capacity by zone, cross-zone shopping.
- **Checks:**
  - One community equals the layer off on every measure, in three environments, at 20 years and at 40 with ageing.
  - Rows without PTF are unchanged.
  - Guard test, validate, unit (223), domtest (153) and the glossary check pass.
  - No outcome value was looked at.

## In flight
Nothing running.

## Decisions waiting
None. The CIP reading above is a modelling assumption (both readings are preregistered). If Duke thinks it misrepresents the design, that is a ledger decision for a later session.

## Next step
**S6** (C2.2 coverage and adequacy), opus, high: next in the Order table. S14, S13 and S50 follow; all must finish before S47.

## Pitfalls
- The study row option `cm` is the conversion model; the layer is `cl`.
- At 500 adults zones are coarse (5 communities): about half the members reach the 40% test with k 100. That is why the addendum's headline is at 10,000 adults.
- S47 must add studies G to J to the job script `runner/jobs/program.js`, and keep the layer's keys, before its dry run (PLAN.md, S47).
- Commit trailers: this project forbids model names. Use `Co-Authored-By: Claude <noreply@anthropic.com>`, not the default trailer.
- The results repository is large: clone it with `--filter=blob:none --sparse`.
