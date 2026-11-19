# Handoff (Nov 19, 2026): S85 part 2 done (output per hour and automation built, sourced, dry-run and dispatched)

## Step status
**S85 parts 1 and 2 done; part 3 is next** once the six result folders show `DONE`. Part 2: Duke's four sources opened and the three values fixed, row option `oh` built behind its switch (off = identical), preregistration Amendment 2, dry run (every check passes), six runs dispatched on Actions.

## What shipped
- compassionism-simulation [PR 167](https://github.com/BetterToBest/compassionism-simulation/pull/167) (merged `503fa48`, v5.9.21): row option `oh` (displacement as lost jobs or shorter hours, output per hour, the dividend to owners; programme-only `kp` and `bk`), MODEL_SPEC section 17, `sources/s85_values.py` with extracts, `sources/s85_output.md` updated, 8 unit tests (408 in all), `dev/DECISIONS.md` "S85 part 2", the lineage link (all six panels' fingerprints unchanged). Guard test identical.
- compassionism-sim-results [PR 61](https://github.com/BetterToBest/compassionism-sim-results/pull/61) (merged `0a7c264`): `runner/jobs/s85.js`, 179 rows per environment and horizon.
- compassionism-simulation [PR 168](https://github.com/BetterToBest/compassionism-simulation/pull/168) (**open**: the engine repository's HANDOFF.md line for v5.9.21; its CI queues behind the study's 120 shards). Merge it once green.
- research-update PRs 186 and this one: `prereg/2026-11-s85-output-per-hour.md` Amendment 2 (items 1-14), PLAN.md S85 notes, this handoff.

## What was found
- Sourced values: `own` 0.541 (Rosenthal and Burke 2020, Table 4: US households' share of US corporate equity), s_L 0.542 (BLS nonfarm business labour share, 2025), yK 0.164 (BEA 2024, capital income per dollar of capital in the essentials industries, basket-weighted); `vk` 0.421 capped at 0.32.
- McKinsey and Goldman Sachs read in the original change no reading. The four-day week pilot (hours 38 to 34, revenue +1.4%, volunteers, no comparison group) is context only.
- The preregistration's check 6 could not hold as written (the a = 0 row counts the project payout at market value; the produced backing replaces that valuation). Corrected in Amendment 2 before any run.
- `conv` adds nothing in the main row (every expired BU goes to the project pool); its rows equal their counterparts.
- Dry run: every check passes; about 100 core-hours. A one-seed unit test suggests the produced backing covers about a sixth of the payout, with programme inflation near 50% a year at D 0.5. Not a result.

## In flight
Six `run-study` runs on compassionism-sim-results (dispatched Nov 19, 22:07 UTC; engine `503fa483f9711900054842e75fc0edc01eba8dc9`; job `s85.js`; 20 shards of 25 seeds; `--procs=4`). Runs 155-160: [155](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625486750), [156](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625492284), [157](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625498538), [158](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625502788), [159](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625507182), [160](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44625512672) (dispatched in the order ref-20, adv-20, str-20, ref-40, adv-40, str-40 at the same second, so match each run to its study by its inputs, not its number). Results land in `s85-<env>-<years>-503fa48/` (`run.txt`, `SHA256SUMS`, `DONE`). A failed shard: "Re-run failed jobs" on its run.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).
- D34 answered by Duke (Nov 19): hold the release. S93 stays on hold.

## Next step
**S85 part 3** (opus, xhigh), once all six folders show `DONE`: the preregistered checks on the batch (1-9; the dry-run checks in `/tmp` are gone, rebuild from Amendment 2 items 7 and 13), the tables (offsets with Holm across the 32 block-A tests, Q4's categories and break-even m, free time split), the plain-words report `dev/reports/s85-output-per-hour.md`, the findings-page text, an outside reading of the results. If a folder is not `DONE`, re-run its failed jobs and end.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- `expectedHeadSha` in a merge call must be the exact 40-character head; take it from `git ls-remote origin refs/heads/<branch>`, never guess the tail.
- BLS refuses direct requests and its API key's daily quota is shared: fetch BLS files through the fetch tool (it saves binaries in `tool-results/`), then parse them with `openpyxl`.
- The `oh` rows' no-programme runs are shared by both-run settings (`none.<key>` rows in `s85.js`): pair each programme row with the `none` row its `rowSpec` names, not with `none.off`.
- `/end-session` cannot be started by Claude (the Skill tool refuses it); Duke types it. Land PRs as you go so little is left for it.
- McKinsey, Goldman Sachs, OECD and Autonomy refuse automated fetches; open a paper's own PDF or a paper that quotes it, and label a quoted figure as context only. PDFs the fetch tool saves can be read with `pdftotext`.
- The GitHub tools failed to connect at session start; a ToolSearch for them reconnected.
- The Hub is cloned read-only at `/home/user/bettertobest/research-hub` for reading its papers (S95 needs it attached with push).
- compassionism-simulation has auto-merge off, and its CI queues behind running study shards. Don't wait: leave the PR open and say so here.
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
