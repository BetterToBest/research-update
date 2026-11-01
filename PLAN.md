# Plan: Simulation, Research Hub v2, then NEEC

Set up Oct 28, 2026 (planning chat, ledger step S27). Step IDs are the ledger's (project "Hub & Simulation", code H). NEEC steps keep their own IDs (N-S70 and so on). Start any step with `/start-session <ID>` in a session on this repository; end with `/end-session`.

Gates (a session never passes these on its own): an unanswered decision; anything that spends money (Runpod: only S48, after the S47 design freeze and once you have added the Runpod key); a step marked (you).

Model and effort per step are below. "fable" means: use it only if it uses no usage credits; otherwise use the model named first.

## Order

| # | Step | What | Model | Effort | Waits on |
|---|---|---|---|---|---|
| 1 | S28 | Wiring: repositories, merge rule, ledger pointers; closes S9, S17, S18 | sonnet | medium | |
| 2 | S2 | Tag Hub v1 and the cited Simulation release; build the /v1/ archive | sonnet | medium | D1 (default proceeds) |
| 3 | S29 | Verify the refine.ink audits against today's Hub | opus | medium | |
| 4 | S23 | Claims ledger: every Hub figure classed by basis (may take 2 sessions) | opus | high | S29 |
| 5 | S30 | Where the early figures came from: rerun published code and pre-v5 engines | opus | high | S23 |
| 6 | S31 | Chat-history provenance of figures with no code basis | sonnet | medium | your chat exports (D2), S30 |
| 7 | S46 | Repair the formal model (mechanism-design paper and compendium math) | opus | xhigh | S29 |
| 8 | S10 | Second, independent implementation of the yearly loop (Python) | opus | xhigh (or fable, high) | |
| 9 | S34 | The no-program baseline against outside data | opus | high | |
| 10 | S33 | Study runner on GitHub Actions; runtime benchmarks | sonnet | high | |
| 11 | S32 | Preregister the study program (scale, synergy, horizon, participation, community arm) | opus | high | S33, S34 |
| 12 | S35 | Pilot studies on Actions (free): scale and synergy at reduced seeds | opus | medium | S32 |
| 13 | S37 | Community and zone layer, if the pilots show it is needed (may take 2 sessions) | opus | xhigh (or fable, high) | S35 |
| 14 | S6 | C2.2 coverage and adequacy | opus | high | ledger decision if the design changes |
| 15 | S14 | Population-weighted cost-of-living line, audited | opus | high | |
| 16 | S13 | Outside audits: triage the Grok audit (I5) and audit the engine before the freeze | opus | high | S10 |
| 16a | S50 | Second, independent implementation of the release row (S10 covered only the validation presets) | opus | xhigh | S13 |
| 17 | S47 | Design freeze: every row and output the plan needs, dry-run at 2 seeds, cost estimate | opus | high | S10, S13, S50, S32-S37, S6, S14 |
| 18 | S48 | The full study batch (Actions where it fits, Runpod for the rest) | opus | medium | S47 and your Runpod key (gate) |
| 19 | S36 | Synergy report: Shapley shares, interactions, 20 and 40 years | opus | high | S48 |
| 20 | S38 | Community-layer report (if S37 built it) | opus | medium | S48 |
| 21 | S5 | Participation threshold: one figure, papers corrected | sonnet | medium | S48 |
| 22 | S39 | Outside engine cross-check (BeforeIT.jl), after the scale results | opus | high | S48 |
| 23 | S7 | Simulation release (tag, hashes, changelog, findings page) | sonnet | medium | S36, S38, S5 |
| 24 | S11 | BLEI visual series exported, visual suite rebuilt (S12 is yours) | sonnet | medium | S7 |
| 25 | S13 | Outside audits of the release (second round) | opus | high | S7 |
| 26 | S24 | Corrections package landed on the Hub, PDFs rebuilt | sonnet | medium | S2, S23, S29, S30 |
| 27 | S25 | Abstracts, then paper bodies, on corrected figures (several sessions) | opus | high | S24, S46, S7 |
| 28 | S40 | Hub figures generated from the release data, with a check | sonnet | high | S7 |
| 29 | S3 | OEIAS as the umbrella name | sonnet | medium | |
| 30 | S4 | X-cents folded into the CCO architecture | sonnet | medium | |
| 31 | S41 | Site and wiki design refresh | sonnet | high | S40 |
| 32 | S43 | Links and publications: portal, x-cents, NEEC, Academia papers | sonnet | medium | your Academia links (D3) |
| 33 | S42 | Machine-readable files regenerated from one manifest | sonnet | medium | S43 |
| 34 | S44 | Hub v2 fresh-eyes review | opus | high | S40-S43 |
| 35 | S45 | Advocacy kit from the release | sonnet | medium | S7, S44 |
| 36 | S15, S16 | CoMSES package and fact sheet; share and access kit | sonnet | medium | S7 |
| 37 | S19-S22 | Comparison items (optional; the comparison stays frozen) | opus | medium | S7 |
| 38 | S8 | Hand back to NEEC | sonnet | low | S7, S25, S44 |
| 39 | N-S70, N-S71, N-S72, N-S42, N-S44, N-S73, N-S43, N-S49, then S26 | NEEC v2 and v2.1, as the NEEC ledger orders them | opus | high | S8 |

## Steps

### S28 · Wiring: repositories, merge rule, ledger pointers
Repos: research-update, compassionism-simulation, research-hub, NormativeEvaluation, compassionism-sim-results.
1. Attach each repository (add_repo, access "push"). The edits below are also the test that you can open and merge a PR in each.
2. compassionism-simulation `CLAUDE.md`: replace "Duke's only jobs ... merge the pull request when its report reads right" with this repository's landing rule (Claude merges its own PR when checks pass; Duke reads reports at leisure and answers ledger decisions). Keep every guardrail. `.claude/commands/handoff.md`: point its ledger write at artifact F1hceP6XEfPQ1pf6Sw1Ki8, document `projects/hub`, and say to prefer this repository's `/end-session` when the session started here.
3. NormativeEvaluation `CLAUDE.md`: the same landing rule. NEEC stays paused; change nothing else.
4. research-hub: add a short `CLAUDE.md` (under 40 lines): what the repo is; surgical edits; research rule 5 (basis classes); keep bettertobest.github.io's machine-readable files in step; `/v1/` is frozen once S2 lands.
5. S9: read the open draft PR(s) on compassionism-simulation; merge if checks are green and the change matches its description (compare page restyled, history section removed); otherwise say why not.
6. S17: check the six clarity edits listed in ledger step S17 on the live pages; list any missing in HANDOFF.md as a small follow-up.
7. S18: map `dev/packets/` (s118 → S10, s119 → S15, s148 → S13); close S18 if nothing else remains.
8. Find the corrections package (C1-C30, ledger S24) and the claims-ledger draft (S23) in these repositories (grep "C23", "claims ledger", "Corpus metadata"). If they are not here, add a ledger decision asking Duke to bring them over from the other account.
9. Try to add `.github/workflows/links.yml` here (a link check of the Markdown files). Record in HANDOFF.md whether GitHub accepted a workflow file from the session; S33 depends on it.
10. Chaining test: with AUTOCHAIN.md on, `/end-session` creates the scheduled task for S2. Record in HANDOFF.md whether the tool was available, whether the first lines `/model` and `/effort` of a chained prompt took effect (the S2 session checks and records its own model), and whether the chained session opened this repository.
Done when: the PRs are merged; S9, S17, S18 resolved or explained; steps 8 and 9 recorded.

### S2 · Tag Hub v1 and the cited Simulation release; build the /v1/ archive
Repos: research-hub, bettertobest.github.io, compassionism-simulation (read only). D1 (confirmed): tag plus /v1/ archive pages, bannered and hidden from search engines.
1. Annotated tag `hub-v1` on research-hub main and on bettertobest.github.io main ("Research Hub v1, the source of NEEC v1's Compassionism entry, frozen at s84"), each with a GitHub release.
2. Confirm v5.6.0 on compassionism-simulation is the commit NEEC cites (ledger: d10ed6e); record both commits in HANDOFF.md.
3. Build `v1/` in research-hub from the tag: every page, the wiki and the PDFs. On every v1 HTML page: the D1 banner, `<meta name="robots" content="noindex">`, `<link rel="canonical">` to the live page; links rewritten to stay inside `/v1/`. Add "Version 1 (archived)" to the live footer.
4. `v1/README.md`: what v1 is, its tag, and that corrections are listed in the corrections log (created by S24).
Done when: tags and releases exist; a scripted check finds the banner and noindex on every v1 page; three pages and one PDF load over `python3 -m http.server`.

### S29 · Verify the refine.ink audits against today's Hub
Repos: research-update, research-hub (read).
Inputs: `audits/refine/presence_check.py` (145 comments, locators, Oct 28 checks). The full audit texts are in the claude.ai Project "Better To Best Research"; if this session cannot read the Project, work from the locators and the Hub text.
1. Run the presence check (`--csv audits/refine/triage.csv`). For "not found" rows, search by hand once (the locator may miss); for present rows, read the passage.
2. Judge each critique. Recompute every arithmetic point in `audits/refine/recompute.py`. Note where the audit is wrong (comment B097 already: neither the paper's $1,847 nor the audit's explanation matches its formula).
3. Classify: fixed / live, critique valid / live, critique wrong / moot. Severity: changes a headline figure / changes a derivation / wording only. Flag passages fixed in the HTML but still in the PDF (32 on Oct 28).
4. Write `audits/refine/triage.md`: summary counts, then the valid live items by severity, each with page and the correction needed. Append them to the corrections list S24 lands (or `audits/corrections-additions.md` if that package is not in these repos).
Done when: every row classified and recompute.py runs clean.

### S23 · Claims ledger: every Hub figure classed by basis
Repos: research-hub, research-update. Merge the other ledger's draft if S28 found it.
1. `tools/extract_claims.py` in research-hub lists every quantitative statement (percentages, money, multipliers, counts, years ahead) on every page and PDF, so none is missed.
2. Class each (research rule 5): simulation release + command; derived calculation (with its file); external source (URL, opened); design parameter; illustrative projection; corpus metadata; no basis found.
3. Write `data/claims.csv` (page, section, sentence, figure, class, source, action: keep / correct / relabel / remove, S29 id) and a summary with counts by class and the full no-basis list.
Done when: every extracted figure is classed. Split by paper across two sessions if needed; HANDOFF.md tracks where you stopped.

### S30 · Where the early figures came from
Repos: research-update, compassionism-simulation (history), research-hub.
1. From S23 take the figures classed "simulation" or "no basis": for example 85% and 98% poverty reduction, $37,000 and $82,000 median wealth (reported with a 95% interval), 65% lower inflation, "10,000 iterations", the elasticity table, Gini 0.28, the 30%, 55% and 75% participation thresholds, and the theta "Monte Carlo calibration" (I7).
2. Run the code the papers print (Appendix A of the modelling and transfer-design papers) as printed, at the stated parameters. Record whether it runs and what it outputs.
3. Recover each engine before v4.20 from compassionism-simulation's history (`git log --follow -- index.html`), run its reference preset on 100 seeds, and record headline outputs by version, beside the errors fixed later (v4.3-v4.4: wage scale, an undocumented ×0.85 cut to the no-program run's wealth, the gamma sampler; others in CHANGELOG).
4. `data/optimal-parameters.json` lists $82,000 under `pth_parameters` as "expected wealth building" (an input) while the papers report it as a result with an interval. Check every figure in that file the same way.
5. Write `audits/early-figures.md`: plain words first, then a table: figure → produced by (code, version, commit, command) / produced only with an error since fixed / not produced by any code found. Scripts in `audits/early/`.
Done when: every early headline figure has a provenance line.

### S31 · Chat-history provenance (D2: export)
Duke exports chat data from both accounts (claude.ai Settings, Privacy, Export data), creates a private repository BetterToBest/research-provenance (sessions cannot create repositories) and uploads the zips there. Until they are there, this step is skipped and the chain moves on. Search `conversations.json` for each figure S30 found no code for: first appearance, who wrote it, and whether a run or a source stood behind it. Keep chat text in the private repository only; copy just the table (figure, first date, basis yes or no) into `audits/early-figures.md`.
Done Oct 30 (D2 answered: the five zips in research-provenance suffice; `audits/early-figures.md` section "Chat-history provenance (S31)", `audits/early/provenance_scan.py`): Claude, not Duke, wrote each figure first, in drafts dated Aug 1-26 and Sep 5, 2025; no code ran for any (the export's 41 shell calls are all Nov 4-8, 2025); five figures appear in no chat before the Hub (65% inflation, elasticity table, $64,000-$103,000 interval, 75% minimum viable participation, 88% work participation).

### S46 · Repair the formal model
Repos: research-hub (paper sources), research-update.
The 13-comment audit (A01-A13) finds: the Pareto theorem rests on unproven premises; the budget constraint counts Basic Units twice; the first-order conditions are mis-stated; the equilibrium lemma is a one-market argument; monotonicity is only weak where the cap binds; gamma and delta are reused. Rewrite the formal section: a budget identity with B_spent + B_conv ≤ B_0; correct marginal rates; weak monotonicity with the cap; the Pareto claim as a conditional proposition (state the condition on today's transfers under which no one is worse off, and report the release's share of adults better off than with no program), or remove it; Lemma 2 scoped as partial equilibrium; notation fixed. Add the compendium's math items from S29 (p* against its theorem, V(n) convexity, the stability index's units). Deliver as edits to the paper sources with a PDF rebuild script and a "what changed" note. Lands with S24/S25.

### S10 · Second, independent implementation of the yearly loop
As ledger S10: write it from `dev/packets/s118-second-implementation.zip` without reading harness.js internals beyond the spec; save under `dev/reports/s118-independent-implementation/`; compare with `python-reference-500.json` as `dev/packets/s118-brief.md` says. Any disagreement is reported, then explained.
Done Oct 29 (compassionism-simulation #48): exact on all 2,500 validation runs once the three functions the packet lacked were added; 31 description gaps in `GAPS.md`. The validation presets run the older engine path, not the release row, hence S50.

### S50 · Second, independent implementation of the release row
Repos: compassionism-simulation. S10 checked the validation presets (`runScenario`), which switch off every release-model mechanism. This step does the same for the release row and its no-programme pair (Reference, Adverse, Stress): households, BU on essentials, project hiring, ESP payroll and the split, PTF capacity, open enrolment, the price module, the labour response, the spending rule. First close the description gaps S10 listed (`dev/reports/s118-independent-implementation/GAPS.md`) in MODEL_SPEC.md. Then build a packet from the release row with every function it calls, including samplers and reporting, and engine outputs for 500 seeds. A fresh session that has not read the engine writes the program. Same two phases as S10: independent result committed first, then differences explained. May take two sessions.
Part 1 done Nov 1 (compassionism-simulation, see HANDOFF.md): MODEL_SPEC.md describes the published release row (v5.6) and closes the S10 gaps; packet `dev/packets/s50-release-row.zip` (brief `dev/packets/s50-brief.md`; reference equal to the published v5.6 panel).
**Part 2 (the program), for a fresh session that has not read the engine:** attach compassionism-simulation, read its CLAUDE.md, open only the packet (unzip it outside the repository) and follow its `00-START-HERE.md`. Do not open `index.html`, `harness.js`, `earlier-engine.html`, `dev/` outside the packet and `dev/reports/s50-independent-implementation/`, or the results repository until the phase-1 program and results are pushed. Then phase 2 (differences explained), the same PR or the next session.

### S34 · The no-program baseline against outside data
Repos: compassionism-simulation.
Compare the no-program run (Reference, years 0 and 20) with CPS ASEC income and official poverty, the Fed's SCF wealth distribution (median, share below the model's wealth line), BLS employment, and for today's safety net, PolicyEngine-US (`pip install policyengine-us`, AGPL; household calculator) for six representative households against the engine's SNAP, EITC and CTC amounts. Write `dev/reports/baseline-realism.md` with a gap table. Fix gaps only with cited constants behind switches (simulation guardrails); changes to released figures wait for S7.
Done Oct 30 (compassionism-simulation #49; results `s34-baseline-realism-e8f8a77`): safety net matches PolicyEngine-US; the wage scale is far below US earnings (with CPS earnings, no-programme basket poverty 49.2% to 27.1%; reading `lt: {s: 'all', m: 'all'}`, off by default); everyone works (scope); household debt drift open (the spending rule).

### S33 · Study runner on GitHub Actions; runtime benchmarks (D4: Actions now; Runpod only in S48)
Repos: compassionism-sim-results, compassionism-simulation (read).
1. Benchmark seconds and memory per seed (release testbed, one environment) at 500, 2,000, 10,000 and 50,000 adults. Check the current limits of GitHub-hosted runners for public repositories, and size each planned study for Actions and for Runpod.
2. Add `.github/workflows/run-study.yml` to compassionism-sim-results: `workflow_dispatch` (study id, engine commit, job script, shard count); a matrix of shards, each running its seed range, writing outputs with `run.txt` and `SHA256SUMS`; a final job that checks every shard and writes `DONE`. It commits to its own repository with `GITHUB_TOKEN` (contents: write) only. If GitHub refuses the file: S28's rule.
3. Smoke test: dispatch a 4-seed study; its outputs must match a local run of the same seeds byte for byte.
4. Write `prereg/RUNNING.md`: how a session dispatches a study, checks it started, records it in HANDOFF.md and ends; and the Runpod route (`dev/batch/runpod.sh`) for jobs too long for Actions.
Done Oct 30 (compassionism-sim-results #4 to #7; `prereg/RUNNING.md`): GitHub accepted the workflow file from the session; smoke tests byte for byte equal to local runs (also with 4 processes per shard); benchmarks on a runner: 0.68, 1.5, 9.2 and 63 seconds a seed (main row plus no-programme pair, 20 years) at 500, 2,000, 10,000 and 50,000 adults, about twice that at 40 years; nothing planned in S32 needs Runpod by these numbers (worst case about 830 core-hours, 10.5 hours on 20 runners). S32 sizes its seeds from RUNNING.md sections 3 and 5.

### S32 · Preregister the study program
Write `prereg/2026-11-study-program.md` from `prereg/TEMPLATE.md`, pinned to the engine commit after S34, committed before any run of S35-S38.
- Q1 scale: do headline results change with population size? 500, 2,000, 10,000, 50,000 adults, seeds sized from S33 so each size has a comparable Monte Carlo error.
- Q2 synergy: every architecture combination the engine can run (check which of PTF, PTH, SZH and CIP can run without CCO; full factorial over the switches that can), seeds 1-500 paired, three environments. Report Shapley shares and interaction contrasts with paired-bootstrap 95% intervals.
- Q3 horizon: 20 and 40 years; outcomes by age at joining.
- Q4 participation: 10% to 90% (feeds S5).
- Q5: every row with the octave wage raise on and off (ledger watch rule).
- Q6 yardstick (from S34): every row against both no-programme yardsticks, the released wages and the CPS earnings of adults 25-64 (`lt: {s: 'all', m: 'all'}`). Fix here, before any result, which one the headline uses (S34 recommends the CPS one) and say which on every page. Consider a preregistered reading for the debt drift (S34 report, section 5).
- Primary outcomes, fixed now: share below 30 days of basic living (BLEI); share below the cost of living; share with too little wealth (years 20 and 40); program cost per adult; cumulative inflation. Secondary: Gini, children below the cost of living, work hours.
- Decision rules: a synergy is claimed only where the interaction's interval excludes zero; a scale effect only where it exceeds both the Monte Carlo error and one percentage point.
- Reporting: every cell published (research rule 2).
Done Oct 30 (`prereg/2026-11-study-program.md`, checks `prereg/checks/s32_feasibility.js`; engine d33de07): headline yardstick CPS earnings of adults 25-64, raise off; seven studies (A scale, B synergy, B10 synergy at 10,000, C ageing, D participation, D10 participation at 10,000, F debt reading), about 463 core-hours, all on Actions. All 32 part combinations run; all five off equals no programme; SZH alone moves only the design's own BLEI, so BLEI claims use the design-neutral BLEI. S35 first adds the job script `runner/jobs/program.js`, three reporting measures and the debt-reading switch.

### S35 · Pilot studies on Actions (free)
Run reduced versions of Q1 to Q5 on GitHub Actions only (for example 50 seeds; 500 to 10,000 adults; every architecture combination; 20 and 40 years). Purpose: find what the full batch must contain (is a community layer needed? which rows matter? are any outputs missing?), not headline figures. Write `dev/reports/pilot-studies.md`, labelled pilot throughout, and list everything the pilots show the full batch needs. If no mechanism in the engine depends on population size, say so plainly: a bigger population then only narrows intervals, itself a robustness result.
Partly done Oct 30: the "Before the first run" items landed (engine 70d23be, compassionism-simulation #50; job script `runner/jobs/program.js`, compassionism-sim-results #8; preregistration amendment 1). Seven pilots dispatched on Actions (50 seeds, three environments, 500 to 10,000 adults): folders `pilot-{a,b,b10,c,d,d10,f}-70d23be`. Done Oct 31: all seven `DONE`; `dev/reports/pilot-studies.md` (compassionism-simulation #51). No outcome depends on population size; PTF, PTH and SZH near inert, so S37 goes ahead; its section 9 lists what S47 must add.

### S47 · Design freeze (before any money is spent)
1. Collect every output the rest of the plan will need from the batch, consumer by consumer: the release panel (S7), the BLEI visual series (S11, I1), the participation figure (S5), the synergy tables (S36), the community-layer rows (S38), the scale rows and settings S39 compares with, NEEC's simulation readings (N-S70), the advocacy charts (S45), and the preregistration (S32 plus amendments). Write `prereg/run-manifest.md`: every job, its rows, environments, seeds, population, horizon, outputs and their consumer.
2. Check nothing is still moving: S10 and S50 match (or their differences are explained), the engine audit (S13) is triaged, S6 and S14 are settled, S37 is built or ruled out. Pin the engine commit.
   For the community layer (S37): add studies G, G10, H, I, J to compassionism-sim-results `runner/jobs/program.js` (row counts per the addendum) and keep its keys (`clN`, `clZ`, `clSd`, `clHi`, `clTh`, `pfMem`, `pfCut`) before the dry run.
   For the outside audits (S13; Simulation `dev/reports/s13-engine-audit.md` section 3, research-update `audits/grok-i5-triage.md`), each as a dated amendment: main rows with the audit's corrections (`au: true`) and the as-released row beside them; wages following outside inflation (`au: {wOut: true}`) as a sensitivity reading in Adverse and Stress; a sweep of wage indexation (`wIdx`); the FBS50 reading; the middle and every-dollar-backed readings of the release pair; the 0.593 spending share re-derived on the current no-programme run; MODEL_SPEC.md and TESTBED_SPEC.md written for the frozen model.
   For coverage and adequacy (S6): add study K (`runner/jobs/c22.js --env=all --procs=2`, seeds 1-500, about 6 runner-hours) to the batch, with the design Duke chose in the S6 ledger decision (if he changed the design, the release row itself changes: a dated amendment to both preregistrations before the freeze).
3. Dry-run every job at 2 seeds on Actions; confirm each output file exists and loads in its consumer's script.
4. Estimate Runpod hours and cost per job from S33's benchmarks; put the cheapest split (Actions vs Runpod) in the manifest.
5. Add a ledger decision: "Design frozen; add the Runpod key to the Claude Code environment to start S48" with the cost estimate. The chain stops here.

### S48 · The full study batch
Only after S47's decision is answered and the key is present. Run the manifest exactly (Actions where it fits, Runpod for the rest), pieces resumable, results to compassionism-sim-results with run.txt and SHA256SUMS. Start the jobs, confirm they started, record them in HANDOFF.md, and end; the next session checks for `DONE`. Any job that fails is rerun from its piece, never redesigned (a redesign is a preregistration amendment and a new S47 pass).

### S36 · Synergy report
From the batch: Shapley shares and the interaction table, 20 and 40 years, three environments, scale results, octave raise on and off. This replaces the Hub's "0.42 / 0.28 / 0.18 / 0.12" welfare decomposition, which states no method (audit A08), with a computed one.

### S37 · Community and zone layer (only if the pilots, S35, show it is needed)
The framework's synergy argument rests partly on local density: SZH zones, PTF merchant networks, PTH communities. Today the engine gates SZH by the realised PTF share but has no communities. Read the SZH, PTF and PTH papers and write "Claude's reading" of what should depend on local density. Design a community layer (communities of sourced sizes; local PTF and PTH density; zone formation), every parameter sourced or labelled and swept; build it behind a switch (off = bit-identical, `guard_test`). Add a preregistration addendum before any run.
Done Oct 31 (compassionism-simulation #52, engine c9d5287; `dev/reports/community-layer.md`; addendum `prereg/2026-11-community-layer.md`, amendment 2 of the programme; checks `prereg/checks/s37_layer_checks.js`): the Hub puts the PTF density tests (food price cut at 40%, θ at 55%) "in a given zone" and has SZH organize where PTF is deployed; the layer reads those tests per community and, with SZH, places the starting members together in zones (k 100, f 0.5; both swept). PTH density not modelled (the Hub gives only a household count). One community equals off exactly. Studies G, G10, H, I, J, about 25 runner-hours; headline at 10,000 adults. No row run yet.

### S38 · Community-layer report
From the batch (S48): the S37 addendum's rows (`prereg/2026-11-community-layer.md`: studies G, G10, H, I, J), 20 and 40 years, three environments; reported as S36, headline at 10,000 adults.

### S5 · Participation threshold
Take the figure from the batch's Q4, with its computation, and correct each paper that states 30%, 55%, 60-65% or 75% differently (lands through S24/S25).

### S6 · C2.2 coverage and adequacy
As ledger S6. Model options are Claude's call; a change to the design itself (who receives Basic Units, how much) goes to Duke as a ledger decision with the modelled figures beside each option.
Done Oct 31 (pilot): switch `C22` (compassionism-simulation #53, #54), preregistration `prereg/2026-11-c22-coverage-adequacy.md` (study K), pilot `pilot-k-395dd5b`, report `dev/reports/c22-coverage-adequacy.md` (#55). Duke's design choice: ledger D8 (default: keep the design as written). Study K's 500-seed rows join the S48 batch (S47).

### S14 · Population-weighted cost-of-living line
As ledger S14: audit the derivation from MIT's data and every dollar path in the engine first, then run it beside the current line.
Oct 31 (done): audit and switch `LW` (compassionism-simulation #56, `f66dc67`), report `dev/reports/lw-weighted-line.md`, preregistration `prereg/2026-11-lw-weighted-line.md` (study L), pilot `pilot-l-f66dc67` analysed in the report's section 6 (compassionism-simulation #57, `dev/tools/lw_pilot.py`). Release row robust to the line in the headline cell; C2.2's effect grows with the line by construction; rule 3 keeps $49,370 (ext and bea 1.2% apart). ext re-derived from MIT's 51 figures (D10: Duke pasted the outside review's source table; compassionism-simulation #58): $51,201.27. S47 chooses the line; recommendation: ext. Study L's 500-seed rows join S48 (S47).

### S39 · Outside engine cross-check (D5: after the scale results, regardless)
BeforeIT.jl implements Poledna et al. (2023) and runs at full population scale (Austria; an experimental Italy calibration). Add a Basic Unit and conversion module, run at full scale, and compare price-level effects with this engine at matched settings. Report what a US calibration would take.

### S7 · Simulation release
As ledger S7, plus: the release carries S34-S38, S5, S6 and S14 behind their switches as decided; release notes list each preregistered study with links to every result; the findings page shows them all.

### S11 · BLEI visuals
As ledger S11 (and I1). S12 (which visuals go on which page) stays Duke's choice.

### S13 · Outside audits
First pass (before S47): triage the Grok audit (I5) and run an outside-style audit of the engine (a subagent that has not seen the code reads ODD.md and MODEL_SPEC.md, then checks the code against them); fix confirmed bugs behind switches before the freeze. Second pass after S7: the release itself.

### S24 · Corrections package
As ledger S24, plus S29's valid items, S30's provenance actions and S46's patch. Rebuild every PDF from corrected sources (32 audit passages survive only in PDFs on Oct 28). Start `corrections.html` (the corrections log), linked from every corrected page and from `/v1/`.

### S25 · Abstracts, then bodies
As ledger S25. Every figure either comes from the release (S40 block), is a sourced calculation, or is labelled an illustrative projection. One paper per session if needed.

### S40 · Hub figures generated from the release
`tools/build_figures.py` in research-hub reads the Simulation's release file by tag and writes figures into marked blocks (`<!-- FIG:name -->…<!-- /FIG -->`); `--check` fails when a page disagrees with the release. Replace hand-typed simulation figures with these blocks.

### S3 · OEIAS; S4 · X-cents
As ledger S3 and S4.

### S41 · Site and wiki design refresh
One shared stylesheet, header and footer across the Hub, the wiki (index, glossary, FAQ, implementation roadmap, international adaptation guide) and the papers index; light and dark; mobile; keyboard, focus and contrast (axe, no serious or critical findings); wiki search kept. Front page: what Compassionism is; findings (S40 blocks); papers; tools (Simulation, CIP portal, x-cents, NEEC); how to help. Prose unchanged beyond navigation labels. Screenshots in light, dark and mobile in the PR.

### S43 · Links and publications
Link the CIP portal (bettertobest.github.io/portal/), x-cents (bettertobest.github.io/x-cents/), NEEC (bettertobest.github.io/NormativeEvaluation/) and the Simulation from the front page and wiki. A publications page: every Academia paper (D3: Duke pastes the links into D3's note in the ledger; until then the chain skips this step) with title, year, link, the Hub page it matches, and a note where the Hub corrected its figures.

### S42 · Machine-readable files
`data/site-manifest.json` in research-hub becomes the one source; a script with `--check` generates ai-index.json, research-index.json and llms.txt (bettertobest.github.io), JSON-LD on Hub pages, sitemap.xml and CITATION.cff. Include the release, NEEC, the portal, x-cents, the Academia papers and `/v1/` (marked archived). Validate the JSON and JSON-LD.

### S44 · Hub v2 fresh-eyes review
A subagent that has not seen the work reads the Hub as a journalist and as an economist: every figure traced through `data/claims.csv`, every link resolves, accessibility passes, the v1 banner shows. Fix small, certain items; list the rest in the PR.

### S45 · Advocacy kit from the release
From the release data only, in research-hub `press/`: a one-page brief that leads with the strongest robust findings in plain words (each with its environment and interval); five shareable charts; a "what the model does not show" FAQ; a 150-word press paragraph; Bluesky posts under 300 characters. Every number carries its source line.

### S8 · Hand back to NEEC
As ledger S8: list the Hub v2 papers and the release OEIAS is read on; draft the push-back cases (N-S72); unpause NEEC.

### NEEC steps (N-S…)
Read NormativeEvaluation's CLAUDE.md and STATE.md; the step text is in the ledger (document `neec`). NEEC's own rules govern; its scores change only through its recorded rescoring pass.
