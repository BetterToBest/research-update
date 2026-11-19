# Handoff (Nov 19, 2026): S92 done (the private price at the sale is the corrected model)

## Step status
**S92 done.** The rerun passed every check. Setting the private businesses' BU price at the sale makes every poverty and wealth effect of the main rows slightly larger in the programme's favour, and changes no sign. **S89 is Duke's.**

## What shipped
- compassionism-sim-results [PR 60](https://github.com/BetterToBest/compassionism-sim-results/pull/60) (merged `e831444`): folder `s90-tables-b8ccd8d`, with every cell and its interval, the findings-page reading, run.txt and SHA256SUMS.
- compassionism-simulation [PR 165](https://github.com/BetterToBest/compassionism-simulation/pull/165) (**open**: its CI was still running at session end, and auto-merge is off). It holds the report section "The rerun, part 2", `dev/tools/s90_page_check.py`, dated notes on the findings page (v5.9 and v5.6 sections) and in eight reports, and `dev/DECISIONS.md` "S92 part 2". Locally domtest (162), `check_round2.js`, `reader_codes.py --check` and glossary passed. **Merge it once green** (merge commit, not squash: run.txt cites commit `8897f34`).
- research-update (this PR): PLAN.md S92 notes, this handoff.
- Earlier this step: compassionism-simulation PR 164 and research-update PR 183, both merged.

## What was found
- Checks 1 and 2 pass in all six folders: the no-programme and late-price rows equal the published rows on 1,465,500 values each. Check 3 passed in part 1. So under decision rule 3, the price at the sale is the corrected model.
- Every poverty and wealth effect grows in all 24 cells, each interval excluding zero after Holm. Basket poverty is 0.28-0.59 points lower (full coverage) and 0.04-0.26 lower (opt-in). Median real wealth is $110-1,525 higher. Programme inflation moves by under 0.001 points a year. The 40-year changes are about half the 20-year ones. No secondary reading changes sign.
- Findings page, at its printed precision: 45 of 60 main-row effects change in the last digit. None changes sign or falls outside the printed range across readings, and the prose holds. The cards would read 0.8%, 3.2%, 5.7% and $432,879 (now 0.9%, 3.7%, 6.0% and $432,297). An inspection of 180 distribution and work effects found no sign change.
- The page gets dated notes, not new figures: rule 3 replaces the figures at the release. The other reached studies are not rerun now; each rerun is its own amendment, best done on the release engine.

## For the next release (Duke sets the version)
Make `sp.vAt: 'sale'` the default, regenerate the main rows' page data from the at-sale rows, and add a Hub corrections-log entry. The readings, financed rows and erosion shares stay late-price until rerun.

## In flight
Nothing.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S85** (opus, xhigh): output per hour, modelled. First merge compassionism-simulation PR 165 if it is green.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- `s90_trace.js --seed=N` alone pools seeds 1 to N into one series. Use `--from=K --seed=K` for one seed.
- compassionism-simulation has auto-merge off, and its CI queues behind running study shards. Don't wait: leave the PR open and say so here.
- In the plain framework run (no open access), ESP payroll BU are returned every year, even with no worker cap, so the residual there is not zero. Test it against the returned premium, not against zero.
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- `s90_tables.py` flags a "rounding" change at 2 decimals, so it flags nearly every cell. The findings page prints 1 decimal. Read the page with `s90_page_check.py`.
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
