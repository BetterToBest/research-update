# Preregistration: the private businesses' BU price at the sale (S90's fix), rerun of the v5.9 main rows

Committed Nov 18, 2026 by S90, before any run. Engine: compassionism-simulation at commit `b8ccd8d4b8f39a621db6186402877ba60be1904e` (main, the merge of pull request 163), which adds the option `sp.vAt: 'sale'` (off by default; with it off every output equals v5.9's, guard test identical).

## Why
S90 traced the damped two-year swing in the BU each adult spends (main row, Reference, seed 1: $22,838 in years 0-1, then $10,969, $21,452, $13,819, $19,472, $16,202) to the private businesses' lower BU price. The code paid it from last year's premium, shared by last year's BU. Duke's design sets it at the sale ("At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU", Oct 1, quoted in compassionism-simulation `dev/reports/v5-1-private-esp-correction.md`). So the lag is a defect (research rule 9), and the swing reaches incomes, BU spent and expired, project hiring and programme cost by year. The fix: under `vAt: 'sale'` a BU spent at a private business buys 1 + vK dollars, where vK is that BU's premium after the conversion tax, payroll and the workers' match. The cut is paid as an advance that next year's premium repays exactly. Only the premium on payroll BU returned a year later (d73) is still shared a year late. Full record: compassionism-simulation `dev/DECISIONS.md` "S90" and `dev/reports/s90-private-price-at-sale.md`. Every published programme figure since v5.0 (Oct 2, 2026) uses the lagged rule. A first look on seeds 1-2 (inspection, not a result) moved the main row's cut in basket poverty by about 0.6-0.7 points.

## Questions
- Q1. Does the at-sale price remove the swing in every environment? Answer: the swing measure below, at the sale against lagged, per environment.
- Q2. How much do the v5.9 headline effects change (the five headline measures, both designs, three environments, 20 and 40 years)? Answer: the paired change, at the sale minus lagged, with its 95% interval.
- Q3. Does any headline statement on the findings page change in sign or in its stated rounding? Answer: a yes/no per statement, read under decision rule 4.

## Design
- **Rows.** The v5.9 main rows as `r2.js --part=M` builds them (no programme; the full-coverage design; the opt-in design), each programme row run twice: lagged (the published setting) and at the sale (`sp: Object.assign({}, row.sp, {vAt: 'sale'})`). The no-programme row does not read the option (it has no surplus split) and is run once.
- **Environments:** Reference, Adverse, Stress. **Horizons:** 20 and 40 years. **Adults:** 500. **Seeds:** 1-500, paired across all rows (common random numbers).
- **Where:** GitHub Actions (`run-study` in compassionism-sim-results; free), a new job `runner/jobs/s90.js` added by pull request before the dispatch. It builds the rows exactly as `r2.js --part=M` does, adds the at-sale copies, and calls the engine's `startRelease({baseline: true})`. Study ids `s90-sale-ENV-YRS`, folders `s90-sale-ENV-YRS-<engine, 7 characters>` with `run.txt` and `SHA256SUMS`.
- **Swing measure (Q1).** Run on the session machine with `node dev/tools/s90_trace.js` (compassionism-simulation; read-only probes, `--check` proves the copy's outputs equal the harness's), seeds 1-20, 500 adults, 20 years, three environments, lagged and `--sale`. It is the mean over years 2-12 of |BU spent per programme adult this year − last year| / this year.

## Checks (before any outcome is read)
1. The lagged programme rows and the no-programme row equal the published `r2-m-ENV-YRS-104691f` rows per seed, on every output key (the option is off on them).
2. Every folder has 500 seeds per row, its engine commit, a clean engine, and `run.txt` and `SHA256SUMS`.
3. The engine's accounting checks (`ACCT`) pass on the at-sale rows for seeds 1-5 in each environment (no identity fails; the premium identity included), run with the unit suite's method.

## Outcomes
- **Primary** (main row against no programme, per design, environment and horizon; as REPRODUCE.md's "Headline values" table defines them): below 30 days of basic living (unweighted); below the cost of living, basket poverty (unweighted); too little wealth, yearly average (unweighted); median real wealth in year-0 dollars (weighted); programme inflation (basket index above no programme, points a year).
- **Secondary:** FGT2 (poverty severity); mean real income; BU spent and BU expired per programme adult (20-year mean); programme cost (the testbed's cost keys); the weighted versions of the primary measures where the published tables give them.
- Gains are confirmed on basket poverty and wealth poverty, not FGT2 alone.

## Analysis
- For each outcome, cell (design × environment × horizon): the effect against no programme under each rule and the paired change (at the sale − lagged), mean over seeds 1-500, with a 95% paired bootstrap interval (2,000 resamples, generator seed 9001).
- The analysis script is added to compassionism-simulation (`dev/tools/s90_tables.py`) before the results are read; it prints checks 1-2 first and stops if one fails.
- No synergy claim is made (one change, not a factorial).
- Multiple comparisons: Holm across the five primary outcomes within each cell, for the statement "the change is not zero"; every interval is published unadjusted as well.

## Decision rules
1. If check 1, 2 or 3 fails, stop: nothing is read, the defect is found, and the run is redone after a dated amendment.
2. Q1: the fix is taken to work if, in every environment, the at-sale swing measure is below half the lagged one. If it is not, stop and report; the default does not change.
3. If rule 2 holds, the at-sale price is the corrected model. Its figures replace the main rows' figures at the next release (Duke assigns the version), with an entry in the Hub's corrections log. The lagged figures stay published as the v5.9 record (the OSF registration is the frozen v5.9 model). This holds whichever way the figures move.
4. Q3: a findings-page statement changes if the at-sale effect changes sign, or if its rounding as printed changes. Each changed statement is listed with both figures.
5. Every other published study that runs programme rows (the main rows' readings, financed rows and 10,000-adult rows, `r2-s/f/b`; the central-bank study `s74-final-3beb5ff`; the history study `s75-eras-e5649ef`; the supply study S82; the suite folders `x2`, `x3`, `x4`; the v5.0-v5.6 panels) gets a dated note on its page or report: it paid the private price a year late, the main row's change was the figure Q2 found, and a rerun is or is not planned. A rerun of any of them is its own preregistered amendment.

## Reporting
Every cell above is published in compassionism-sim-results and in the plain-words report, including changes against the programme and changes too small to matter.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.

### Amendment 1 (Nov 19, 2026): readings fixed before the six result folders existed
Clarifies only, so no design changes. Each reading was fixed in code before its results were run or read: the swing driver before the swing measure was run, and the tables script before any folder of the full rerun existed.
- **Rows.** "The main rows as `r2.js --part=M` builds them (no programme; the full-coverage design; the opt-in design)" is read as those three rows plus the two at-sale copies, five in all. Part M's financed rows are left out. They are among the other reached studies of decision rule 5, so they get a dated note.
- **Swing measure (Q1).** The measure is computed for each seed and then averaged over seeds 1-20, so swings in different seeds cannot cancel. The same measure on the series pooled over the seeds is published beside it. BU spent per programme adult is the trace tool's BU spent at face value, summed over programme adults, over their number, for each year (`dev/tools/s90_swing.js`).
- **Secondary outcomes.** The engine stores no mean real income key, so real wage earnings per adult-year (`Er`) and the median real disposable income at the last year (`dmYp50E`, weighted) stand for it. BU spent is `mfBU` (face value per adult-year, the run's mean), and BU expired is `mfIss − mfBU` (issued and not spent). Both are per adult-year over all adults, not per programme adult; under full coverage these are the same adults. Programme cost is `cost`. The weighted primaries are `wtF0E` and `wtPovE` (the last year; the published tables give no weighted yearly versions).
- **Check 3** is run by `dev/tools/s90_acct.js` with the unit suite's method.
- **Q3.** The tables mark each primary effect whose sign or REPRODUCE.md rounding (2 decimals; whole dollars) changes. The findings-page statements are then read against the page itself.

### Amendment 2 (Nov 21, 2026, S97): the release's reruns and checks, fixed before the release
Committed before the release engine exists and before any rerun below. It decides what decision rule 5 left open (which reached studies are rerun) and fixes the checks the release must pass before its figures are published.

**What this is.** A corrective rerun, not a new confirmatory study. The corrected main rows were already run and read (S92, folders `s90-sale-*-b8ccd8d`, tables `s90-tables-b8ccd8d`): every poverty and wealth effect grew slightly in the programme's favour and none changed sign. So the reruns below are not a test of a hypothesis whose answer is unknown; they bring every figure the release shows onto one engine. The rerun list follows code dependencies only (which rows run the private price rule), not which way any figure moved or might move.

**Terms.** *The release engine*: the compassionism-simulation commit that S93 merges with `sp.vAt: 'sale'` as the default (version: ledger D34), named by its full hash in every rerun's `run.txt`. *Published figures*: the frozen model (engine `104691f`, registered on OSF and first published as v5.8), shown on the pages as the v5.9 model, and the studies run on later engines with the late price. *Reached*: a row reads the private price rule if its surplus split has `priv: 'prices'` under the framework conversion (index.html, `spVOn`). Every row built from `relMainCfgs` carries it (`REL_V5`), so every v5.0-and-later programme row is reached, including `r2FreezePair`'s; no reading in `r2.js`, `s82.js`, `series-r2.js`, `s74_pilot.js`, `s75_eras.js` sets `sp` (checked Nov 21 by grep; the `sp` in `s74_sweep.js` is the central bank's spread, a different option), and `s85.js` and `s94.js` only add `vAt: 'sale'` to it. (`r2FreezePair` is the row builder these jobs share, not a study.) No-programme rows have no surplus split and are not reached.

#### A. Engine conditions (S93, before any rerun)
1. `sp.vAt: 'lag'` selects the old rule on the release engine. With it set on every guard-test row, the guard test equals its pre-release reference exactly (proof that the default switch is the only change). The guard test's new reference, made with the default, is recorded in DECISIONS.md as a change by design, naming the at-sale rows it was checked against (`s90-sale-*-b8ccd8d`).
2. The release engine's lineage (`engine_lineage.js prove`) links it to `b8ccd8d`, `503fa48` and `c5682f9`; `sync_earlier.py` run; unit counts rewritten.

#### B. Which studies are rerun on the release engine (decision rule 5)
Every study whose figures a page shows at the release, and which ran reached rows with the late price, is rerun as it was run, on the release engine, same rows, seeds, adults, environments and horizons, with no row changed (its job script unchanged except the engine commit and, where a path names an engine, that path). Folders: `<study>-<release engine, 7 characters>`, with `run.txt` and `SHA256SUMS`.

| Study | Published folders | Where it shows | Rerun as |
|---|---|---|---|
| Main rows (part M) | `r2-m-*-104691f`; at sale `s90-sale-*-b8ccd8d` | findings page cards and tables, release data `data/releases/r2/` | `r2.js --part=M`, six cells, seeds 1-500 (GitHub Actions) |
| The 62 readings (part S) | `r2-s-*-104691f` | readings' curves, ranges, `r2-curves.json`, `r2-effects.json` | `r2.js --part=S` (Actions) |
| Financed rows (part F) | `r2-f-*-104691f` | `r2-financed.json` | `r2.js --part=F` (Actions) |
| 10,000-adult rows (part B) | `r2-b-*-104691f` | the 10,000-adult check | `r2.js --part=B` (Actions) |
| Erosion shares | `r2-erosion-104691f` | the erosion share beside each wealth figure; `r2-backing.json` and the other r2 data files | its `run.txt` commands (session machine) |
| The r2 tables | `r2-tables-104691f` | every `data/studies/r2-*.json` | the tables tools on the rerun folders |
| Central-bank study | `s74-final-3beb5ff` | `s74-cb.json`, the central-bank section | `s74_pilot.js ENV 100` for ref, adv, st, hx, then `s74_table.js`, `s76_cb_data.py` (session machine or Actions) |
| History study | `s75-eras-e5649ef` | the Hub's policy-eras page, its report | `s75_eras.js ERA 100` for e1-e4, then `s75_table.js` |
| Supply study | `s82-v6-*-aa2a4e0`, `s82-v6-age-*-ab11c05`, tables `s82-tables-aa2a4e0` | `s82-supply.json`, `s82-breakeven.json` | `s82.js`, all 231 rows, both batches as run (Actions) |
| Visual suite | `x2-5b62481`, `x3-6d095a1`, `x4-a60bd3e` | the visual suite page, `data/releases/r2/suite-*.json` | `series-r2.js` as each `run.txt` records, its panel path pointed at the rerun part M folder (Actions) |

**Already at the sale, on a later engine: reproduced, not rerun.** The automation study (`s85-*-503fa48`, `s85sec-*-503fa48`) and the lending study (`s94-*-c5682f9`) set `vAt: 'sale'` in every programme row. On the release engine, seeds 1-10 of every row in all six cells of each (`--seeds=1-10`, Actions) must equal the published shards on every stored key. If they do, the published folders stand as release figures, labelled with both commits ("run on `503fa48`; the release engine reproduces it"). If any value differs, the cause is found and recorded, and the study is rerun in full on the release engine.

**Kept as the record, not rerun** (reached, but superseded or not a release figure; each keeps its dated note of Nov 19 where it has a report): the v5.0-v5.6 release panels (`data/releases/v5.*`; an earlier model generation, shown under its own version); superseded folders (`s74-final-a60ecd1`, `s74-cb-5f11ceb`, `s75-eras-77a85d6`, `s82-v6-*-eb0969c`, `r2dry-104691f`); the round-2 screen (`s70-screen-*-8b96cdd`; it chose which readings are swept, a design input of the frozen model, and rerunning it would be a redesign); the round-1 and v5.x studies (`prog-*`, `*-ce8d030`, `s51`-`s62`, `s39-*`, `s137*`, the `x-ce8d030` suite). Studies before v5.0 (Oct 2, 2026) do not read the rule.

**The engine rule for pages.** No page, data file, chart or Hub page shows figures from two engines without naming each, and no range, curve or comparison mixes them. After the reruns every figure in the findings page's release sections comes from the release engine (or from a study reproduced on it, labelled as above). A kept figure shown anywhere names its version and says the private price was paid a year late.

#### C. Below full backing (from Kimi's reading, Nov 20)
Full backing barely tests the price rule, because the price level hardly moves there. So the fix is also verified where it does:
1. **Swing.** The swing measure (`s90_swing.js`, seeds 1-20, 500 adults, 20 years, three environments), extended by a backed-share option in `s90_trace.js` (tool only, written before it is run), at no backing (a = 0) and half backing (a = 0.5), full-coverage design, lagged (`vAt: 'lag'`) and at the sale (the default), on the release engine. The fix works below full backing if, in every environment and at both backed shares, the at-sale measure is below half the lagged one. Where the lagged measure is itself no larger than S92's at-sale measure at full backing in that environment (no swing to remove), the condition is instead that the at-sale measure is no larger than the lagged one. (The premium per BU comes from the conversion rate and taxes, not from the backed share, so the rule is expected to act at every backed share.)
2. **Books.** `s90_acct.js`, extended the same way, at a = 0 and 0.5: no accounting identity fails, the premium identity included (the advance is repaid exactly by next year's premium), seeds 1-5, three environments.
3. **Paired change.** On the supply study's rerun, the base rows at a = 0, 0.25, 0.5, 0.75, 1 against the same rows published (`s82-v6-*-aa2a4e0`), same seeds 1-500: the paired change (release minus published) on the five primary outcomes, with a 95% paired bootstrap interval (2,000 resamples, generator seed 9001), per cell; a cell is one base row (one backed share) in one environment and horizon, so 5 × 3 × 2 = 30 cells per outcome. It is valid only if the no-programme rows equal the published ones per seed on every key (check D2). Published whichever way it moves.
4. If 1 or 2 fails: stop and report. The release's figures below full backing (supply study, the automation study's produced backing, the central bank's no-backing arms) are not published from the release engine until the cause is found and fixed by a dated amendment; the full-backing figures go ahead.

#### D. Checks on every rerun (before any figure is read)
1. Every folder: all seeds per row, the release engine's commit, a clean engine, `run.txt`, `SHA256SUMS` (`sha256sum -c` passes).
2. The no-programme rows equal the published no-programme rows per seed on every key (they do not read the rule; any other difference is an unannounced engine change).
3. Part M's programme rows equal `s90-sale-*-b8ccd8d`'s at-sale rows per seed on every key.
4. The central-bank study's "off" arm and the history study's start equal the rerun part M as their own checks require (`s76_cb_data.py --check-r2`, `s77_check_start.js`), pointed at the rerun folders.
5. The supply study's checks rows (`Achk`) pass as before.
If a check fails: stop; nothing is read; the cause is found. If it is a defect, it is fixed and the rerun redone after a dated amendment (decision rule 1); if it is an engine change made by design, a dated amendment names it and what it reaches before anything is read.

#### E. Archived commands reproduced from scratch (from Kimi's reading)
From a clean checkout of each folder's recorded engine commit and runner commit, the shard's recorded command is run again (Actions) and every stored value compared: each seed's value of each key under the shard's `rows` (the run's figures), to the stored digits; the shard's `_meta` block and the `.timing.json` and `.log` files are not compared. The sample was drawn on Nov 21 before any of it was run (Python `random.Random(9797)`: environment, horizon and shard per study, in this order): `r2-m-adv-40-104691f` shard 0000; `r2-s-ref-40-104691f` shard 0000; `r2-f-adv-40-104691f` shard 0006; `r2-b-ref-20-104691f` shard 0000; `s90-sale-adv-40-b8ccd8d` shard 0011; `s82-v6-str-20-aa2a4e0` shard 0013; `s85-adv-40-503fa48` shard 0007; `s94-ref-40-c5682f9` shard 0003; and, from the session-machine studies, `s75-eras-e5649ef` era e2 (the shortest). Every value must be equal. If one is not, the release waits until the cause is found and recorded in the folder's `run.txt`.

#### F. The pre-publish checklist (S93, before the pages that show release figures are merged)
1. **Changes recorded.** For every figure the pages print, a table of the published value and the release value (extend `s90_page_check.py` to every release data file), with the count that change in the last printed digit, in sign, or out of a printed range. Expected (from S92): small, and at full backing in the programme's favour. Any change against the programme, or in sign, is listed and the page's statement rewritten to the release figure; nothing is held back for its direction.
2. **Swing gone** in the regenerated rows: the swing measure on the release engine's default (seeds 1-20, 500 adults, 20 years, three environments, as S92 ran it) equals S92's at-sale measure, below half the lagged one in every environment; section C's result beside it.
3. **Guard test** reference rewritten and recorded (A1).
4. **Qualifiers present:** `check_round2.js` passes; reader codes `--check` (simulation, Hub, root site) 0; the full-backing footnote on every headline card; the erosion share beside each wealth figure; the interval notes; the opt-in figure beside each card (S98).
5. **BLEI visuals and the Five Measures chart** (ledger I1): each series they draw is present in the release data (`data/releases/r2/`); confirmed, or the missing series listed and the item closed with the chart labelled or removed.
6. **Charts and captions** (`data/studies/r2-charts/*.svg` and every figure caption) regenerated from the release data; none left from the published data.
7. **Correction notes:** the findings page's and text file's dated notes on the late price are replaced by the current statement (item G); the reports keep their notes as history.
8. **Engine names:** each page section names, in text a reader sees (its heading note or caption, not only the data file), the version and engine commit its figures come from; a script lists every data file a page reads with its engine commit, and any section mixing two fails.
9. **Outside reading** of the regenerated figures and the release text by two language models from makers other than Anthropic and from each other (OpenRouter `:free` or the NVIDIA catalogue), before the merge that publishes them; each point triaged in a file in `audits/` (agreed and fixed, or not taken, with the reason); a point that would change a figure is acted on only after the data file or code it concerns has been opened and checked.
10. Hub corrections-log entry; root-site indexes (`ai-index.json`, `research-index.json`, `llms.txt`) in step.

#### G. What the release text says
The release version and the release engine's commit; that the private businesses' lower BU price is now set at the sale (Duke's design, Oct 1) and is the default; what that changed, stated from item F1's release figures (not from S92's range, which is only the expectation); which studies were rerun and which reproduced; that the model registered on OSF (v5.8, engine `104691f`) and the v5.9 figures stay published as the record, reproducible from their engine commits.

#### Decision rules for the reruns
1. Section D or E fails: stop, as above.
2. Section C fails: as C4.
3. Otherwise the release figures replace the published ones on every page for every rerun or reproduced study, whichever way they move (decision rule 3).
4. No figure, constant or row is changed to move a figure. A defect found in a rerun is fixed by a dated amendment and a full rerun of what it reaches.

*Changes from the outside reading (Nov 21, before this amendment was merged or anything run).* Nemotron 3 Ultra (OpenRouter, free tier) read the amendment; triage in `audits/2026-11-21-s97-amendment-reading.md`. Taken: the cell definition in C3; a fallback in C1 where there is no lagged swing; F2's seeds; what E compares; what D does when a failure is by design; visible engine names in F8; F9's readers and triage; G states the release figures, not S92's range; the grep's scope stated. Nothing else changed.

### Amendment 3 (Nov 21, 2026, S93): the release main row adds pay by household type and the care credit
Committed before the release engine exists and before any rerun of section B. Reason: a design decision, not a result of this rerun. Duke answered ledger D36 on Nov 21 ("adopt both if the decision rule holds"); the yardstick study's decision rule 2 holds (`prereg/2026-11-s100-part-time-dcc.md`; tables compassionism-sim-results `s100-tables-e50a3b3`), so the release main row carries both readings. Version (ledger D34): Duke's answer of Nov 19 held the release until the pre-release steps were done and named no number, so its default stands, a v5.9 patch: **v5.9.22** (the engine's next version). Amendment 2 is unchanged except where this amendment says so.

**The release main row.** `harness.js` `r2FreezePair` (both rows of the pair: no programme and programme; both designs) with the private price at the sale (`sp.vAt 'sale'`, now the engine default), pay by household type (`eh {}`, partners' correlation 0.2198) and the child and dependent care credit for households that pay for care (`sn.cdc true`). It is the yardstick study's `both` rows (`none.both`, `c22.both`, `rel.both`) without `sn.rep` (reporting keys only; that study's unit test shows it moves no key). The v5.9 main row stays reproducible on the release engine with `eh: false` and `sn.cdc: false` on both rows and `sp.vAt: 'lag'` on the programme row.

**A. Engine conditions (replaces A1; A2 stands).**
1. `sp.vAt: 'lag'` selects the old rule. With it on every guard-test row, the guard test equals its pre-release reference exactly (the guard rows are the v5.4 panel's, which carry the private price rule but not `r2FreezePair`, so the yardstick readings do not reach them). The new reference, made with the default, is recorded in `dev/DECISIONS.md` as a change by design.
2. With `sp.vAt 'lag'`, `eh: false` and `sn.cdc: false`, every key of `r2FreezePair`'s rows (none, full coverage, opt-in) on the release engine equals the engine before (main `a33c59d`): Reference, Adverse and Stress, 20 and 40 years, seeds 1-2.
3. With the defaults, every key of the release main pair at seeds 1-2 (Reference and Stress, 20 years) equals the yardstick study's `both` rows on `e50a3b3` (its shards), keys both hold.
4. `sp.vAt` takes only 'sale' or 'lag' (any other value is refused, so a misspelt option cannot select the old rule silently).

**B. Which studies are rerun (changes Amendment 2's table and its "reproduced" paragraph).** Every study in Amendment 2's table is rerun as listed; each job builds its rows from `r2FreezePair`, so it carries the release main row with its script unchanged. The automation study (`s85-*-503fa48` and its supplement `s85sec-*-503fa48`) and the lending study (`s94-*-c5682f9`) move from "reproduced" to **rerun in full** (`s85.js`, `s85.js --sec`, `s94.js`, all rows, six cells, seeds 1-500, Actions): their rows are built from `r2FreezePair` and now carry the two readings, so the published shards are no longer the release row (a code dependency, decided before any rerun). The yardstick study (`s100-*-e50a3b3`) is **kept as run**: it compares the readings, its `both` rows are the release main row on the engine before, and check D3 ties the release to it. Its findings section is reworded at the release to say the readings were adopted, its figures unchanged.

**C. Below full backing.** As Amendment 2, on the release main row; "lagged" is the release main row with `sp.vAt 'lag'`.

**D. Checks on every rerun (replaces D2 and D3; D1, D4, D5 stand).**
2. The no-programme rows carry the two readings, so they no longer equal the published ones. Part M's no-programme rows equal the yardstick study's `none.both` per seed on every key both hold. A study's no-programme row built exactly as part M's equals part M's rerun per seed. For the other no-programme rows (their own settings: central bank, history, supply, suite), the engine proof A1-A2 stands for this check, and each job's dry run (seeds 1-2, every row, every cell, before dispatch) passes the accounts, the eight draws per adult-year and finite outputs (`acctDrawCheck`) and its own checks, with the two readings on beside every other switch the job sets (no study has run them together before).
3. Part M's programme rows equal the yardstick study's `c22.both` and `rel.both` per seed on every key both hold, seeds 1-500, six cells.

**E. Archived commands reproduced.** Unchanged (each sample shard is run on its own recorded engine commit).

**F. Pre-publish checklist (changes F1, F2).**
1. The table of published against release values splits part M's change where both parts were run: the private price at the sale (`s90-sale-*-b8ccd8d` against the published rows) and the yardstick readings (the yardstick study's `both` against `off`). Amendment 2's expectation (small and in the programme's favour) no longer covers the whole change: the yardstick study measured the opt-in design's cut in basket poverty 0.32-0.91 points smaller in every cell and the full-coverage design's cut below 30 days of basic living 0.41-0.73 points larger. Every change against the programme or in sign is listed and the page's statement rewritten to the release figure, as Amendment 2 says.
2. The swing measure on the release main row is below half the same row's with `sp.vAt 'lag'` in every environment; S92's at-sale measure is printed beside it (it was measured on the v5.9 row, so equality is no longer expected).

**G. The release text** also says: the main row now includes pay by household type and the child and dependent care credit (Duke's decision, Nov 21, after the yardstick study's preregistered rule held), what that changed (F1's split), and that the v5.9 main row without them stays the record.

**Decision rules for the reruns.** Unchanged.

### Amendment 4 (Nov 21, 2026, S93): a defect found by condition A3, fixed in the release engine before any rerun
**Found.** Condition A3 failed: the release main pair did not equal the yardstick study's `both` rows in its published shards (Reference and Stress, 20 years, seeds 1-2; 1,207 and 1,166 of about 2,980 series differ; the no-programme row's inflation, 0 when run alone, was about 0.0001 points). That study's own job reproduces its shards exactly on the engine before, but the `none.both` row run alone in a fresh process gives the release's values, while run after the care-credit rows it gives the shard's. Cause: the engine caches each seed's no-programme supply path (`tbBaseS`, used by every main-row run through `fx.sp`; also `s3BaseS`) under a key that leaves out settings that are not cleared for the cached run: pay by household type (`eh`), and the price rule's settings (`pr`), which act on no-programme runs too; bargaining, the government account and PTF running costs were also missing. In a process that runs several rows, a row could take the supply path computed for an earlier row with different settings. A row run first in a fresh process was always right.

**Fixed** in the release engine (`index.html` `rowKeyS93`; the health module's government-share key also gains `eh`): each of these settings, when set, is part of the key. With all of them off the key is unchanged, so every run without them is unchanged (guard test identical to its new reference; condition A2 as before), and a row run alone is unchanged in any case. The Collectives' fund is left out of the key (its study's check 2b shows a no-programme run with it set is identical).

**Condition A3** becomes: the release main pair equals the yardstick study's `both` rows each run alone in a fresh process on the engine before, with that study's job (`--rows=9-9`, `10-10`, `11-11`), Reference and Stress, 20 years, seeds 1-2, on every key both hold. The comparison with the published shards is printed for information.

**What it reaches.**
1. *The yardstick study* (`s100-*-e50a3b3`): its rows with pay by household type that ran after a row without it in the same process (`eh` and `both`, by its job's split of rows into four processes) carry the earlier row's supply path. Its decision rule 2 reads `none.off.full` and `none.both.full`, each first in its process with its own key, so the rule's basis is untouched and D36 stands; its effect figures are not. It moves from "kept as run" to **rerun in full** on the release engine (six cells, seeds 1-500, its job with one change: its rows are built from the v5.9 row, `r2FreezePair(P, design, true)`, so its readings are exactly as preregistered on either engine). Its report and findings section get a dated note now; their figures are replaced from the rerun at the release, whichever way they move. Check D3 then compares part M with the rerun's `both` rows.
2. *The studies rerun for the release* (Amendment 2 B with Amendment 3): every one runs on the fixed engine, so no release figure carries the defect. Their published folders may carry it where a row with a price-rule, bargaining, government or PTF-cost reading ran after a row without it in one process (the round-2 readings, the supply study's price-option rows); they stay as the record of their engine, and the release text says so.
3. *Studies kept as the record* that ran such rows several to a process (the price-rule studies, the round-2 screen, the government, bargaining and PTF-cost studies): an audit of which folders are reached and by how much is added to the plan (a follow-up after the release; each reached report gets a dated note). It does not hold the release, since no release figure comes from them.

**Unchanged:** sections C, E, F (with Amendment 3), G and the decision rules. The release text (G) also names this defect and its fix.
