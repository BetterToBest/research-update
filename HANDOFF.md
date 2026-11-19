# Handoff (Nov 19, 2026): S92 part 1 done (the at-sale rerun is running; the swing is gone)

## Step status
**S92 partly done.** Steps 1-4 are finished. Step 5, reading the six result folders under the decision rules and publishing every cell, is **S92 part 2**. **S89 is Duke's.**

## What shipped
- compassionism-sim-results [PR 58](https://github.com/BetterToBest/compassionism-sim-results/pull/58) (merged `c2a0970`): `runner/jobs/s90.js` with five rows: no programme, and the full-coverage and opt-in designs, each late and at the sale. Part M's financed rows are left out.
- compassionism-sim-results [PR 59](https://github.com/BetterToBest/compassionism-sim-results/pull/59) (merged `7b25594`): folder `s90-swing-b8ccd8d` (the swing measure, check 3, run.txt, SHA256SUMS).
- compassionism-simulation [PR 164](https://github.com/BetterToBest/compassionism-simulation/pull/164) (**open**: CI was queued behind the study shards, and this repo has auto-merge off): `s90_swing.js`, `s90_acct.js`, `s90_tables.py`, `s90_trace.js --from`, and the report section "The rerun, part 1". No engine change. Merge it once green.
- research-update (this PR, branch `claude/s92-reader-rule`): HANDOFF's Standing rules, `/end-session` told to keep them, preregistration Amendment 1 (clarifications only), PLAN.md S92 notes.

## What was found
- Swing measure (seeds 1-20, per seed then averaged), at the sale over late: Reference 0.124, Adverse 0.201, Stress 0.224. All are below 0.5, so decision rule 2 holds.
- Check 3 passes: no accounting identity fails on the at-sale rows (seeds 1-5, three environments).
- Two-seed trial of check 1: the no-programme and late rows equal `r2-m-ref-20-104691f` on all 5,862 values.

## In flight
- Six `run-study` runs on GitHub Actions in compassionism-sim-results, dispatched Nov 19 01:02 UTC (runs 149-154). Pinned to engine `b8ccd8d`, seeds 1-500, 20 shards each. Results land in `s90-sale-<ref|adv|str>-<20|40>-b8ccd8d`; each run is done when its folder has a `DONE` file. Expected within about an hour.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S92 part 2** (opus, high): merge PR 164, check that the six folders have `DONE`, then run `python3 dev/tools/s90_tables.py ../compassionism-sim-results OUT --swing ../compassionism-sim-results/s90-swing-b8ccd8d/swing.json --acct ../compassionism-sim-results/s90-swing-b8ccd8d/acct.json` (it stops if check 1 or 2 fails). Read under the decision rules, publish the tables to sim-results and the report, read Q3 against the findings page, and add dated notes on the other reached studies (rule 5). Then S85.

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
