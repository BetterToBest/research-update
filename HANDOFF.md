# Handoff (Nov 20, 2026): S95 done; next S94

## Step status
**S95 is done**, with an added correction (Duke, Nov 20): the model frozen and registered on OSF is v5.8 (engine 104691f, no central bank), not v5.9. S85 part 5 is also merged.

## What shipped
- research-hub [PR 39](https://github.com/BetterToBest/research-hub/pull/39), merged `4f7a32a`: dated note on Pencavel (2015) in the corporate transformation paper, corrections log entry, PDF rebuilt. The root-site indexes do not quote the figure.
- compassionism-simulation [PR 172](https://github.com/BetterToBest/compassionism-simulation/pull/172), merged `3835242`: "frozen and registered" now names v5.8 on the findings page, simulation page, README, replication page, manifest summary, round-2 basis line, CHANGELOG and the findings-page text report. Wording only; local checks and CI passed.
- compassionism-simulation [PR 171](https://github.com/BetterToBest/compassionism-simulation/pull/171), merged `e9fd0a3` (S85 part 5, the automation section on the findings page).
- This file and PLAN.md: research-update PR 192.

## What was found
- Left as history on purpose: DECISIONS.md entries, earlier release notes, and the `prereg` fields in the round-2 data files (they name the registration, not a version). The Hub and root site never made the mistake.
- The Hub claims table (`data/claims.csv`, R297) still marks the Pencavel sentence "keep"; not edited (surgical).
- The Hub's reader-codes check shows one existing hit ("Part B", `us-money-history.html`), not from this step.

## In flight
- Nothing running.

## Decisions waiting
- D33 (headline cards' headings and the full-backing condition; default: no change).
- D34 answered (Nov 19): hold the release; S93 on hold.

## Next step
**S94** (opus, high): the Creative Collectives' lending to start-ups where banks will not lend. Claude's reading of the design (read the Hub papers first), sources, preregistration, then a switch. Read Duke's Nov 19 note on S94's ledger step first: small essential providers get support with premises, logistics and setup costs; large utility and transport projects are usually financed by municipal bonds and public debt (Claude's research), with public operators as a possible move to Collective charters. Attach compassionism-simulation (push).

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
- `node dev/tools/check_round2.js` (every printed number on the v5.9 findings section is tied to a row of its file) is not run by CI: run it by hand after editing `site/round2.js`. A share printed as a percent must be stored as a percent in the data file, or the check fails.
- PR 172 was merged after PR 171 landed, on checks that ran before it; wording only, so accepted.
- The GitHub tools disconnect after a worker restart; a ToolSearch for them reconnects.
