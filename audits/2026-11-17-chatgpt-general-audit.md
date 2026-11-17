# ChatGPT, general audit of the Simulation (v5.9.9), Nov 17, 2026

Pasted by Duke at the start of the S13 part 2 session as "the reply from the general audit from GPT". Like Grok's general audit (`audits/2026-11-17-grok-general-audit.md`), it answers a general request, not the prompt in `audits/2026-11-17-release-audit-prompt.md`. Saved word for word below the line, including the citation chips the chat interface left in the text (favicon image links, "raw.githubusercontent.com+1" and `&#x20;` entities). Triaged in `audits/2026-11-release-review-triage.md`.

---

# **Compassionism Simulation V5.9.9 — Technical Audit**

**Audit scope:** Model clarity, economic and mathematical rigor, causal structure, implementation integrity, reproducibility, statistical treatment, documentation, and presentation of results.

**Primary sources:** [GitHub repository](https://github.com/BetterToBest/compassionism-simulation?utm_source=chatgpt.com), [live simulation](https://bettertobest.github.io/compassionism-simulation/?utm_source=chatgpt.com), [Replication Framework](https://bettertobest.github.io/compassionism-simulation/replication.html?utm_source=chatgpt.com), and the current model and testbed specifications.

## **1. Important distinction: what V5.9.9 actually changes**

The November 17, 2026 release notes identify V5.9.9 as a reporting and visualization update, not a new simulation-engine release.

Its principal correction is to the statistical treatment of the 18 simulated adults representing very wealthy families. The visual suite previously counted each simulated adult equally, rather than applying the population weights. The corrected release adds weighted averages alongside the existing unweighted series. The underlying simulation and stored figures are unchanged.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



Consequently, this audit separates three things:

1. V5.9.9's new reporting and weighting implementation.
2. The V5.9 simulation engine, including its substantial additions.
3. The research infrastructure supporting the findings and their interpretation.

I also distinguish genuine defects from explicitly disclosed modeling assumptions. An assumption can be debatable without being a coding error.



Confirmed release identity

&#x20;The source code identifies itself as V5.9.9, and the current replication framework carries the same version. Some older documentation and previously indexed pages have not caught up.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+2



## **2. Overall assessment**

The most important issues are not a demonstrated failure in the V5.9.9 reporting patch. They are the limits on what the weighted results represent, the sensitivity of the main results to calibration and backing assumptions, and a research-documentation package that no longer reliably describes the current engine.

My assessment:

| Area                               | Assessment                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| V5.9.9 reporting change            | Internally checked; no engine change                                                                          |
| Population weighting               | Material improvement, but not consistently applied to every headline metric or behavioral mechanism           |
| Economic calibration               | Consequential; results depend on the revised spending parameter                                               |
| Funding assumptions                | Full backing is an imposed scenario, not an independently established outcome                                 |
| Household and demographic modeling | Substantial additions exist, but not all are active in the primary configuration                              |
| Reproducibility                    | Significant documentation and configuration-management weaknesses                                             |
| Statistical inference              | Good separation of paired seeds, but parameter uncertainty and some lower-seed studies need clearer treatment |
| External validation                | Still needs independent economic review                                                                       |

## **3. Findings requiring attention**

### **P1 — The research documentation no longer provides a reliable description of the current release**

This is the clearest release-management problem.

The current files have become inconsistent in ways that affect how a researcher would interpret and reproduce the model:

- `ODD.md` still identifies itself with the v5.2 engine.
- `TESTBED_SPEC.md` contains an earlier main-design description in which the Source pays for the program without backing (`a=0`). That conflicts with the v5.9 primary full-backing design.
- `MODEL_SPEC.md` has newer material covering S72 and S73, but its section organization still describes a narrower S55–S71 range and does not adequately document S74 and S75.
- `REPRODUCE.md` still contains instructions and fingerprints associated with older releases. The current data architecture includes separate release data, round-two study shards, and separate studies.
- `CITATION.cff` contains an old v5.2.2 description and says every figure averages 500 paired runs, despite some current studies using 100.

These are not merely cosmetic version-number errors. Someone following the published specifications could configure or describe a different experiment from the one that produced the current results.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+6



**Recommended correction**

Treat the specifications as release artifacts, not continuously evolving historical notes.

For V5.9.10, I recommend:

1. Update `MODEL_SPEC.md`, `TESTBED_SPEC.md`, `ODD.md`, `REPRODUCE.md`, and `CITATION.cff` together.
2. Add explicit sections for S74 and S75, including their configuration, sample sizes, outcomes, and limitations.
3. Identify the exact primary configuration and distinguish it from optional sensitivities.
4. Generate version, commit, sample-size, and data-file metadata from a single release manifest.
5. Add a CI check that fails when the release version, model specification, testbed configuration, and manifest disagree.

The documentation should make it possible to answer one question without searching several reports: **What exact model, parameters, data, and seed count produced this result?**

### **P1 — Full backing is an assumption, not a demonstrated economic result**

The current main design uses the full-backing interpretation: each Source payout is matched by new output.

That is a legitimate scenario to model. It is not, however, evidence that the proposed conversion and reward mechanisms will generate enough additional production to back the payouts in practice.

The current documentation recognizes that the amount of new output generated by conversion rewards is a key unresolved question. The main full-backing configuration effectively chooses the favorable answer to that question as a model condition.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



This distinction matters because the simulation's outcomes are conditional on the funding architecture.

A model can show:

- What happens when every payout is fully backed.
- What happens when backing is partial.
- What happens when payouts are not backed.
- How much additional production would be required to support a given result.

It cannot establish the backing assumption simply by demonstrating favorable outcomes under that assumption.

**Recommended correction**

Make backing an explicit experimental dimension, preferably with several levels rather than only a binary switch. For example:

| Scenario        | Share of payouts matched by additional output |
| --------------- | --------------------------------------------- |
| Unbacked        | 0%                                            |
| Low backing     | 25%                                           |
| Partial backing | 50%                                           |
| High backing    | 75%                                           |
| Full backing    | 100%                                          |

These should be examined across the Reference, Adverse, and Stress environments.

Also report the minimum backing level at which each major outcome changes direction or crosses a policy threshold.

The government-finance accounting module is useful as a separate financing investigation, but it should not be presented as though it closes the funding question for the Source-based main design. The model's government-accounting work is an additional accounting and financing framework, not proof that the Source itself is funded.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



### **P1 — The spending calibration change materially affects the conclusions**

The current frozen main study uses `SPEND_FROZEN = 0.877`.

This replaced the earlier value of 0.593. The change arose because the original calibration did not reproduce the intended baseline saving rate when applied to the frozen no-program baseline. The revised calibration was selected to reproduce the cited 5.4% U.S. saving-rate benchmark; the wage-only alternative was approximately 0.862.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com



This is important because the parameter is not simply a cosmetic fit.

The model documentation reports that applying the old 0.593 value to the frozen no-program baseline produces a 19.5% saving rate. It also reports that the direction of some wealth-poverty findings changes under that calibration.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com



That means comparisons across versions can be misleading if the reader assumes that changes in results arise only from newly added model features.

**Recommended correction**

Publish a prominent calibration table for every principal result:

| Parameter             | Main value | Alternative |
| --------------------- | ---------- | ----------- |
| `SPEND_FROZEN`        | 0.877      | 0.593       |
| Wage-only calibration | —          | 0.862       |

For the main outcomes, show the results under all three values, including the no-program baseline.

I would also distinguish two questions in the reporting:

- How well does the model reproduce the selected reference saving rate?
- How sensitive are the policy conclusions to reasonable alternative spending calibrations?

Matching one aggregate benchmark is calibration, not validation of the model's full spending behavior.

### **P1 — A configuration omission has already produced materially different results in auxiliary studies**

The S74 central-bank and S75 deep-history studies initially omitted global configuration settings, including `applyNR6` and `TB_PROFILE_G`.

The resulting central-bank run produced substantially different wealth results from the v5.9 baseline. The studies were corrected and rerun. The corrected no-intervention arms reproduce the v5.9 baseline across the reported series and environments.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



This is a resolved error in those reported studies, not evidence that the current main release is still running with the wrong settings.

It does reveal a systemic reproducibility vulnerability: separate study runners can silently omit global defaults.

**Recommended correction**

Create one shared configuration constructor used by:

- The browser simulation.
- The batch runner.
- Every auxiliary study runner.
- The test harness.
- Replication and export scripts.

Each run should write its complete effective configuration to its output, including defaults that were not explicitly overridden.

Before an intervention study starts, its no-intervention arm should be required to match the designated baseline fingerprint. The run should abort if it does not.

I would make that a mandatory automated test rather than a manual research check.

## **4. Statistical and measurement findings**

### **P1/P2 — The wealth-tail correction is necessary, but weighted reporting is not yet consistent**

The V5.9.9 change addresses a serious measurement problem.

The model represents the wealthiest population segments using 18 synthetic adults with population weights. In the earlier reporting, each synthetic adult was counted once. That made the unweighted savings-day average extraordinarily high.

The S81 correction adds population-weighted averages while preserving the existing unweighted measures. The report states that the original plain engine values and earlier plain output values match exactly.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



The scale of the correction is substantial. In one Year 40 Reference comparison, the no-program average savings-day figure changes from approximately 565,170 unweighted to 8,173 weighted, with a weighted median of approximately 1,467. The full-coverage and opt-in cases show the same broad pattern.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



This is not a small adjustment. It changes the interpretation of the measure.

There are two remaining issues.

**First: one important outcome remains unweighted.**

The share below 30 days (`pbO`) is still reported unweighted. The S81 report says the weighted and unweighted values can differ by as much as 0.61 percentage points.

That difference is not necessarily large enough to change the conclusions, but leaving it unweighted alongside population-weighted measures makes the reporting inconsistent.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com



**Second: population weights do not make the entire simulation population-weighted.**

The source code uses weights for distributional measures and selected accounting calculations, but the weights do not generally enter behavioral rules, prices, or production mechanisms. The specification itself describes these limitations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



That means the results are best understood as a weighted representation of selected outcomes from an agent-based model, not as a fully population-weighted economy in which every agent's economic influence is represented proportionally.

**Recommended correction**

Adopt a formal metric classification:

| Metric class        | Meaning                                                    | Reporting                           |
| ------------------- | ---------------------------------------------------------- | ----------------------------------- |
| Agent-weighted      | Each simulated agent counts once                           | Label as unweighted                 |
| Population-weighted | Each agent represents its assigned population              | Use for population estimates        |
| Accounting-weighted | Weights enter designated aggregate accounting calculations | Explain which accounts are weighted |

For every major distributional result, show weighted and unweighted values together, including `pbO`.

Also add automated tests for:

- Weight totals within each represented population group.
- Weighted means and quantiles.
- Zero-weight and extreme-weight handling.
- Effective sample size.
- The maximum share of the total weight held by any single simulated agent.

I would also change comments that broadly say weights do not enter any rules. The intended distinction is more specific: weights affect designated measurement and accounting paths but generally do not change the behavioral rules or price formation.

### **P2 — The wealth-tail calibration needs uncertainty beyond the current point estimate**

The tail representation is fitted using Survey of Consumer Finances wealth data, with a Pareto fit beginning at the 97.5th percentile. The reported exponent is approximately 1.4901, with a standard error of approximately 0.136.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



The fitted distribution improves the representation of upper-tail wealth compared with the earlier model. But fitting a model to the same survey distribution used to construct it is calibration, not an independent validation.

The reported results also show sensitivity of the top 1% wealth-share effects to debt-relief assumptions. Under the main debt-relief reading, the model shows a decline in the top 1% share; under the no-debt-relief reading, the direction can reverse.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

raw\.githubusercontent.com+1



**Recommended correction**

Propagate uncertainty in the tail assumptions into the reported outcomes.

Specifically:

- Bootstrap the SCF observations used for the tail fit.
- Re-estimate the Pareto exponent and threshold for each bootstrap sample.
- Recalculate population weights and weighted outcome distributions.
- Report sensitivity to the 97.5th-percentile threshold and alternative fits.
- Include this uncertainty alongside the variation across simulation seeds.

The current seed intervals describe stochastic simulation variation. They should not be presented as encompassing uncertainty in the underlying wealth distribution.

## **5. Household, child, and demographic additions**

### **P2 — The primary long-horizon configuration still uses a largely static demographic structure**

The newer engine does include household, child, birth, death, and age-transition functionality. This is a substantial addition and should be documented as such.

However, the primary study configuration does not activate the full lifecycle implementation. The main labor-flow reading uses a stock-style approach that maintains labor-force shares where ages do not change. Ageing and replacement are alternative settings rather than part of the primary main row.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub+2



The optional age implementation includes births, ageing, deaths, children aging out of dependency, and estate transfers. It does not currently model all household transitions, including new partnerships and separations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub+1



This distinction matters particularly for 20- and 40-year simulations.

A 40-year run with household membership and demographic composition largely held static is not equivalent to a 40-year lifecycle model. It can still be useful for policy comparison, but its conclusions should be described accordingly.

**Recommended correction**

Promote the lifecycle model to a major sensitivity, with side-by-side results for:

1. The current stock-style primary configuration.
2. Full ageing, birth, death, and child-transition settings.
3. A household-transition extension incorporating partnership formation and separation, once implemented.

Compare changes in:

- Household size and composition.
- Dependency ratios.
- Per-adult and per-household poverty.
- Child-to-adult resource allocation.
- Wealth inheritance and intergenerational distribution.
- Labor-force participation and retirement.

For now, explicitly label the main 20- and 40-year estimates as results under the fixed-composition or stock-style demographic configuration.

## **6. Economic measurement and internal consistency**

### **P2 — BLEI is a composite capacity measure, not literal days of liquid savings**

The Basic Living Economic Index combines a share of wealth, monthly wages, and basic-unit food support, then divides by a daily cost measure. The wage contribution uses different coefficients for participants and nonparticipants.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



That can be a useful measure of estimated economic capacity, but its interpretation needs care.

It combines:

- A capital stock.
- An income flow.
- A designated basic-unit benefit.
- A modeled daily-cost denominator.

Consequently, BLEI days are not equivalent to days that a household could literally survive using cash or immediately accessible liquid assets.

This is especially important when BLEI is used to classify households as secure, to measure poverty, or to determine eligibility for other mechanisms.

**Recommended correction**

Keep BLEI, but accompany it with separate measures for:

- Liquid savings in days of essential expenses.
- Net wealth.
- Monthly disposable income.
- Basic-unit support.
- Actual essential-basket affordability.

Rename or label the existing index as a **days-equivalent economic capacity measure**, rather than allowing the label to imply cash-on-hand.

A useful reporting display would show both the BLEI classification and the separate underlying components.

### **P2 — PTH's 25% housing-saving allocation does not equal 25% of actual housing savings**

The current PTH calculation derives the housing-saving basis from the BLEI daily-cost measure rather than directly using the actual housing-basket saving.

The model documentation reports that this makes the resulting amount approximately 12.6% of the actual PTH saving, despite the nominal 25% designation. The behavior is disclosed in the specification, but the terminology can mislead readers about the size of the allocation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub+1



**Recommended correction**

Choose one of two paths:

- Calculate the 25% allocation from actual housing-basket savings, if 25% of actual savings is the policy intention.
- Retain the current calculation but rename it to make clear that it is 25% of the BLEI-estimated housing saving.

I recommend reporting both figures during the transition so that the consequences of changing the basis are visible.

### **P2 — The creditor-side debt analysis needs an especially clear boundary around unmodeled creditors**

The S71 creditor-side analysis allocates household debt across different creditor groups. Its reported allocation places substantial shares with businesses, government, and foreign holders, as well as households outside the modeled population. The report estimates that approximately 66 cents per dollar of debt losses fall outside the modeled people under its principal allocation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



This is useful because it prevents the model from treating all debt relief as a transfer between the same modeled households.

However, the treatment remains dependent on the creditor allocation assumptions. It is not a complete model of the financial system or of the balance sheets of every creditor sector.

**Recommended correction**

For debt-related conclusions, show:

- The creditor allocation used.
- The fraction of gains and losses inside the modeled population.
- The fraction external to the modeled population.
- Sensitivity to alternative creditor allocations.

Avoid describing the resulting wealth-distribution effect as a complete accounting of the economy-wide incidence of debt relief.

## **7. Auxiliary studies: interpretation and sample-size limitations**

### **P2 — The central-bank study does not yet test the full monetary-policy mechanism**

The central-bank module adds a stylized Taylor-rule policy-rate response and bond purchases at the zero lower bound. It affects modeled deposit and loan rates, refinancing, share and home prices, job loss, and forced sales.

But the study uses 100 paired seeds rather than the 500 used in the main study, and its policy rule does not affect essential-basket prices. The documentation also correctly distinguishes this from an implementation of the Federal Reserve itself.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub+1



The result should therefore be framed as a test of a particular interest-rate and asset-price channel, not as a complete test of monetary policy's distributional effects.

**Recommended correction**

Keep the existing study, but state its scope prominently. A future extension should include an essential-price channel if the research question concerns how monetary policy interacts with the cost of basic needs.

### **P2 — The deep-history study is a historical-settings experiment, not a historical reconstruction**

The S75 experiment applies earlier U.S. economic-era settings to a present-day, 2022-based modeled population. The report explicitly says that it is not a reconstruction of the actual households that lived in those historical periods.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



The correction of the missing global settings also changed some of the earlier findings. In particular, the corrected full-coverage results show a longer income-shock recovery period under the 1973–83 setting, reversing the prior directional result in the six relevant arms. The report describes 12 directional reversals across the examined outcomes, while the opt-in effect retained its direction in all 120 comparisons.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



The study also discloses limitations involving the lack of an expectations channel, tax treatment of capital income, extrapolation beyond the historical estimation range, and its relatively limited era sample.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



**Recommended correction**

Call the study a *historical-policy-environment sensitivity experiment* or equivalent, not a historical backtest.

For the next version:

- Include the exact number of seeds next to every historical result.
- Show confidence intervals and directional consistency by outcome and arm.
- Preserve the prior and corrected results in the research archive.
- Explain why the corrected configuration changes the conclusion.
- Separate statements about the modeled mechanism from claims about what actually happened historically.

## **8. Technical improvements for the next release**

I would prioritize the following engineering changes.

| Priority | Improvement                             | Acceptance test                                                                                            |
| -------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| P1       | Single shared configuration constructor | All browser, batch, and study runners emit identical defaults and configuration hashes                     |
| P1       | Baseline fingerprint gate               | Every intervention study reproduces its designated no-intervention arm before proceeding                   |
| P1       | Machine-readable release manifest       | Version, commit, parameters, seed counts, input hashes, and output files are recorded for every run        |
| P1       | Documentation consistency CI            | Release files fail validation if version or configuration descriptions disagree                            |
| P1       | Explicit metric-weighting contract      | Every reported metric identifies whether it is unweighted, population-weighted, or accounting-weighted     |
| P2       | Bootstrap parameter uncertainty         | Tail-fit uncertainty and other calibrated-parameter uncertainty are shown separately from seed uncertainty |
| P2       | Lifecycle comparison                    | Primary stock configuration and age-transition alternative are reported side by side                       |
| P2       | BLEI component reporting                | Readers can inspect liquid savings, income, wealth, and support independently                              |
| P2       | External independent review             | A reviewer can reproduce the equations and inspect the assumptions without relying on project summaries    |

Two additional engineering changes would be particularly useful:

**First, strengthen the test harness around configuration and output identity.** The repository already describes accounting identities, finite-value checks, reproducibility controls, and run-order tests. Extend those checks to the configuration layer and all auxiliary studies rather than relying on each runner to implement them independently.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub



**Second, broaden independent implementation checks.** The specification describes a second implementation for an earlier frozen model. That kind of independent parity check is valuable, but should eventually cover the newer household, lifecycle, wealth-tail, and financing modules as well. The documentation still identifies independent economic review as outstanding.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://raw.githubusercontent.com\&sz=32)

GitHub+1



## **9. What I would put in V5.9.10**

I would not recommend reopening the entire simulation or changing the engine simply to address the V5.9.9 reporting correction.

The most defensible next release would be a targeted research-integrity release:

**Required**

1. Bring all specifications and reproduction instructions into alignment with the current v5.9 engine and S74/S75 studies.
2. Add shared configuration generation and baseline fingerprint checks.
3. Add weighted `pbO` reporting and explicit metric-weighting labels.
4. Make the full-backing assumption and `SPEND_FROZEN = 0.877` unmistakable in the primary results.
5. Correct the sample-size descriptions in the metadata and reports.

**High-value follow-up**\
6\. Bootstrap wealth-tail parameter uncertainty.\
7\. Report lifecycle and stock-style results side by side.\
8\. Clarify the BLEI and PTH measurement terminology.\
9\. Prepare the newer engine for independent replication and external economic review.

## **10. Final verdict**

The V5.9.9 correction is appropriately scoped: it changes reporting, adds weighted measures, and preserves the prior unweighted engine outputs. The correction exposes a real problem in the earlier savings-day averages, but it does not turn the engine into a fully population-weighted economic model.

The more consequential research issue is that the current headline conclusions depend on specific conditions: the revised spending calibration, the chosen backing interpretation, and the primary demographic configuration. Those conditions need to remain visible wherever the results are presented.

The most serious technical weakness is configuration reproducibility across separate study runners. The S74 and S75 corrections show that this is not hypothetical. The documentation inconsistencies make that weakness harder for an outside researcher to detect.

**My recommendation:** Preserve the current v5.9 results as a documented release, do not silently overwrite earlier findings, and make V5.9.10 a configuration, specification, and reporting-integrity release before adding more economic mechanisms.

*Verification limitation:* This is a source-code, specification, and project-report audit. I did not independently execute the Node test suite, browser harness, or 500-seed simulation batches. Where I describe exact replication or parity, I am reporting what the repository's own test reports claim, not asserting that I independently reproduced those results.

A useful next deliverable would be a V5.9.10 issue list with file-level changes, severity, and explicit acceptance tests for each correction.
