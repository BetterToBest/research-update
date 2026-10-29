# Handoff (Oct 29, 2026): S23 claims ledger

## Step status
S23 **done.** Every figure on the live Hub (6,577 on 55 pages, Markdown pages, PDFs and `data/optimal-parameters.json`) has a basis class and an action, each set by a rule written after reading the passage. S2 is closed: Duke answered D7 (skip the tags; the /v1/ archive and its README name the commit). Next: **S30**.

## What shipped
- research-hub PR [#7](https://github.com/BetterToBest/research-hub/pull/7), merged as `7e3b829`: `tools/extract_claims.py`, `tools/class_claims.py`, `tools/claims_review.py` (the reviewed rules, and Claude's reading of rule 5 in its docstring), `data/claims.csv`, `data/claims-summary.md`. No Hub page changed. Rerun with `python3 tools/class_claims.py` (research-update beside it, for the S29 triage).
- Counts: simulation 6, derived 894, external source 226, design parameter 1,856, illustrative projection 420, corpus metadata 662, no basis found 2,513. Actions: keep 3,464, correct 922, relabel 912, remove 1,279.
- The session-5 records S5-01 to S5-13 are merged (`prior_id`); 84 S29 ids are linked (`s29_id`). The original claims-ledger draft never came over (S28), so the ledger starts from the Hub as it is.
- Sources opened: the ONDCP critique of the Portugal report (deaths 369 in 1999, 280 in 2001, 152 in 2003, 314 in 2007; nothing supports "fell by 95%"; Greenwald's own PDF is blocked to fetching); Wikipedia's Bristol pound entry citing the Bristol Post (GBP 5 million spent by late 2017, not 5 billion).

## In flight
Nothing.

## Decisions waiting
- None. D7 is answered (no tags). New ledger issue I12: the 168 unopened cited sources and the longer PDFs (for S24/S25).

## Next step
S30 (where the early figures came from), opus, high. It waited only on S23. Its inputs are the rows with `claimed` = "simulation result" (and the `data/optimal-parameters.json` rows): filter `data/claims.csv` on class "no basis found" and claimed "simulation result".

## Pitfalls
- 168 cited external figures are classed "external source" but not opened (`checked` = "cited, not opened"). S24/S25 open each before a rewritten paper keeps it.
- 1,709 figures are in a PDF only. Several PDFs are longer papers than their HTML pages (citizens-internet-portal 59 pages, corporate-transformation 45 pages, public-trust-financial is an older version). Rebuilding those PDFs from the HTML (S24) drops that content; decide per paper.
- PDF text runs table cells together. The classer matches PDF rows only 70 characters around the figure and lets a PDF figure take its HTML page's class before any page-wide fallback; keep that order if rules are added.
- The extractor once dropped "2,000" and "18-24" as calendar years (fixed). After any change, run the coverage check in the PR history: every number on a page is either extracted or a section number, year or citation marker.
- Rule numbers (`R123`) change when rules are inserted; the rule text in `claims_review.py` is the record.
- `papers/corporate-transformation.html` carries "[cite: N]" drafting placeholders; `assets/downloads/README.md` describes a package that is not in the repository (both marked remove).
- The github plugin server failed to connect again; the GitHub tools via ToolSearch worked.
