# Handoff (Oct 28, 2026): plan set up in the planning chat (S27)

## Step status
S27 (planning) done. Next: **S28**.

## What shipped
- This repository: CLAUDE.md (rules), PLAN.md (36-row order with model and effort), `/start-session` and `/end-session`, `prereg/TEMPLATE.md`, `audits/refine/presence_check.py`.
- Ledger (document `hub`): steps S27-S48 added, decisions D1-D5, issues I9-I11; `next`, `left`, `watch` and `landing` updated.

## Findings from planning (to build on, not redo)
- The two refine.ink audits hold 145 distinct comments (13 on the mechanism-design paper, 132 on the Oct 2025 compendium). 128 of the quoted passages are still on the live Hub; 32 of those survive only in the PDFs (the HTML was corrected but the PDFs were not rebuilt; for example the Bristol Pound "£5 billion" and the 2.86 multiplier).
- Spot-checked arithmetic: the audits are right on the multiplier (1.95), the half-life (3.72 discrete), the steady state (11.8% and 7.4%, both above the theorem's 5%), the elasticity (-1.6), 13 not 15 points, 11% not 14% of GDP; the audit is itself wrong on the $1,847 NPV (its explanation gives $1,832).
- `research-hub/data/optimal-parameters.json` lists $82,000 under PTH parameters as "expected wealth building" (an input); the papers report the same figure as a simulation result with a 95% interval. S30 traces it.
- The ledger's I7 already notes no record that the theta "Monte Carlo calibration" was ever run.
- No tags exist on research-hub (S2). The Hub links one of the 22+ Academia papers (S43).

## Decisions (answered Oct 28)
- D1: tag plus /v1/ archive pages, bannered and hidden from search engines (S2).
- D2: chat exports from both accounts into a private repository; Duke creates BetterToBest/research-provenance and uploads them (S31 waits for that).
- D3: Duke pastes the Academia links into D3's note (S43 waits for them).
- D4: GitHub Actions now; Duke adds the Runpod key once the design is frozen (S47, then S48).
- D5: BeforeIT.jl cross-check after the scale results, regardless (S39).
- Duke, Oct 28: settle every design before any paid run, so nothing has to be rerun. The plan now runs free pilots on Actions (S35), freezes the full design (S47), then runs one batch (S48).
- Duke, Oct 28: sessions should start the next step themselves. AUTOCHAIN.md and `/end-session` step 5 do this; S28 tests it.

## Next step
S28: wiring (merge rule in each repository's CLAUDE.md, ledger pointers, S9, S17, S18, workflow-file test).

## Pitfalls
- Open and merge pull requests with `gh api` (repos/<owner>/<repo>/pulls, then .../pulls/<n>/merge). The GitHub connector's pull-request tools returned 403 here; `git push` works once the repository is attached with add_repo.
- Past-chat search from the claude.ai Project only sees chats inside the Project, so early chats are out of reach there (S31 uses a data export instead).
- The corrections package (C1-C30) and the claims-ledger draft were worked on in the other account; S28 looks for them in these repositories first.
- An older account-level skill also named `start-session` belongs to the CIP portal plan (portal steps 1-12). If `/start-session S28` answers with portal steps, the wrong skill ran: ask Duke to remove that plugin skill (the portal repository has its own `/start-sessions`).
- compassionism-simulation's `/handoff` still points at the other account's ledger until S28 changes it.
