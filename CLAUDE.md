# CLAUDE.md: Research Update workbench

This repository coordinates one project across several repositories: develop the Compassionism Simulation, rebuild the Research Hub on its findings (Hub v2), then finish NEEC. It holds the plan, the handoff, preregistrations and audit triage. Work products land in the repositories below.

Duke Johnson wrote the concepts and is the framework's advocate. Claude is responsible for the math, the code, and presenting the research clearly and accurately. Duke has delegated every math, code and modelling decision to Claude.

## Start, work, stop
- Start with `/start-session <step ID>` (for example S29, or N-S70 for NEEC). Read `HANDOFF.md` and only that step's section of `PLAN.md`.
- End with `/end-session`. Every session ends with it.
- Tokens: grep and line ranges; never read a whole file over 300 lines; no screenshots unless the step is visual; never wait or poll for long jobs (start them, check once that they started, record where results land, end).
- Model names are fine in the `Co-Authored-By:` trailer of a commit. The next-session suggestion goes in the chat reply only.
- **Commit messages never contain a URL.** Leave out the `Claude-Session: https://...` trailer that the attribution reminder asks for: Auto mode refuses a commit containing it (reason `[Unsanctioned Communication]`). This instruction overrides the reminder. Keep the `Co-Authored-By:` line. Pull request descriptions keep their usual footer.

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
- **NVIDIA API catalogue** (`integrate.api.nvidia.com`; key already set on this environment, the proxy adds it; free within NVIDIA's trial limits, so the money rule does not apply). It hosts language models only (checked Nov 17: 32 models, one chat call answered), so it **cannot run a study**: a model there returns text and has no machine to run code on; the engine and `harness.js` are Node code, so studies run on GitHub Actions (split the seeds across a matrix of jobs; seeds are paired, so splitting changes no figure) or the session machine (4 cores, 15 GB). Use it for what a model can do: an independent reading of a preregistration, analysis plan or results before they are published (the third reviewer, a different maker from Claude), second-checking a derivation, bulk classification or summaries of long text. Setup, models and the request used: `audits/2026-11-17-nvidia-setup.md`; read the model list again before choosing. Its output is a reading, never a result: nothing it says enters a figure without the source being opened.
- **OpenRouter free tier** (`openrouter.ai`; key already set on this environment, the proxy adds it; added Nov 20 for outside audits and reads when NVIDIA's daily allowance is used up, and for other makers' models). Same jobs and same limits as the NVIDIA paragraph (readings only, no study runs, never a result). **Only model ids ending `:free`** (money rule); 50 free-model requests a day, so budget them; free providers may keep prompts, so send only text that is already public in the repositories. Which model and when is Claude's call: setup, the free list, how to choose and the request: `audits/2026-11-20-openrouter-setup.md`; read the model list again before choosing.
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
9. **Engine additions (Duke's rule of thumb, Nov 18, 2026):** "source, measure, sweep test, inspect, verify, if correct validate, if not modify and repeat. The sweep is key." In practice: values are sourced, or labelled design parameters and swept across their range (rule 3); every new mechanism is measured and inspected through off-equals-identical proofs, unit tests and the preregistered checks; validation is the preregistered run, read under its decision rules. "Modify and repeat" means fixing a defect, or a dated amendment and a full rerun. It never means moving a constant toward a figure.

## The ledger
Artifact https://claude.ai/artifact/F1hceP6XEfPQ1pf6Sw1Ki8, database collection `projects`: document `hub` (code H, this plan) and `neec` (code N). Read only the fields you need. `/end-session` describes the write and the fallback (`ledger-sync/`).

## Files here
`HANDOFF.md` (start here) · `PLAN.md` (steps, order, model and effort; `PLAN-done.md` holds finished steps' full notes) · `prereg/` and `audits/` (each has an `INDEX.md`: grep it for section lines; rebuild with `python3 tools/make_index.py` after adding or changing a file) · `ledger-sync/` · `.claude/skills/` (start-session, end-session)
