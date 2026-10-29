# Preregistration: <study name>

Committed <date> by <step ID>, before any run. Engine: compassionism-simulation at commit `<full hash>` (release or branch).

## Questions
Q1 … (one sentence each; what would count as an answer)

## Design
- Rows (settings compared), each with its switches.
- Environments: Reference, Adverse, Stress (all three unless stated why not).
- Seeds: which, how many, paired across rows (common random numbers).
- Population size and horizon (years).
- Where it runs (GitHub Actions or Runpod), the exact command, the results folder in compassionism-sim-results.

## Outcomes
- Primary (fixed here; the headline can only come from these): …
- Secondary: …
- Every outcome's definition and unit, and the measure it is confirmed on (basket poverty and wealth poverty, not FGT2 alone).

## Analysis
- Estimates: paired differences against no program and between rows; intervals by paired bootstrap (state replicates).
- Synergy: Shapley shares and interaction contrasts; claimed only where the 95% interval excludes zero.
- Multiple comparisons: how they are handled (for example, Holm across primary outcomes).

## Decision rules
What result leads to what statement, written before the run.

## Reporting
Every cell above is published, including null and unfavourable results, in compassionism-sim-results and on the findings page.

## Amendments
Dated, with the reason, below this line. Nothing above changes after the first run.
