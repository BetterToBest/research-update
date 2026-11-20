# Handoff (Nov 20, 2026): S85 part 3 done (the batch read: checks, tables, report, outside reading); the savings supplement in flight

## Step status
**S85 part 3 done; part 4 is next** once the six supplement folders `s85sec-<env>-<years>-503fa48` show `DONE`. Part 3: Amendment 3 before any table was read, checks 1-9 pass in all six folders, the tables, the plain-words report with the findings-page text, and an outside reading acted on.

## What shipped
- research-update (this branch's PR): `prereg/2026-11-s85-output-per-hour.md` Amendment 3 (items 1-11: the savings outcome's supplementary run, Holm over 48, the D 0 references, signs, rebuilt checks, check 7 read as an inspection); `audits/2026-11-20-s85-results-reading-nemotron.md` with its packet and reply; PLAN.md S85 notes.
- compassionism-sim-results [PR 62](https://github.com/BetterToBest/compassionism-sim-results/pull/62) (merged `f260054`): `s85.js --sec` (blocks A and F with the security measures on, 48 rows; without the flag the job is unchanged). [PR 63](https://github.com/BetterToBest/compassionism-sim-results/pull/63) (merged `020c4b1`): `s85-tables-503fa48` (checks, tables at 20 and 40 years, `s85-summary.json`, `analysis.txt`).
- compassionism-simulation [PR 169](https://github.com/BetterToBest/compassionism-simulation/pull/169) (branch `claude/s85-tables`; see In flight): `dev/reports/s85-output-per-hour.md` (section 14 is the findings-page text), `dev/tools/s85_tables.py`, `dev/DECISIONS.md` "S85 part 3", CODEMAP, its HANDOFF line. No engine change.

## What was found
- Checks: all pass. Check 1 is strong: the main rows with the option off equal the published main rows at the sale in every key and seed.
- Displacement with no programme raises basket poverty 2.0-12.6 points by year 20 (Reference; 1.6-9.6 Adverse and Stress) and lowers median wealth $7,158-$48,326.
- Full coverage at full backing: offsets 80-100% of the rise in basket poverty, 59-97% of wealth poverty's, 97-100% of the basic-living measure's, 13-40% of the fall in median wealth; all 144 tests significant (136 in part, 8 fully).
- Opt-in: offsets far less; with lost jobs it worsens the rise in basket poverty in 9 of 12 cells (98 in part, 31 do not offset, 15 worsen at 20 years; 80/32/32 at 40). Inspection (Adverse, seeds 1-100): a head-count effect (participants held just above the line by their wage) and the flat contribution rising 3.5% to 4.5% as wages shrink. On poverty severity the opt-in programme offsets part of the rise in every lost-jobs cell (0.4-9.9 points), which fits the head-count reading.
- The backing produced: 5-18% of the payout (full coverage), 3-8% (opt-in); inflation 18-71 points a year at 20 years, up to 82 at 40; all 44 rows "do not back enough" in every cell; no break-even m. Decision rule 5 binds every full-backing headline.
- Free time at 50% lost jobs: 494 freed hours a year; insecure 76-81% with no programme, 4-10% full coverage, 55-77% opt-in.
- The fourth primary reading is `bNAPy` (below 30 days of basic living) until the supplement is read; the preregistered `secM3A` was never switched on in the batch.

## In flight
- Six supplement runs on compassionism-sim-results (dispatched Nov 20, 02:23 UTC; engine `503fa48`; job `s85.js --sec`; 20 shards of 25 seeds): runs [161](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/44660461514) to 166, in the order ref-20, adv-20, str-20, ref-40, adv-40, str-40. Their shards were still queued for runners when this session ended. Results land in `s85sec-<env>-<years>-503fa48/`. A failed shard: "Re-run failed jobs".
- compassionism-simulation PR 169 and research-update PR 188: their checks queue behind the supplement's shards. Merge each once green (`expectedHeadSha` from `git ls-remote origin refs/heads/<branch>`); if this handoff is not on main, read it from branch `claude/compassionate-franklin-c9ginb`.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).
- D34 answered by Duke (Nov 19): hold the release. S93 stays on hold.

## Next step
**S85 part 4** (opus, xhigh), once the six `s85sec-*` folders show `DONE`: rerun `python3 dev/tools/s85_tables.py <results> <out>` into a new folder (`s85-tables2-503fa48`; the tool merges `secM3A` for blocks A and F once check 10 passes), update the report's savings lines and section 4's table; trace why the opt-in design worsens displacement's cost with lost jobs (decompose the head-count effect, the contribution and who takes part); the findings-page section from the report's section 14, as the supply study's part 3b did (`site/round2.js`, `data/studies/`), unless D34's hold covers it. If a folder is not `DONE`, re-run its failed jobs and end.

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
- An NVIDIA reasoning model can spend its whole `max_tokens` on reasoning and return no answer (`finish_reason` "length", content empty): give it 40,000 for a long packet.
- `s85_tables.py` takes about 25 minutes for the six folders (10,000 replicates): run it in the background.
- `mfChk` is the Source-financing identity, not 0 on the flat-contribution main rows: never read it as a pass/fail check there.
