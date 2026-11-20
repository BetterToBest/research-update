# Handoff (Nov 20, 2026): S85 part 3 done (automation batch read: checks, tables, report, outside reading); part 4 next

## Step status
**S85 part 3 done; part 4 next.** All PRs merged. Part 4 needs the six supplement folders `s85sec-<env>-<years>-503fa48` to show `DONE` (running at session end).

## What shipped
- research-update [PR 188](https://github.com/BetterToBest/research-update/pull/188) (merged `f83a608`): prereg Amendment 3 (items 1-11), `audits/2026-11-20-s85-results-reading-nemotron.md` (+ packet, reply), PLAN.md S85 notes.
- compassionism-sim-results [PR 62](https://github.com/BetterToBest/compassionism-sim-results/pull/62) (merged `f260054`): `s85.js --sec`; [PR 63](https://github.com/BetterToBest/compassionism-sim-results/pull/63) (merged `020c4b1`): `s85-tables-503fa48`.
- compassionism-simulation [PR 169](https://github.com/BetterToBest/compassionism-simulation/pull/169) (merged `171a27d`): `dev/reports/s85-output-per-hour.md` (section 14 = findings-page text), `dev/tools/s85_tables.py`, DECISIONS "S85 part 3". No engine change.

## What was found
- Checks 1-9 pass in all six folders; the main rows (option off) equal the published main rows at the sale in every key and seed.
- No programme: displacement raises basket poverty 2.0-12.6 points by year 20 (Reference). Full coverage at full backing offsets 80-100% of it and 13-40% of the median-wealth fall (all 144 tests significant). Opt-in offsets far less and, with lost jobs, worsens the rise in 9 of 12 cells (head-count effect + rising contribution; severity still offset).
- Produced backing 5-18% (full coverage), 3-8% (opt-in); inflation 18-71 points/yr at 20 years, up to 82 at 40; no break-even m. Rule 5 binds every full-backing headline.
- Savings is read on `bNAPy` until the supplement's `secM3A` lands.

## In flight
- Supplement runs 161-166 on compassionism-sim-results (Actions; engine `503fa48`; `s85.js --sec`; 20 shards each). At 03:25 UTC run 161's shards had all succeeded and its finish job was queued. Results: `s85sec-<env>-<years>-503fa48/` with `DONE`. A failed shard: "Re-run failed jobs".

## Decisions waiting
- D33 (headline cards' headings and the full-backing condition; default: no change).
- D34 answered (Nov 19): hold the release; S93 on hold.

## Next step
**S85 part 4** (opus, xhigh): rerun `python3 dev/tools/s85_tables.py <results> <out>` into `s85-tables2-503fa48` (merges `secM3A` for blocks A and F after check 10), update the report's savings lines and section 4 table; full trace of the opt-in worsening; findings-page section from report section 14 (as the supply study's part 3b), unless D34's hold covers it.

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
- An NVIDIA reasoning model can spend its whole `max_tokens` on reasoning and return no answer: give it 40,000 for a long packet.
- `s85_tables.py` takes about 25 minutes for six folders: run it in the background.
- `mfChk` is not 0 on flat-contribution main rows: never a pass/fail check there.
- Each push to a PR branch queues new CI runs; cancel the stale ones (runners are shared with study shards).
