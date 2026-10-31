# Preregistration addendum: the community and zone layer (S37, for S38)

Committed Oct 31, 2026 by S37, before any run of the layer's rows. It adds studies to the study programme (`prereg/2026-11-study-program.md`, its Amendment 2 points here) and changes nothing already fixed there. Engine: BetterToBest/compassionism-simulation at commit `c9d52877d77ca9b75bfdda8745a0caae7227f24c` (pull request 52: the switch `COMM`, row option `cl`, off by default; guard test identical). S47's design freeze pins the commit the full batch runs on. Claude's reading of the design, and every choice behind the layer: compassionism-simulation `dev/reports/community-layer.md` and `dev/DECISIONS.md` (S37).

## Why
The pilots (S35) found the community businesses (PTF), community housing (PTH) and zone coordination (SZH) close to inert, and nothing in the engine depending on place. Without a mechanism, a synergy study can only report "no synergy". The Research Hub sets two density tests for PTF "in a given zone": the food price cut needs about 40% of a zone's residents to be members, and the synergy coefficient θ needs 55%. It also says SZH organizes where the PTF is deployed. The layer models both: it reads the density tests in each community, and with SZH it places the PTF's starting members together in zones. These studies ask what that changes.

## Plain-words summary
- Four questions: does the layer change what the full design achieves (Q7)? Do the five parts do more together than apart once density counts (Q8)? How much do the answers depend on the layer's four design parameters (Q9)? Does the PTF's starting size matter more with the layer (Q10)?
- **Headline cell, fixed now:** Reference environment, **10,000 adults**, 20 years, the release row with the layer against the release row without it, CPS earnings yardstick, octave raise off. Reason: at 500 adults there are only five communities, so zones are coarse. 10,000 adults give 100. Every 500-adult figure is shown beside it, labelled coarse.
- Five studies, G, G10, H, I and J, about 25 runner-hours on Actions (the programme's batch was about 230).
- Every cell is published, including null and unfavourable results, all three environments.

## Checks made before writing this (no outcome value was looked at)
`prereg/checks/s37_layer_checks.js` (run in an engine checkout on the S37 branch; seeds 1-2; 60 to 400 adults) prints only whether each setting runs, which settings give bit-identical results, and the layer's own placement figures (communities, zones, where members live). Its output, which this design rests on:
1. **One community equals the layer off** on every measure, in all three environments, at 20 years and at 40 years with ageing. So the layer's effect is measured against the same engine, and k is a resolution, not a new mechanism.
2. **Without PTF the layer changes nothing.** The no-programme row, and a row with CCO but no PTF, are bit-identical with the layer on and off. So the 15 architecture cells without PTF, and the none row, are those of study B and are not run again.
3. At 400 adults the layer changes the release row, and it runs with every swept setting. Zones form only with SZH and PTF on. With `zc: true` and CIP off, none form.
4. **Placement at 400 adults (k 100):** 4 communities, 2 zones at the start in Reference and Adverse, 1 in Stress. About half the members live where the share is at least 40% (Reference, over the run). That is about three quarters with k 50, and a third with k 250. This coarseness at small populations is why the headline is at 10,000 adults.

## Questions
- **Q7 Layer effect.** For each primary outcome: the release row with the layer minus the release row without it (paired, same seeds), and the release row's effect (against none) with the layer. Answer: both, with intervals, at 500, 2,000 and 10,000 adults, 20 and 40 years, three environments.
- **Q8 Synergy with the layer.** The Shapley shares and interaction contrasts of the study programme (Analysis, unchanged), computed on the factorial with the layer on. The 16 cells with PTF come from study G (or G10), the 15 without PTF and the none row from study B (or B10). Answer: the tables, and each part's Shapley value and each pair contrast minus its value with the layer off (study B or B10), with intervals. The pairs the layer is built to test are PTF × SZH and CIP × SZH.
- **Q9 Design parameters.** For the release row with the layer: the effect of the zone member share f (0.5; 2/3 and 1), the community size k (100; 50 and 250), local against population-wide imitation (`bass`), and zones that need CIP (`zc`, on the four cells with PTF and SZH on and CIP off). Answer: each row's effect against the main-value row, with intervals.
- **Q10 PTF starting size.** The release row with and without the layer at a PTF starting share of 10%, 30% and 50% (beside the environment's own: 18% in Reference and Adverse, 8% in Stress). Answer: the layer's effect at each share, and whether it is larger where the PTF starts small (the Hub's case for zones: "Phase deployment beginning in high-density urban zones").

## Design

### Rows
Every row is built as in the study programme (Rows), on the main row (element 1 of `relMainCfgs`), with `c.cl` set. `c.cl = {}` gives the main values `COMM_DEFAULTS = {k: 100, f: 0.5, zc: false, bass: 'local'}`. The none row is identical with or without the layer (check 2) and is taken from the matching programme study. All rows: CPS yardstick (`c.lt = {s: 'all', m: 'all'}`), octave raise off, no ageing, unless a row says otherwise.

| Switch | Setting | How it is set |
|---|---|---|
| Layer | off / **on (main values)** | `c.cl = {}` on the main row |
| Zone member share f | **0.5** / 2/3 / 1 | `c.cl = {f: 2/3}`, `{f: 1}` |
| Community size k | **100** / 50 / 250 adults | `c.cl = {k: 50}`, `{k: 250}` |
| Imitation | **local** / population-wide | `c.cl = {bass: 'pop'}` |
| Zones need CIP | **no** / yes | `c.cl = {zc: true}` |
| PTF starting share | environment's own / 10% / 30% / 50% | `P.ptfShare` set before `tbPresets(P)` (the none row has no PTF, so it is unchanged) |

### Studies
Seeds 1-500, paired across rows. Reference, Adverse, Stress. Rows counted per environment.

| Study | Questions | Rows | Adults | Years | Rows per environment | Runner-hours (estimate) |
|---|---|---|---|---|---|---|
| G layer synergy | Q7, Q8 | the 16 architecture cells with PTF, layer on; plus the release row with the layer under the released-wages yardstick, and with the raise on | 500 | 20 and 40 | 18 | 2.7 |
| G10 layer synergy at scale | Q7, Q8 (headline) | the 16 cells with PTF, layer on | 10,000 | 20 | 16 | 16.4 |
| H design parameters | Q9 | release row with the layer at f 2/3, f 1, k 50, k 250, bass 'pop'; the four cells with PTF and SZH on and CIP off, with `zc: true` | 500 | 20 and 40 | 9 | 1.4 |
| I PTF starting size | Q10 | release row at PTF share 10%, 30%, 50%, layer off and on | 500 | 20 and 40 | 6 | 0.9 |
| J layer at scale | Q7, Q1 | release row with the layer | 2,000 and 10,000 | 20 and 40 | 2 | 4 |

Estimates from the pilots' measured cost (S35 report, section 1), 500 seeds, 2 processes per runner: a row costs about 0.15 runner-hours at 500 adults (three environments, both horizons), about 1 at 10,000 adults for 20 years and about 2 for 40 years, and about 0.7 at 2,000 adults for both horizons. Total about 25 runner-hours, all on Actions. The rows without the layer that these studies compare with are already in the programme: B (cells without PTF, and every cell with the layer off, 500 adults), B10 (10,000 adults), A (the release row at 2,000 and 10,000 adults) and the none rows. If S47 drops the separate 20-year rows (S35 report, section 9, item 4), these studies follow the same rule.

### Where it runs
GitHub Actions, as the programme: the job script `runner/jobs/program.js` gains `--study=G|G10|H|I|J` and keeps the layer's keys (below). It lands, with a check of its row counts (G 18, G10 16, H 9, I 6, J 2 per environment and horizon run), before S47's dry run. Results folders `prog-<study>-<engine, 7 characters>`, each with `run.txt`, `SHA256SUMS` and `DONE`. No pilot of these rows is planned: S47's 2-seed dry run checks that each runs and its outputs load.

## Outcomes
The programme's five primary outcomes and its secondary outcomes, read and reported the same way. Beside every row with the layer, as diagnostics, never as headline: the layer's keys `clN` (communities), `clZ` (zones at the start), `clSd` (how much the member share varies between communities, points), `clHi` (share of members living where the share is at least 40%), `clTh` (the same where θ is above zero), and the PTF's `pfMem` (members, % of adults, mean over years) and `pfCut` (members' average price cut).

## Analysis
As the programme (paired bootstrap, 10,000 replicates, seed 20261101, one resample per study and size shared by its rows). Comparisons between a study's rows and rows from another study at the same size (for example G against B) use the same seeds and are paired; the bootstrap resamples the seed indices once for the pair of studies. The layer's effect (Q7) is the paired difference of the release rows with and without the layer. Comparisons across sizes are independent runs, as in the programme. Holm's correction is stated within each family: the five primary outcomes for Q7; the 11 contrasts per outcome for Q8; the nine rows of study H per outcome for Q9; the three shares per outcome for Q10.

## Decision rules
The programme's rules 1 to 9 apply unchanged. In addition:
1. **The layer's effect** on an outcome is stated only where its interval excludes zero. It is called *material* only at 1 percentage point or more (outcomes 1-3 and 5) or 5% of the release row's cost (outcome 4). The headline sentence comes from the headline cell (10,000 adults). Where the 500-adult figure leads to a different decision, the report says that the result depends on how finely zones are resolved.
2. **Synergy with the layer** follows the programme's rule 2 on the factorial with the layer. The synergy table's headline is G10 at 10,000 adults (20 years). G at 500 adults gives 40 years and stands beside it. A CIP × SZH synergy found only with `zc: true` is reported as coming from the design's own rule (zones need CIP), not as a finding.
3. **Design parameters.** For each swept row, the report says whether any decision under rule 1 or the programme's rule 1 differs from the main-value row. If one does, the headline sentence says the result depends on that design parameter and names it. The main values stay the headline, whatever the swept rows show. No parameter is chosen, or re-chosen, after a result is seen.
4. **PTF starting size.** The layer's effect is said to depend on the PTF's starting size only where the difference between two shares has an interval excluding zero and is at least 1 percentage point.
5. **Scale.** The programme's rule 3 applies to the layer rows (J against G, G10 against G). Because the headline is already at 10,000 adults, a scale effect changes no headline. It is reported as the size of the coarseness at 500 adults.
6. **What a null means.** If the layer changes no outcome materially, the report says that reading the Hub's density tests locally, with zones placed as SZH places them, does not change the results in this engine. That is a finding about the mechanism as modelled, not about real zones.

## Reporting
Every cell of G, G10, H, I and J is published in compassionism-sim-results (per-seed values of every measure kept) and on the findings page beside the programme's tables, with the layer's diagnostics. S38 writes the report. The limits in `dev/reports/community-layer.md` (PTH density, moving between zones, capacity by zone and cross-zone shopping are not modelled; the thresholds and price cuts are the Hub's figures, used as given) are stated on the findings page.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
