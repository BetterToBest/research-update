# The results repository disabled by GitHub (Nov 26-27, 2026): cause, what survives, and the plan

## What happened
On or before Nov 26, GitHub disabled `BetterToBest/compassionism-sim-results` for a terms-of-service matter and gave no reason. The API returns `403 Repository access blocked`. Duke opened a ticket. On Nov 27 Duke checked the public archives (Software Heritage, the Wayback Machine) and found no copy.

## The likely cause (an inference; GitHub has not said)
The repository existed mainly to run the study batches on GitHub-hosted Actions runners: about 650 runner-hours for round 1 on 20 runners at once, then round 2 (about 186 runner-hours) and every later study. All results were committed back into git, including folders over a gigabyte. GitHub's *Terms for Additional Products and Features* (Actions section) forbid, on GitHub-hosted runners, "any other activity unrelated to the production, testing, deployment, or publication of the software project associated with the repository", and "any activity that places a burden on our servers, where that burden is disproportionate to the benefits provided to users". They say misuse may lead to the "disabling of repositories created to run Actions in a way that violates these Terms".

The risk was written down at S47 (ledger I16: "check whether running studies there is accepted"). The plan ran the batches there because they were free, and the check was never settled. That was the plan's error, not Duke's.

## What survives (other repositories)
- The engine at every commit, its tests, `harness.js`, the study tools in `dev/tools/`, every report (`dev/reports/`), the published tables (`dev/runs/`), and the release data the pages read (`data/releases/`, `data/studies/`). All of these are in compassionism-simulation.
- Every preregistration and amendment, every audit and triage, and the plan (this repository).
- The Hub, the root site, and NEEC's records and adjudication.
- Every published figure. None is wrong because of this.

## What is inside the disabled repository
- The per-seed result folders (`<study>-<commit>/`, with `run.txt` and `SHA256SUMS`).
- The job scripts (`runner/jobs/*.js`), the `run-study` workflow, the BeforeIT module, and the round-2 tables folders.
- NEEC's outside-review result files. Those were model readings, so a rerun will not reproduce them exactly. NEEC's adjudication, which records what they said, is in NormativeEvaluation.

The studies are deterministic: the same engine commit, job and seeds give identical outputs (the central-bank study's rerun reproduced all 542,000 pilot values). Every folder can be rebuilt once its job script is rebuilt.

## Standing rules from today
1. **No study, batch or analysis computing on GitHub Actions, in any repository.** Actions runs only a repository's own checks, builds, releases and deploys. This protects the whole account and the Hub's hosting with it. Workflow check on Nov 27: every remaining workflow is of that kind (compassionism-simulation `checks`, `release`, `apply-upload`; NormativeEvaluation `harness`, `land-session`; research-update `links`; research-hub `apply-update`; portal's issue, label, test and Pages checks). None needs to change.
2. **Studies run on RunPod** (paid) **or the session machine** (free; small runs). Before every paid batch, a ledger decision gives its estimated cost. Nothing paid runs until Duke has answered.
3. **Results data are not stored in git.** Each published results folder is deposited in a research data archive (Zenodo by default, D39) with a DOI. Git keeps a manifest: folder, engine commit, job, seeds, SHA-256 of each file, and the DOI.
4. **Every repository has a second home**, a mirror on another host (Codeberg by default, D41).

## Steps (ledger H)
- **S104** (done Nov 27): rules written into CLAUDE.md, PLAN.md and HANDOFF.md; workflow check above.
- **S105** (Duke): send the GitHub ticket below.
- **S106**: the results home. Zenodo (or D39's answer) set up by Duke; the deposit tool and manifest built by Claude.
- **S107**: the RunPod runner. A script that starts a CPU pod, runs a job shard by shard, checks every shard, deposits the folder, and stops the pod. Costed per batch.
- **S108**: rebuild the job scripts S103 part 2 needs from the preregistrations, the reports and the tools in compassionism-simulation, each checked against the published tables on a seed sample before any batch runs. They go to compassionism-simulation `runner/jobs/`, with no workflow.
- **S109**: mirror every repository (Duke creates the account; Claude writes the steps).
- **S110**: published pages and reports that link the disabled repository get a dated note (offline; reproducible from the named engine commit; the data deposit to follow).
- **S103 part 2** then runs on S107's runner from S108's scripts.

## Draft ticket text for Duke (S105)
> Subject: Request for read-only access or an export of BetterToBest/compassionism-sim-results
>
> Hello. GitHub disabled the repository BetterToBest/compassionism-sim-results for a terms-of-service matter. I believe the cause was my use of GitHub-hosted Actions runners to run large simulation batches for an open-access research project, and committing their outputs to the repository. I now understand that this falls outside the Actions terms. I have stopped all such use in every repository in the account, and future runs will use separate paid compute, with the data held in a research archive.
>
> I am not asking to run Actions in that repository again. I am asking for one of these: (a) the repository restored read-only, or archived, with Actions disabled, so I can download its contents once; or (b) an export of its contents (a git bundle or archive). The data back published, open-access research (CC BY 4.0) and its replication record. Once I have a copy I am happy for the repository to be deleted.
>
> Thank you for considering it.

## Duke's answers and the next moves (Nov 27, later)
- **D39:** Zenodo is the record (Duke's existing account, `AuthorDukeJohnson`); OSF holds a second copy. S106 builds the deposit tool for both.
- **D41:** GitLab, not Codeberg (Codeberg restricts AI-generated code). Group `BetterToBest-group`, ID 148851118. S109 mirrors every repository into it.
- **D40:** open. Duke is looking at other compute systems; S107 waits. Checked so far: RunPod has $4.03 prepaid (small runs only). Google AI Pro's cloud machine is Jules, a coding agent with daily task limits and a 20 GB VM, not batch compute; its Drive storage (2 TB or more) can hold a backup copy. Oracle Cloud Always Free is the best free candidate (2 Arm cores and 12 GB, about 1,400 core-hours a month; 4 cores and 24 GB reportedly on a pay-as-you-go account). Any platform's terms must allow long batch jobs, and the guard test must match exactly on its machine before any result from it is used. S107 builds the runner for any plain Linux VM, RunPod included.
- **Reachable from the session machine (Nov 27):** zenodo.org, gitlab.com, codeberg.org.
- **Recovery from old sessions (ledger I22).** Each Claude Code session has its own machine; a recent one may still hold its sparse clone of the results repository. The S93 sessions (Nov 21-26) checked out the release folders (about 6.5 GB); S103's never had a clone. Duke reopens them, newest first (then S92, S85, S82), and pastes the prompt below. Recovered data go to an unpublished Zenodo draft, never back to GitHub (re-hosting a disabled repository's contents there could look like evading the enforcement). S108 then checks anything recovered against the published tables and uses recovered job scripts in place of rebuilding them.

```
The repo compassionism-sim-results was disabled by GitHub. Do not try to fetch or push to it.
1. Check whether a clone of it exists on this machine (find / -maxdepth 4 -type d -name "compassionism-sim-results*" 2>/dev/null).
   If none, say so and stop.
2. If found: list the checked-out folders with sizes (du -sh), whether runner/ and runner/jobs/ are present,
   and `git -C <clone> log -1 --format='%H %cd'`.
3. For each folder: tar.gz it, write a SHA256SUMS of the archives, and upload them to a NEW Zenodo
   deposition as an unpublished draft (do not publish), title "compassionism-sim-results recovery, <date>".
   Zenodo token: <paste here>. Upload runner/ first, then the smallest folders, largest last.
4. Report the deposition id, the folders uploaded with their sizes, and anything that failed.
```

## Recovery result and a compute candidate (Nov 27, evening)
- Two S93 sessions still held sparse clones. 58 folders (56 tarballs, about 2.6 GiB compressed) are in Duke's unpublished Zenodo draft 24615619, with `SHA256SUMS` and `SHA256SUMS-20261128T043653Z.txt`. The job scripts were not recovered. Next: S106 part 1 (inventory and verify), then publish.
- Kaggle (account `bettertobestresearch`) is a compute candidate for D40: free CPU notebooks with 4 cores and 16 GB, batch runs of up to 12 hours, 20 GB of saved output. Duke phone-verifies the account (internet in notebooks needs it) and creates an API token, best kept in the Claude Code environment's variables (`KAGGLE_USERNAME`, `KAGGLE_KEY`). S107 then tests one shard there: the guard test must match exactly, and Kaggle's terms must allow the use. The session machine reaches kaggle.com (checked Nov 27).
