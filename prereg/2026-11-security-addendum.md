# Preregistration addendum: security outcomes beyond wealth, and the per-year series for public costs (S53, study P, for S47)

Committed Nov 2, 2026 by S53, before any run of these rows on Actions. One disclosure: before this file was committed, the engine measures, the job script and the two consumer scripts were tested on seeds 1-2 on the session machine (all three environments), to check that switching the measures on moves no other figure, that the yearly series add up to the run's person-year figures, and that both consumer scripts load every row and key. Those numbers are not results and are not used. They changed nothing in this file.

## Why
The model reports poverty, wealth, work, cost and prices. It did not report security as people live it: whether a fall in income can be absorbed, how long the basics last without wages, how many hours of work the basics cost, whether people are pushed out of their homes, and how much of their budget is exposed to market prices for essentials. Plan step S53 adds these as outputs of every study that asks for them, and the per-year poverty figures that the public-costs step (S19) needs, so S19 is a calculation on the full batch with no new run.

## Plain-words summary
- **Q17 (primary).** Compared with no programme, does the design make big income drops with no buffer rarer, and does it change how many households could cover the basics for three months without wages? For whom: those who take part, and those who choose not to?
- **Q18.** How many hours of work a week do the basics cost, how often are households displaced by price, and how much of the budget is paid in money at market prices for essentials? These are mostly true by construction and are reported as the design's accounting, not as evidence.
- **Q19.** Do the answers hold under S52's outside supply shock, and how much of the savings measures is savings losing value to inflation (savings that keep up with prices, S51's sensitivity)?
- Two designs: the release row as released, and the C2.2 design (study programme Amendment 4).
- **Pilot now:** seeds 1-50 on GitHub Actions, labelled pilot throughout. **Full:** S47 adds the measures (study option `sec`) to every batch job that S54 and S19 read, and study P's rows at seeds 1-500.

## Design
**The measures** (study option `sec`, reporting only: no draw, nothing any rule reads; engine reading `dev/reports/s53-security-reading.md` in compassionism-simulation). Groups: A all adults; P the adults who take part; X the adults who choose not to (the same adults in every design and in the no-programme run). Words: *resources* are money income plus in-kind help (the engine's resources measure); *liquid savings* are 20% of positive savings (the BLEI's liquid share); *income without wages* is cash transfers, unemployment insurance and Social Security (conversion proceeds left out, the cautious reading); *need* is own cost of living less income without wages.

| Key (per group) | Outcome | Basis |
|---|---|---|
| `secU25` | resources fall 25% or more from the year before and liquid savings at the start of the year are below the fall (per 100 adult-years) | emergent |
| `secD25`, `secU50`, `secU25m` | any 25% fall; an uncovered 50% fall; an uncovered 25% fall in money income alone | emergent |
| `secM3`, `secM1`, `secMd` | % of adult-years with liquid savings covering under 3 / under 1 month of need; median months (cap 120) | mixed: need by construction, savings emergent |
| `secM3w` | under 3 months on all savings | mixed |
| `secHr`, `secH40`, `secHrc` | median hours of work a week to cover need at the adult's usual wage (2,080-hour year), working-age adults with a wage; % above 40 hours; median with conversion proceeds counted | by construction, given prices and wages |
| `secDs` | displacement by price, a proxy: adults outside PTH who could pay last year's cost from income and savings and cannot this year (the engine's housing-distress test), per 100 adult-years | emergent (proxy: the model has no moving decision) |
| `secPx` | PTH tenancies ended per 100 member-years | by construction: no rule ends a tenancy against the member's will; with the PTH books on, members leave at the drawn moving rate (6.2%) |
| `secXb`, `secXe` | essentials (what BU can buy) paid in money at own prices, % of the whole cost of living at market prices; % of essentials at market prices | by construction (no programme: `secXe` = 100, unit test) |

**The S19 series**, per year `s19<m>_<t>` (t = 0..39, 0 past the run): basket poverty, FGT1, poverty-gap dollars per adult (year-0 dollars) and the same capped at $10,000 a year, deep poverty (half or more of the cost unmet), housing distress, the engine's extreme-poverty estimate, adults, and basket poverty of group X. Weighted by adults, the yearly basket poverty and FGT1 equal the row's `fgt0PY` and `fgt1PY` (unit test).

**Rows** (job `runner/jobs/security.js` in compassionism-sim-results; `--check` confirms 10 rows per environment). Every row is the runner's reference job (release-pair.js settings, study options plus `sec: true`) with only the named change:

| Design | Path | Rows |
|---|---|---|
| rel (release row) | off (no outside shock) | none; prog |
| c22 (C2.2 design, CPS yardstick) | off | none; prog |
| rel | main (S52's main supply shock, preset key `sx` with its defaults, the environment's) | none; prog |
| c22 | main | none; prog |
| rel | off, savings that keep up with prices (row option `sv`, both rows) | none.sv; prog.sv |

- Environments: Reference, Adverse, Stress.
- Seeds: pilot 1-50; full 1-500. Paired across all rows (common random numbers).
- 500 adults, 20 years.
- Engine: compassionism-simulation commit `f15eaf65b31ca15430590af764ee0b629a0229a0` (pull request 66; the merge commit).
- Where: GitHub Actions, workflow `run-study`, study `s53-security`, job `security.js`, `job_args` `--env=all --procs=4`, 5 shards; folder `s53-security-<engine, 7 characters>/` in compassionism-sim-results.

## Outcomes
- **Primary (Q17):** `secU25` and `secM3`, group by group, the design minus no programme on the same seeds, in each environment, on the path without the shock.
- **Confirmations:** the same under the main shock; `secD25`, `secU50`, `secU25m`, `secM1`, `secM3w`, `secMd`; basket poverty (`fgt0PY`) and wealth poverty at year 20 (`pov`) beside them (guardrail 6); non-participants' basket and wealth poverty (`gNonF0`, `gNonW`).
- **Secondary (Q18, accounting):** `secHr`, `secH40`, `secHrc`, `secXb`, `secXe`, `secPx`; and `secDs` (emergent).
- **Q19:** each primary outcome's change with savings that keep up with prices against the change without them (release row, no shock): a difference in differences.
- **The S19 series:** recorded and checked only (the loader `dev/tools/s19_series.py` in compassionism-simulation); S19 costs them after S48.

## Analysis
- **Estimates:** seed means of paired differences, design minus its own no-programme row (the shocked design against the shocked no-programme row). 95% interval: paired bootstrap over seeds, 2,000 replicates, resampler seed 53, the same resample for every cell (`dev/tools/s53_security.py`).
- **By construction, said so:** `secXe` = 100 with no programme; lower own cost means fewer hours and less exposure; `secPx` counts only drawn moves. A change in these is the design's accounting and is reported as such; it is never called evidence that the design works.
- **Multiple comparisons:** intervals unadjusted at 95%; every cell published. No single favourable group, environment or measure is reported alone.

## Decision rules
1. **A security gain** on a measure is claimed only where the interval of the change excludes zero in the favourable direction, on an emergent or mixed measure, and is stated with the group and environment, for example "under the release row, uncovered income drops among participants fall from x to y per 100 adult-years".
2. **Harm:** where a measure is worse for group X with the programme (interval excluding zero in the unfavourable direction), the report says the design makes non-participants less secure on that measure and names the channel (for example savings losing value to the programme's inflation).
3. **Savings and inflation:** if the change in `secM3` with savings that keep up with prices differs from the change without them (interval of the difference excluding zero), the report says how much of the savings result is inflation's.
4. **Both readings stand:** where the money-income reading (`secU25m`) and the resources reading (`secU25`) disagree in sign, the report gives both and says which part of income the BU replaces.
5. Pilot results are labelled pilot and never quoted as figures of the model. They decide only what S47 carries into the batch.
6. The policy comparison stays frozen (ledger d94): no comparator rows are run.

## Reporting
Every cell above is published, including null and unfavourable results and the Adverse and Stress environments: per-seed values in compassionism-sim-results (`s53-security-<engine>/`, with run.txt and SHA256SUMS), the pilot report `dev/reports/s53-security.md` in the engine repository, and the findings page after S48.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
