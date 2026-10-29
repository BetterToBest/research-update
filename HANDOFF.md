# Handoff (Oct 29, 2026): S30 where the early figures came from

Model check (chained session): ran on claude-opus-5-5, effort high. The chained task resumed the S23 session (same conversation and container) rather than opening a fresh one.

## Step status
S30 **done.** Every early headline figure has a provenance line in `audits/early-figures.md`: none was produced by any code found. Next: **S46** (S31 waits on the chat exports, D2).

## What shipped
- research-update PR (this branch; link and merge commit in the ledger log): `audits/early-figures.md` (plain-words report and tables); `audits/early/`: `first_dates.py` + `first-dates.md`, `run_printed_code.py` + `printed-code.md`, `run_engines.js` + `engines.txt` + `runs/*.jsonl` (3,800 runs), `summarize_runs.py` + `engine-results.md`/`.json`.
- Findings: every early figure was on the Hub by Sep 18, 2025; the first engine is May 21, 2026. The printed code is a skeleton that fails as printed; its runnable blocks return typed-in constants (92% stable) or other numbers (carbon 20%, not 45%). The promised Python repository never existed. Early engines used the Hub figures as targets ($82K, Gini 0.28), had a random "stability" metric, and cut the no-program run's wealth by 0.85.
- One figure reappears only with an error: engines v4.0-v4.2 (Aug 2026) give $81K-$83K median wealth while adding model-unit wages to dollar wealth (fixed v4.3: about $484K). The BLEI paper's v4.4 Gini 0.518 reproduces on 100 seeds (no-program 0.858).
- research-hub PR `claude/s30-claims-provenance`: the claims-ledger notes now carry these findings (classes unchanged). No Hub page or engine changed.

## In flight
Nothing.

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped until Duke creates BetterToBest/research-provenance and uploads them.

## Next step
S46 (repair the formal model), opus, xhigh. S31 is blocked on D2.

## Pitfalls
- The current simulation page (v5.6.0) still holds the Hub figures as targets (`CFG.TARGET_WEALTH` 82000, `TARGET_GINI` 0.25, `TARGET_POVERTY` 0.05, `TARGET_STABILITY` 0.90) and prints "Target $82K". Rule 3: remove them (S40 or the next engine release).
- Early pages run seed 42 by themselves on load; `run_engines.js` waits for that run, blanks the tiles, then runs the requested seed. Check any reuse against the CHANGELOG seed-42 figures (v4.19: 16.6%, $559K, 0.534).
- Engines before v3.3 cannot be seeded; the runner seeds `Math.random`. Their "seeds" are reproducible but are not the page's own.
- `f46d5fa` (May 23) is a truncated upload and cannot run.
- The auto-mode guard refused a force-push; restarting the branch needed a fast-forward from main instead (the branch tip was already in main).
