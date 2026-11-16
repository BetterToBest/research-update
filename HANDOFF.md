# Handoff (Nov 16, 2026): S76 done (release 2 leads both pages, with a central-bank switch; S74 corrected)

## Step status
**S76 is done**, widened by Duke (Nov 16): lead both simulation pages with release 2 (the fully backed main row) and a central bank on/off switch; release 2 above release 1 on the findings page; fix the release dropdown; fewer release options; fold the release notes; back-to-top buttons; a clarity edit. Released as v5.9.0.

## Found first: S74 left out the release's settings
S74's tools (`dev/tools/s74_pilot.js`, `s74_sweep.js`) and S75's `dev/tools/s75_eras.js` never called `applyNR6()` and `tbSetG(TB_PROFILE_G)`, which the round-2 runner (compassionism-sim-results `runner/jobs/r2.js`) sets before every run. So S74's "no central bank" arm was not release 2's main row: for C2.2 in Reference, median real wealth was $1,223,000 against release 2's $431,700. With the two settings, today's engine reproduces release 2 per seed.
- Preregistration Amendment 4 (`prereg/2026-11-s74-central-bank.md`) was committed before any rerun.
- The S74 tools are fixed and the 100-seed study was rerun (`s74-final-3beb5ff`). Its no-central-bank arm equals release 2 on 72 series, per seed.
- **No verdict changed** (P1-P5 and the interaction, all eight cells). Some magnitudes moved: for example, C2.2's cut in the largest wealth fall in Adverse went from −$40,800 to −$22,200. Three decision-rule-3 words changed. All are listed in the report's dated correction.
- Still to rerun (S77): S74's sweep and discount readings, and S75's engine readings, which feed the Hub's US policy eras page. That page now carries a "correction pending" notice.

## What shipped
- compassionism-simulation [PR 130](https://github.com/BetterToBest/compassionism-simulation/pull/130): S74 correction (the tool fix, `dev/runs/s74-corrected/`, the report's correction, `dev/tools/s76_cb_data.py`).
- compassionism-simulation PR 131 (v5.9.0, pages): see its notes in CONTRIBUTING.md. The simulation page opens on release 2 with three switches: Design, Central bank and Environment. Central bank off shows release 2 as frozen (500 seeds, `data/studies/r2-effects.json`); on shows S74 corrected (100 seeds, `data/studies/s74-cb.json`), with the change on the same seeds. Release 1 is relabelled, the limits are corrected and the S75 link is added. On the findings page, release 2 and a new central-bank section come first. The dropdown shows v5.9, v5.6 and v5.4; the others stay reachable by address. Each release shows only its own sections. Both pages have back to top (`site/totop.js`).
- compassionism-sim-results [PR 47](https://github.com/BetterToBest/compassionism-sim-results/pull/47) (merged): `s74-final-3beb5ff`.
- research-hub [PR 16](https://github.com/BetterToBest/research-hub/pull/16) (merged): the notice on `us-policy-eras.html`.
- research-update: Amendment 4, PLAN.md (S76 note, new step S77), this handoff.

## Checks
- Locally: `harness.js validate` passes; domtest is in the PR's checks; the page figures were rendered at 1200 px (light) and 390 px (dark and light) with no console errors and no horizontal scroll. Switching to v5.6 hides the release 2 sections.
- The page numbers are printed from the data files (snum spans), as on the round-2 section. The central-bank words in `site/cb.js` (directions: steadier at the bottom, prices less steady, wealth moved up and shrunk by the programme, forced sales, small rule-3 effects) were checked against the corrected tables.

## In flight
- See the PR states above. If PR 131's checks failed, it is open and says why.

## Decisions waiting
- None.

## Next step
1. **S77** (opus, high): rerun S74's sweep and discount readings and S75's engine readings with the release's settings, correct the S74 report body and the Hub's US policy eras page, then remove its notice. Attach compassionism-simulation, compassionism-sim-results and research-hub (push).
2. S24 (sonnet, medium) can run beside it.

## Pitfalls
- **Any study tool must call `H.applyNR6(); H.tbSetG(H.TB_PROFILE_G);` before its runs**, as `runner/jobs/r2.js` does. Without them the main row runs under older defaults and does not reproduce release 2. Check a new tool's "off" arm against `r2-m-*-20-104691f` on a few seeds before trusting it.
- `fsQ` is dollars sold per adult-year; the share of adult-years with a forced sale is `fsN`.
- The release dropdown keeps every release as an option (hidden and disabled, not removed): `dev/tools/check_figures.js` selects each release by value.
- github.com page links return 403 from this machine; use blob-less sparse clones of compassionism-sim-results.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
