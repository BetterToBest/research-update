# Handoff (Oct 30, 2026): S31 chat-history provenance of the early figures

## Step status
S31 **done**. D2 is answered: the five zips in the private repository research-provenance cover what S31 needs.

## What shipped
- research-update [#15](https://github.com/BetterToBest/research-update/pull/15) (merged, 98bc2b1): section "Chat-history provenance (S31)" in `audits/early-figures.md` (figure, Hub date, first date in the chats, author, run or source, basis); `audits/early/provenance_scan.py`; PLAN.md marks S31 done.
- Findings: Claude wrote each figure first, in drafts dated Aug 1-26 and Sep 5, 2025; Duke's first mention is Sep 21 or later. Most of the Hub block came from one reply on Aug 25, 2025 (chat `68fe152d`). No code ran for any figure: the export's 41 shell calls are all Nov 4-8, 2025. Five figures appear in no chat before the Hub (65% inflation, elasticity table, $64,000-$103,000 interval, 75% minimum viable participation, 88% work participation).
- No chat text or personal data was copied into any repository.

## In flight
Nothing.

## Decisions waiting
None.

## Next step
**S32** (preregister the study program), opus, high: S33 and S34 are done. Carry Q6 (the yardstick) and ledger issue I15 into it. S32 can cite the S31 table. The chain is off (`AUTOCHAIN.md`), so Duke starts it by hand.

## Pitfalls
- `/start-session` and `/end-session` cannot be run by Claude; the first attempt in this session was refused until Duke ran it.
- A bare-number search (for example "65%") matches unrelated text; every hit in the table was read by hand. The script's raw output is noisy.
- The export covers one account, has 8 empty conversations and only 2 in October 2025. "Not in any chat" does not prove a figure had no earlier source.
- An Aug 26, 2025 chat asked for an author line naming a Claude model on the papers. If S24 or S25 touches that line: no model names in pushed files (CLAUDE.md).
- The research-provenance repository holds phone, email and login IPs in `light_metadata`; never copy them.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model names).
