# Handoff (Nov 20, 2026): S85 part 4 done (supplement read, opt-in worsening traced); part 5 (findings-page section) next

## Step status
**S85 part 4 done; part 5 next.** Part 5 is the findings-page section only: nothing else of S85 is open. The pull request below (compassionism-simulation PR 170) is open at this commit (its guard check passed; the main check was still running).

## What shipped
- compassionism-sim-results [PR 64](https://github.com/BetterToBest/compassionism-sim-results/pull/64) (merged `257b6c1`): `s85-tables2-503fa48` (the tables with the real savings measure; check 10 passes in all six folders; the first folder kept as published). [PR 65](https://github.com/BetterToBest/compassionism-sim-results/pull/65) (merged `327200b`): `s85-trace-503fa48` (the trace; all checks pass).
- compassionism-simulation [PR 170](https://github.com/BetterToBest/compassionism-simulation/pull/170): the report's savings lines, counts, section 4 row and category grid, the trace subsection, `dev/tools/s85_trace.py`, DECISIONS "S85 part 4". No engine change.
- research-update (branch `claude/tender-rubin-w7xl7i`): prereg Amendment 4 (committed before the trace was computed), `audits/2026-11-20-openrouter-setup.md` and a CLAUDE.md line (the OpenRouter route), the outside-reading packet and reply (`audits/2026-11-20-s85-part4-reading.md`: Nemotron on OpenRouter answered; Gemma was rate-limited upstream on every try, so there is no Google reading; no figure moved, four wording fixes in the report), PLAN.md notes.

## What was found
- Savings, on the preregistered measure: with full coverage the programme offsets 66-94% of displacement's rise (the stand-in read 97-102%); opt-in 3-47% with shorter hours and -7% to 19% with lost jobs, and it worsens the rise in Stress at 50% and 70% lost jobs. Counts at 20 years: full coverage 142 in part, 2 fully; opt-in 88 in part, 39 do not offset, 17 worsen (40 years: 75, 32, 37). At the produced backing: 7-48% (full coverage), 0-23% (opt-in).
- The trace: where the opt-in design makes the rise in basket poverty larger with lost jobs (9 of 12 cells, at 20 and at 40 years), the adults who would take part carry 71-89% of it (62-87% at 40); it is a head count, not depth; enrolment does not fall; the contribution's rise is as large with full coverage, where nothing worsens; the adults who would not take part carry 11-29% (contribution and programme inflation together, not separated).

## In flight
- compassionism-simulation PR 170: checks running; merge it once they pass (auto-merge is off). If they fail and cannot be fixed, leave it open and say so here.
- Gemma (Google, via OpenRouter) was never served: try it again for the part 5 text if a different maker's reading is wanted; 4 of the day's 50 free requests were used.

## Decisions waiting
- D33 (headline cards' headings and the full-backing condition; default: no change).
- D34 answered (Nov 19): hold the release; S93 on hold. It covers the version and the main rows' default, not a study section on the findings page.

## Next step
**S85 part 5** (opus, high): the findings-page section. Attach compassionism-simulation (push). Write `dev/tools/s85_page_data.py` (pattern: `dev/tools/s82_page_data.py`) to make `data/studies/s85-automation.json` (block A, six readings, by environment, horizon, design, form and D: costs, offset share with interval, category) and `s85-backing.json` (every non-floor backing row: programme inflation and produced share with intervals) from `s85-tables2-503fa48/s85-summary.json`; add `s85Section()` to `site/round2.js` after the supply study's (add the files to `FILES`), with the words of report section 14 and every figure read from the data; keep the page's rules (no wealth figure without its price rule, every inflation figure with the backing statement beside it, unfavourable cells named beside favourable ones). Run `node domtest.js`-level checks the CI runs and `python3 dev/tools/reader_codes.py --check` before pushing. Landing: pull request, merge once checks pass.

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
- OpenRouter's free tier (`openrouter.ai`, ids ending `:free` only; 50 free-model requests a day; free providers may keep prompts, so send only public text, with the author's name turned into a role) is a second route for outside readings: `audits/2026-11-20-openrouter-setup.md`. Google's Gemma was rate-limited upstream (429, a shared pool) on every try; Nemotron on OpenRouter answers. `audits/openrouter-2026-11-20-s85-part4/ask.py` sends a packet and saves the reply.
- A `SHA256SUMS` made with `ls | xargs sha256sum > SHA256SUMS` lists itself and cannot match: leave it out (`ls | grep -v '^SHA256SUMS$'`), then `sha256sum -c`.
- The page's figures are read from `data/studies/*.json` by `site/round2.js` (`show`, `find`, `snum`; no figure typed there); the supply study's tool `dev/tools/s82_page_data.py` is the pattern. The report's backing ranges (5-18%, 3-8%, 18-71 points a year) are over every non-floor backing row (main readings and variants); the 72 main-reading rows alone give 6-17%.
- The results clone's sparse checkout needs `s90-sale-*-b8ccd8d` (check 1) as well as `s85-*` and `s85sec-*`; the tables tool took about 12 minutes for six folders this time, the trace tool about 2.
