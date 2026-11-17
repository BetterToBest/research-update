# Handoff (Nov 17, 2026): S84, one start for every study runner (v5.9.13), and its v5.9.14 follow-up

## Step status
**S84 done.** No engine change and no stored figure changed (guard test: every figure identical, 25 rows x 20 seeds x 483 outputs, three environments).

## What shipped
- compassionism-simulation PR 148 (`claude/s84-one-start`), **merged** as `3c88e9b`, v5.9.13 (CI green: checks and guard; local validate, unit, domtest 162 of 162):
  - `startRelease()` in `harness.js`: applies the release's two global settings once. All 43 tools use it (`dev/tools/start_test.js` fails if one calls `applyNR6` itself).
  - Every output has `_settings`: version, the engine's 28 constants, profiles, labour response, PTF and pathway switches, price defaults, frozen spending share, CFG scalars and SHA-256, Node version, baseline result. The guard and SNAP-rule reference files are untouched.
  - Baseline check: `data/baseline.json` (published no-programme rows, seeds 1-20, three environments, from `dev/tools/make_baseline.js`). `startRelease({baseline: true})` stops a run whose no-programme arm differs per seed. On in the S74 pilot, S74 sweep and S75 era runner. Fails without the start and with one constant moved.
  - New CI: `start_test.js`, `check_docs_agree.js`, `weight_tests.js` (main row: effective sample size 472.6 of 500, largest weight 3.47 = 0.69%).
  - Decisions in `dev/DECISIONS.md` ("S84"); notes in CONTRIBUTING.md (v5.9.12 notes moved to CHANGELOG.md).
- compassionism-simulation PR 149 (`claude/s84b-weights-stated`), **merged** as `dcad38f`, v5.9.14 (CI green; local unit 384, domtest 162/162, guard identical; no engine change), Duke's follow-up:
  - The weight spread is stated where weights are used: model card, MODEL_SPEC 14.8, ODD, and the findings page (read from `data/manifest.json` `docs.weights`; also `_settings.weights` in every run). 18 tail adults: 13 below 0.1, 4 above 2 (largest 3.47), one about 1; the other 482 at 0.99-1.13; effective sample size 472.6 of 500; largest weight 0.69%. The set of weights is the same in every seed and environment; which adults carry them depends on the seed. `check_docs_agree.js` and `weight_tests.js` check this.
  - The model card (and ODD, MODEL_SPEC, TESTBED_SPEC, REPRODUCE, CITATION, the manifest's v5.9 summary, the findings page's central-bank note) now says the OSF registration is the frozen model **without a central bank**, first published as v5.8 (Nov 15); v5.9 (Nov 16) added the central-bank switch and study, preregistered separately.
- research-update: PLAN.md (S84 note, Order row 25c), CLAUDE.md (NVIDIA API catalogue note: free, model readings only, cannot run studies), this file.

## In flight
- None.

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change). D31 confirmed. S12 unchanged.

## Next step
**S82** (opus, preregister first): the v6 engine. It waits on nothing. S85 follows S82. S13 part 3 starts when Grok's reply arrives.

## Pitfalls
- An explanation given in this session said the tail adults carry larger weights; wrong (most carry far less than 1). Corrected in the simulation's `dev/DECISIONS.md` ("S84 follow-up"). Check a claim about the weights against `weightSummary()` before repeating it.
- ECONOMIST-REVIEW.md and README name no registration and were left alone; earlier release notes still say "v5.9" for the frozen model (history).
- The baseline check tests the start (the frozen no-programme arm), not each study's own arm; a study that changes its baseline on purpose still passes. Studies in the results repository's runner (`runner/jobs/r2.js`) do not use `startRelease` yet: S82's runner should (`startRelease({baseline: true})`).
- Scripts that loop over every key of a run file must skip `_settings` as they skip `_meta`.
- The first domtest run failed: CONTRIBUTING.md is reader-checked, so release notes may not name steps (S74, S75).
- `register_repo_root` gave no system reminder; the simulation's CLAUDE.md was read directly. Simulation commits carry no model name (its CLAUDE.md); research-update commits may.
- NVIDIA API: hosted models return text only. It cannot run studies; do not plan on it for them.
- A zero-weight adult can move a weighted quantile by about 0.05% (never a total or share); the engine has none.
