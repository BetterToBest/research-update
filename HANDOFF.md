# Handoff (Nov 19, 2026): S90 done (the BU's two-year swing traced to a defect; fix built behind an option; rerun preregistered)

## Step status
**S90 done.** Steps 1-3 are finished: the term was found, it is a defect, and the fix is built with its rerun preregistered. The rerun itself is the new step **S92**. **S89 is Duke's.**

## What shipped
- compassionism-simulation [PR 163](https://github.com/BetterToBest/compassionism-simulation/pull/163) (merged `b8ccd8d`): option `sp.vAt: 'sale'` (off by default; guard test identical; lineage linked), `bizTaxRates`/`bizPremPerBU`, five tests in `privUnitSuite`, trace tool `dev/tools/s90_trace.js`, report `dev/reports/s90-private-price-at-sale.md`, DECISIONS "S90"; unit count 400 in README/CONTRIBUTING.
- research-update [PR 182](https://github.com/BetterToBest/research-update/pull/182) (merged once its link check passed): `prereg/2026-11-s90-private-price-at-sale.md` (engine `b8ccd8d`), outside reading `audits/2026-11-18-s90-reading.md`, PLAN.md S90 notes and S92.

## What was found
- BU budget (about $24,900) < essentials bill (about $30,000), so the BU spent move one for one with the price cuts paid before them. The private businesses' lower BU price (plan step 14) was paid from **last year's** premium shared by last year's BU: a big cut means fewer BU spent, so less premium and a smaller cut the next year. That is the swing. With it off the swing goes; with the community cut off it stays (all three environments).
- Duke's design sets that price at the sale ("$9 menu becomes $3 in BU" at 3x), so it is a defect. Under `vAt: 'sale'`, a BU spent there buys 1 + vK dollars (vK about 0.90, then 0.81; Stress 0.79, then 0.71), paid as an advance that next year's premium repays exactly. The premium on payroll BU returned a year later is still shared by last year's BU.
- Reach: every programme figure since v5.0. On seeds 1-2 (inspection only), the main row's cut in basket poverty grows by 0.6-0.7 points.
- Outside reading (Nemotron 3 Ultra) confirmed the diagnosis, the defect call and the algebra. Two wording fixes were made: the fix is a candidate until the rerun passes, and the community split's yearly timing is labelled a modelling assumption.

## In flight
- Nothing running.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).

## Next step
**S92** (opus, high): add `runner/jobs/s90.js` to compassionism-sim-results, then dispatch the main rows (lagged and at the sale; 500 seeds; three environments; 20 and 40 years) on GitHub Actions. Then S85.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- In the plain framework run (no open access), ESP payroll BU are returned every year, even with no worker cap, so the residual there is not zero. Test it against the returned premium, not against zero.
- Setting a flag with `process.argv.push` after `require` has no effect if the tool reads it at load time.
- After adding tests: `node harness.js unit --write-counts`.
- domtest needs `npm install` in a fresh clone (jsdom).
