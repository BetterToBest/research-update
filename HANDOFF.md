# Handoff (Nov 17, 2026): S80 part 1 done (reader-facing wording on the pages, the Hub and the root site)

## Step status
**S80 partly done.** Everything a reader sees on the Simulation's pages, the Research Hub and the root site now uses versions by number, plain design names and no step codes. **Part 2 remains:** CHANGELOG.md (130 occurrences) and the 95 reports in `dev/reports/` (about 1,400).

## Names (compassionism-simulation `dev/DECISIONS.md`, "reader-facing names")
- Release 1 is **v5.6**; its panel was published Oct 14.
- Release 2 is **v5.9**: frozen Nov 14, first shown in v5.8, leading since v5.9. "Round 2 of the engine" is the v5.9 model.
- "C2.2" is **the full-coverage design**. NEEC's criterion C2.2 is named once, where the design is introduced.
- "The release design" is **the opt-in design**.
- Studies are named by subject (the central-bank study, …).
- Kept as they were: anchors, `?rel=1`, file and folder names, and the labels stored in data files. The pages map stored labels when they print them.

## What shipped
- compassionism-simulation PR 141 (v5.9.6), branch `claude/s80-reader-wording`:
  - the pages, `site/*.js`, glossary, manifest summaries (with `release_data.py`), study text (with `study_data.py`) and CONTRIBUTING;
  - inventory `dev/reports/reader-wording.md`;
  - checks `dev/tools/reader_check.js` (every page rendered with its data, 10 views) and `dev/tools/reader_codes.py --check` (static text and Markdown), both run as domtest Phase 17;
  - domtest 162 checks passed locally.
- research-hub PR 34 (merged `3685f3c`): figure blocks (`build_figures.py`; `--check` ok), the US policy eras page, wiki card and corrections log; four paper PDFs rebuilt.
- bettertobest.github.io PR 6 (merged `6688dc3`): llms.txt, ai-index.json, research-index.json.
- research-update: PLAN.md S80 note and Order row; this handoff.

## In flight
PR 141's checks were running at handoff; see the line below.

## Decisions waiting
S12 (which visuals go on which page) stays Duke's. No new decision: the names describe what each design does and claim nothing new.

## Next step
S80 part 2: reword CHANGELOG.md and `dev/reports/`, then remove the `pending` list in `reader_codes.py` so CI covers them. `python3 dev/tools/reader_codes.py --check --all` lists every remaining occurrence. After that, S13 (outside audits, second round), in a session that did not build the v5.9 model.

## Pitfalls
- The figure check fails on any typed % or $ in the new sections. "100% of basic needs" in a sentence tripped it, so the page says "all basic needs".
- Some domtest checks match page text. A wording change needs the test's expected text changed too (three did here).
- `RL = 'release design'` and `C = 'C2.2'` in `site/cb.js` and `round2.js` are data keys. Never reword them; reword only what is printed.
- In a shell heredoc with an unquoted delimiter, backticks run as commands. Use `<<'EOF'`.
- The scanner skips JEL codes (D60, I32 …), the draft Act's "Part I", and the formula symbol D0. The allow-list is `dev/tools/reader_codes_allow.txt`.
- Hub `data/claims-summary.md` still quotes old wording. It is generated from the claims ledger, so it changes when that ledger is next rebuilt.
- Earlier pitfalls still stand. Release 2's (v5.9's) wealth measures must use the weighted keys. The engine's `cost` is gross. The engine's `dev/CODEMAP.md` is stale. JSON-LD carries Duke's personal email (S42 fixes it).
