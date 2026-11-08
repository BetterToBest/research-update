# Preregistration addendum: open PTF access (S55, studies T, U, V, W, Y)

Committed Nov 8, 2026 by S55 part 2, before any run of these rows. It adds studies to the study programme (`prereg/2026-11-study-program.md`, its Amendment 11 points here) and to the community-layer addendum (`prereg/2026-11-community-layer.md`, its Amendment 2). It changes nothing already fixed or run there: the frozen batch (S48) and the reports built on it (S36, S38) stand as published. Engine: BetterToBest/compassionism-simulation at commit `0c93593e1ea502555387e42215b79f290a60f127` (pull request 82: the growth rule behind `PTF_ACCESS: 'open'`; part 1 was pull request 81). With `PTF_ACCESS` off (`'members'`) that engine reproduces the frozen engine `ce8d030` figure for figure (guard test; engine lineage), so the rows below are paired with the frozen batch's rows on the same seeds. The reading behind every choice: research-update `audits/2026-11-ptf-access.md` (Duke's answers, ledger D16), and in compassionism-simulation `dev/reports/s55-ptf-access-reading.md`, `dev/reports/s55-ptf-growth.md` and `dev/DECISIONS.md` (S55, parts 1 and 2).

## Why
In the design anyone may shop at a Public Trust Foundation (PTF) business, in dollars or Basic Units, at one posted price (Duke, Nov 7). Until now the model let only PTF members pay PTF prices, and its two density tests (the food price cut is smaller below 40%; the synergy coefficient θ is zero below 55%) counted members. Under open access every adult in a zone buys the zone's PTF share of essential sales at PTF prices, and both tests read that share. The share starts at the environment's starting share and grows as far as capacity (capital), operations and market demand allow. Duke also asked for the whole response curve: the share held at 10% to 100%.

## Plain-words summary
- **Q24 (primary).** What does open access change, against the members-only model, in the full design's results?
- **Q25.** Do the five parts of the design interact differently under open access (the synergy table)?
- **Q26.** Do the community layer's findings (Q7-Q10) change under open access?
- **Q27.** How do the results change with the PTFs' share of essential sales held at 10%, 20%, ..., 100%? Is there a step at the 40% and 55% tests?
- **Q28.** Which of capacity, operations and demand limits the share's growth, by environment and year, and how much do the answers depend on the growth rule's settings?
- **Headline cell, fixed now:** Reference environment, **10,000 adults**, 20 years, the C2.2 design, CPS earnings yardstick, octave raise off: open access (growth on, main values) against the same row with members only (study A's row, same seeds). Every 500-adult figure is shown beside it.
- Five studies, about 108 runner-hours on GitHub Actions (free). A pilot at seeds 1-50 runs first, labelled pilot throughout.
- Every cell is published, including null and unfavourable results, all three environments.

## Checks made before writing this (no outcome value was looked at)
On the session machine, seeds 1-2, 500 adults, 20 years, the frozen release and C2.2 rows. Only the access diagnostics were printed (the PTFs' share of sales, capacity, which limit binds), never an outcome:
1. With the switch off the engine is the frozen engine: guard test identical (25 release-panel rows, seeds 1-20, 483 outputs, three environments) and engine lineage proven. The access unit tests pass (8: four from part 1, four for the growth rule, one per limit binding alone plus the sharing of capacity between zones by hand).
2. Reference, release design, growth on: the share follows capacity (about 33% at year 5) and stops at the 49% demand ceiling before year 10. Zones pass the 40% test partway through the run and never the 55% test. Stress, release design: capacity binds the whole run (about 12%, 19% and 40% at years 5, 10 and 20). With demand at 100% the Reference share reaches 100% by year 20. Under outside running costs no zone grows.
3. Sales at the Hub's PTF prices cover 65.2% of running costs at outside margins below the 40% test and 47.2% above it (the operations limit's outside reading). In the Hub's own cost structure prices are set at cost, so the limit cannot bind in the main reading. This is stated as a property of the rule, not found by a run.

## Questions
- **Q24 Open access.** For each primary outcome: the release row under open access minus the same row with members only (paired, same seeds), and each row's effect against no programme. Answer: both, with intervals, both designs, at 500 and 10,000 adults, 20 and 40 years, three environments.
- **Q25 Synergy under open access.** The study programme's Shapley shares and interaction contrasts (Analysis, unchanged), computed on the factorial with the 16 cells that include PTF run under open access. Cells without PTF and the none row are unchanged by the switch (part 1's unit test) and are taken from study B (or B10). Answer: the tables, and each part's Shapley value and each pair contrast minus its members-only value (B or B10), with intervals. The pairs the change bears on: PTF × SZH (θ now reads the share of sales) and PTF × CCO.
- **Q26 The layer under open access.** The community-layer addendum's Q7, Q8, Q9 and Q10, with every row that includes PTF run under open access: each answer, and its difference from the members-only answer (studies G, G10, H, I, J), with intervals.
- **Q27 Response curve.** The release row with every zone's share held at 10%, 20%, ..., 100% (growth off, `pa: {fix}`): each level's effect against no programme and against the members-only row, with intervals; and the steps across the two tests: the change from 30% to 40% and from 50% to 60%, each minus the mean of the two neighbouring steps (20% to 30% and 40% to 50%; 40% to 50% and 60% to 70%).
- **Q28 Growth.** Which limit stops the share growing (`paCap`, `paOps`, `paDem`: the share of adult-years from year 1 in zones where capacity, operations or demand bound), the share's path (`paS5`, `paS10`, `paS19`, `paS39`) and capacity's (`paC5` to `paC39`), by environment, design, size and horizon. And the open-access effect (Q24) under each swept setting of the growth rule: demand 25%, 75% and 100%; no capacity limit; outside running costs; and growth off (the share held at its start, part 1's reading).

## Design

### Rows
Every row is built as in the study programme and the run manifest (section 1: the frozen engine, `frozenRow`, both designs with the C2.2 design as headline), CPS yardstick (`lt: {s: 'all', m: 'all'}`), octave raise off, no ageing, unless a row says otherwise. Open access is the row option `pa` on the programme row (element 1). The none row has no PTF, so it is unchanged by the switch, and every none row comes from the matching frozen-batch study (same engine figures, same seeds).

| Switch | Setting | How it is set |
|---|---|---|
| Access | members (frozen batch) / **open, growth on, main values** | `pa: 'open'` = `{grow: true, cap: 'own', ops: 'hub', dem: 0.49}` |
| Demand ceiling (design parameter) | **0.49** / 0.25 / 0.75 / 1 | `pa: {dem: x}` |
| Capacity | **own capital** / none | `pa: {cap: 'none'}` |
| Operations | **the Hub's cost structure** / outside running costs | `pa: {ops: 'outside'}` |
| Growth | **on** / off (held at the start) | `pa: {grow: false}` |
| Fixed share (growth off) | 10%, 20%, ..., 100% | `pa: {fix: q}` |

### Studies
Seeds 1-500, paired across rows and with the frozen batch's rows. Reference, Adverse, Stress. Rows counted per environment, both designs.

| Study | Questions | Rows | Adults | Years | Rows per environment | Pairs with | Runner-hours (estimate) |
|---|---|---|---|---|---|---|---|
| T open access | Q24, Q28 | the release row, open | 500 and 10,000 | 20 and 40 | 2 | A | 6 |
| U open factorial | Q25 | the 16 architecture cells with PTF, open | 500 | 20 and 40 | 32 | B | 4 |
| U10 at scale | Q25 (headline synergy) | the same 16 cells, open | 10,000 | 20 | 32 | B10 | 27 |
| V open layer | Q26 | the layer rows of G (the 16 cells with PTF), H (9) and I (6), open | 500 | 20 and 40 | 62 | G, H, I | 12 |
| V10 open layer at scale | Q26 (headline) | G10's 16 cells, open | 10,000 | 20 | 32 | G10 | 31 |
| VJ open layer, other sizes | Q26 (Q7 at scale) | the release row with the layer, open | 2,000 and 10,000 | 20 and 40 | 2 | J | 7 |
| W fixed-share sweep | Q27 | the release row at 10%, ..., 100%, growth off | 500 | 20 and 40 | 20 | A | 3 |
| W10 sweep at scale | Q27 (headline) | the same 10 levels | 10,000 | 20 | 20 | A | 17 |
| Y growth settings | Q28 | the release row, open, with demand 0.25, 0.75, 1; no capacity limit; outside running costs; growth off | 500 | 20 and 40 | 12 | A, T | 2 |

Estimates from the frozen batch's measured cost (run manifest section 3): about 0.13 runner-hours a row at 500 adults (three environments, both horizons; 0.19 with the layer), 0.85 at 10,000 adults for 20 years, 2.1 for 40 years. Total about 108 runner-hours. The G rows with the released-wages yardstick and with the raise on are not repeated under open access (the layer addendum's headline is CPS, raise off).

### Where it runs
GitHub Actions, the `run-study` workflow of compassionism-sim-results (`prereg/RUNNING.md`). The job script `runner/jobs/program.js` gains `--study=T|U|U10|V|V10|VJ|W|W10|Y` and the access keys (`PA_KEYS`), with a check of its row counts (the table above) and that its rows equal the frozen batch's rows with `pa` removed. Results folders `prog-<study>-<engine, 7 characters>`, each with `run.txt`, `SHA256SUMS` and `DONE`. Shards as the run manifest's Amendment 6 sets out.

### Pilot first
Seeds 1-50, 500 adults, 20 years, three environments, for T, U, V, W and Y (folders `pilot55-<study>-<engine>`), labelled pilot throughout and never a headline figure. T's pilot also runs the members-only release rows: they must equal study A's values for seeds 1-50 byte for byte (the pairing check). If the pilot needs a change to any row, outcome or rule, that is a dated amendment below before the 500-seed run.

## Outcomes
The programme's five primary outcomes and its secondary outcomes, read and reported the same way. Beside every open row, as diagnostics, never as headline: the access keys `paSh` (the population's PTF share of essential sales, mean over years), `paLo` and `paTh` (adult-years in zones below the 40% test and above the 55% test), `paCap`, `paOps`, `paDem`, `paCv` (sales at PTF prices over running costs at outside margins), the share path `paS5` to `paS39` and capacity `paC5` to `paC39`; and the PTF's `pfMem` (members, % of adults) and `pfCut` (the mean PTF price cut, over every adult under open access).

## Analysis
As the programme (paired bootstrap over seeds, 10,000 replicates, seed 20261101, one resample per study and size shared by its rows and by the frozen rows it pairs with). Q24's contrast is the paired difference of the open row and the members-only row. Q25 and Q26 recompute the programme's and the layer addendum's tables with the open rows in place of the members-only rows that include PTF. Holm's correction is stated within each family: the five primary outcomes for Q24; the 11 contrasts per outcome for Q25; as the layer addendum for Q26; the 10 levels per outcome, and the two threshold steps per outcome, for Q27; the six swept settings per outcome for Q28.

## Decision rules
The programme's rules 1 to 9 and the layer addendum's rules 1 to 6 apply unchanged. In addition:
1. **Open access's effect** on an outcome is stated only where its interval excludes zero, and called *material* only at 1 percentage point or more (outcomes 1-3 and 5) or 5% of the members-only row's cost (outcome 4). The headline sentence comes from the headline cell (10,000 adults). Where the 500-adult figure leads to a different decision, the report says so.
2. **The growth rule's settings.** The demand ceiling is a design parameter; its main value (0.49) stays the headline whatever the swept rows show. For each swept setting the report says whether any decision under rule 1 differs from the main-value row; if one does, the headline sentence says the result depends on that setting and names it. No setting is chosen, or re-chosen, after a result is seen.
3. **Which limit binds** is reported as measured (Q28), by environment and year. The operations limit cannot bind in the main reading (the Hub prices at cost), and the report says so; its outside-cost reading is reported beside it.
4. **Response curve.** A level's effect is stated as in rule 1. A *step* at a test is claimed only where the threshold contrast of Q27 has an interval excluding zero and is at least 1 percentage point. The curve is read as a response to the share, separately from how fast a real network would grow (Duke, D16).
5. **Synergy** follows the programme's rule 2 on the open factorial. A change in a part's Shapley value or a pair contrast between open access and members only is stated only where the difference's interval excludes zero.
6. **What a null means.** If open access changes no outcome materially, the report says that letting every adult buy at PTF prices for the zone's share, with both tests reading that share, does not change the results in this engine. That is a finding about the mechanism as modelled, not about real PTFs.

## Reporting
Every cell of T, U, U10, V, V10, VJ, W, W10 and Y is published in compassionism-sim-results (per-seed values of every measure kept) and on the findings page beside the members-only tables, with the access diagnostics. S55 part 3 writes the report: open against members on every preregistered outcome, nulls included; the fixed-share curve with intervals; and which of capacity, operations and demand binds, by environment and year. The limits stated on the findings page: the demand ceiling is a labelled design parameter; capacity is counted for the population, not by zone; the share never falls; shopping in another zone is not modelled; the conversion-rate bonus stays with members, and the model has no PTF workforce; the price cuts and density tests are the Hub's figures, used as given.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
