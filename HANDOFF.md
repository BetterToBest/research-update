# Handoff (Oct 29, 2026): S29 refine.ink audit triage

## Step status
S29 **done.** All 145 comments are classified, and `recompute.py` runs clean (64 checks). S2 is still partly done (the tags, D7). Next: **S23**.

## What shipped
- research-update: the S29 pull request (link and merge commit in the ledger log). Files: `audits/refine/triage.md` (summary and item lists), `triage.csv` (one row per comment), `recompute.py`, `triage.py` (rebuilds the CSV, the triage.md lists and the additions file), `presence_check.py` fixes, and `audits/corrections-additions.md` (53 headline and derivation items for S24).
- Checked against research-hub `8a72c68`, read only. Nothing changed on the Hub.
- Result: 99 comments live, 36 PDF-only, 10 gone. 124 valid, 5 partly valid, 0 wrong, 16 moot. Of the live ones, 96 are valid: 30 change a headline figure, 23 a derivation, 43 wording only.

## In flight
Nothing.

## Decisions waiting
- D7 (from S2): Duke to create tag `hub-v1` and the releases by hand. Default: carry on without them.
- No new decisions from S29.

## Next step
S23 (claims ledger), opus, high. It waited only on S29. Its `S29 id` column should cite the ids in `audits/refine/triage.csv`. Each headline row there is a figure S23 must class; most have no run behind them.

## Pitfalls
- presence_check.py treated a bare "<" (for example "p* < 0.05") as the start of an HTML tag, which hid text on several pages. It is fixed, and ten locators were corrected. The Oct 28 counts (128 present, 32 PDF-only) were therefore slightly off: the true counts are 132 and 33.
- Several HTML pages (optimal-transfer-design, dual-currency-inflation, drug-policy-reform) are rewrites of their PDFs, not copies: figures differ between the two (drug-policy integrated net value: $5.0T on the HTML page, $4.7T in the PDF). Judge the HTML. The PDF-only rows are fixed by rebuilding the PDFs (S24).
- The audit's critiques hold, but some of its explanations do not. On B097, B053, B093, B017, B095, B036, B075, B016 and B083 it supplies a reconciliation the paper does not state (listed in triage.md). Do not cite those explanations as the paper's.
- The B028 (Portugal) and B011 (Bristol Pound) source figures were not opened this session. S23 opens them.
- The github plugin server failed to connect at start again, as in S2.
