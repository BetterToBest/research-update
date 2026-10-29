# CLAUDE.md: Research Update workbench

This repository coordinates one project across several repositories: develop the Compassionism Simulation, rebuild the Research Hub on its findings (Hub v2), then finish NEEC. It holds the plan, the handoff, preregistrations and audit triage. Work products land in the repositories below.

Duke Johnson wrote the concepts and is the framework's advocate. Claude is responsible for the math, the code, and presenting the research clearly and accurately. Duke has delegated every math, code and modelling decision to Claude.

## Start, work, stop
- Start with `/start-session <step ID>` (for example S29, or N-S70 for NEEC). Read `HANDOFF.md` and only that step's section of `PLAN.md`.
- End with `/end-session`. Every session ends with it.
- Tokens: grep and line ranges; never read a whole file over 300 lines; no screenshots unless the step is visual; never wait or poll for long jobs (start them, check once that they started, record where results land, end).
- No model names in commits, pull requests, release notes or any pushed file. The next-session suggestion goes in the chat reply only.

## Repositories (attach with add_repo, access "push"; only those the step names)
| Repository | What | Its rules |
|---|---|---|
| BetterToBest/compassionism-simulation | the engine (`index.html`; `harness.js` for studies) | its CLAUDE.md; guardrails 1-9 apply to every engine change |
| BetterToBest/compassionism-sim-results | study outputs, one folder per study: `<study>-<engine commit, 7 chars>` | run.txt and SHA256SUMS beside every result |
| BetterToBest/research-hub | Hub pages and papers (bettertobest.github.io/research-hub/) | surgical edits |
| BetterToBest/bettertobest.github.io | root site: ai-index.json, research-index.json, llms.txt | kept in step with the Hub |
| BetterToBest/NormativeEvaluation | NEEC | its CLAUDE.md and STATE.md |

Linked, not edited unless a step says so: BetterToBest/portal, BetterToBest/x-cents.

## Landing work (Duke's instruction, Oct 28, 2026)
- In each repository you change: a `claude/<step>-<topic>` branch, a pull request, and, once its checks pass, merge it yourself. Duke is not asked to review or merge.
- Never push to main directly, force-push, rewrite history, or move, delete or re-create a tag.
- If checks fail and you cannot fix them this session, leave the PR open and say so in HANDOFF.md.
- If GitHub refuses a workflow file, put its full text in the PR description and add a ledger decision asking Duke to create it by hand.
- What only Duke can decide goes to the ledger as a decision (`/end-session`). Carry on with the default meanwhile unless the step says to stop.
- **Money:** nothing that costs money (Runpod) runs before the S47 design freeze, its ledger decision, and Duke adding the Runpod key. Pilots and tests use GitHub Actions (free) or the session machine. A full study is run once, as frozen; a redesign is a preregistration amendment and a new freeze.
- Sessions may chain themselves (`AUTOCHAIN.md`); every gate above stops the chain.

## Research rules (every step)
1. **Preregister, then run.** Every study has a file in `prereg/` (questions, design, outcomes, analysis, decision rules, engine commit), committed before its first run. Later changes are dated amendments with the reason.
2. **Publish every result.** Every preregistered outcome goes to compassionism-sim-results and the findings page, including null results and the Adverse and Stress environments. Advocacy material may lead with the strongest robust findings; nothing is dropped from the record.
3. **No target results.** No constant is tuned to reach a figure. Constants come from cited primary sources or are labelled design parameters and swept. Earlier figures (before v5, and the Hub v1 papers) are not targets: S30 records which were never produced by any run or came from errors since fixed.
4. **Synergy is measured.** Report interaction effects with intervals (factorial designs, Shapley shares). A synergy is claimed only where the interaction's 95% interval excludes zero.
5. **Every Hub figure has a basis class:** simulation release and command; derived calculation (file); external source (opened); design parameter; illustrative projection; corpus metadata. Figures with no basis are corrected, relabelled or removed, never revived.
6. **Concept questions:** read the Hub papers first, write "Claude's reading of the design" in a short note, take the most cautious reading where the text is silent, and label it a modelling assumption. A change to the design itself (not to the model of it) is Duke's call: ledger decision.
7. Reports and notes make sense on their own, in plain words; ledger IDs may follow in parentheses.
8. Attribution: the text in compassionism-simulation's CLAUDE.md.

## The ledger
Artifact https://claude.ai/artifact/F1hceP6XEfPQ1pf6Sw1Ki8, database collection `projects`: document `hub` (code H, this plan) and `neec` (code N). Read only the fields you need. `/end-session` describes the write and the fallback (`ledger-sync/`).

## Files here
`HANDOFF.md` (start here) · `PLAN.md` (steps, order, model and effort) · `prereg/` · `audits/` · `ledger-sync/` · `.claude/skills/` (start-session, end-session)
