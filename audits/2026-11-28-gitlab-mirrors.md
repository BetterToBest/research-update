# GitLab mirrors of the BetterToBest repositories (S109, D41)

Written Nov 28, 2026. Group: `BetterToBest-group` (ID 148851118). Status: **guide written; no mirror created yet** (no GitLab token on this environment; the group is not visible without one).

## Repositories to mirror
Public: research-update, research-hub, compassionism-simulation, bettertobest.github.io, x-cents, NormativeEvaluation, portal, compassionate-meritocracy-plan.
Private (mirror only if Duke wants a private copy; needs a GitHub token): research-provenance, btb-bluesky-poster.
Not mirrored: compassionism-sim-results (disabled by GitHub; results are in the deposit).

## Important: the free tier has no pull mirror
As far as I know, GitLab.com offers pull mirroring only on Premium and Ultimate; Free projects get push mirrors (GitLab out to elsewhere) and one-time imports. Check this in step 3 below: if the "Mirror repository" box is missing or greyed, use option B.

## Option A: pull mirror (needs Premium, or a trial)
Repeat for each repository:
1. GitLab: open `BetterToBest-group` > **New project** > **Import project** > **Repository by URL**.
2. Git repository URL: `https://github.com/BetterToBest/<name>.git`. Leave username and password empty for public repositories.
3. Tick **Mirror repository** (and **Mirror only protected branches** off). Project name `<name>`, visibility Public. **Create project**.
4. Project > **Settings > Repository > Mirroring repositories**: direction Pull, mirror every branch, interval shown as "last update". Select the refresh arrow once to run now.

## Option B: GitHub pushes to GitLab (free)
One workflow per repository, on push to main. Needs a GitLab deploy token or project access token with `write_repository`, saved as the GitHub secret `GITLAB_TOKEN`. A mirror push is a sync, not a study, but CLAUDE.md allows Actions only for checks, builds, releases and deploys, so this is a decision for Duke before it is added.
```yaml
name: mirror-to-gitlab
on: { push: { branches: [main] } }
jobs:
  mirror:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - run: git push --force https://oauth2:${{ secrets.GITLAB_TOKEN }}@gitlab.com/BetterToBest-group/${{ github.event.repository.name }}.git main
```
(Create each empty GitLab project first: group > **New project > Create blank project**, no README.)

## Check each mirror has the latest commit
```bash
for r in research-update research-hub compassionism-simulation bettertobest.github.io x-cents NormativeEvaluation portal compassionate-meritocracy-plan; do
  gh=$(git ls-remote https://github.com/BetterToBest/$r.git refs/heads/main | cut -f1)
  gl=$(git ls-remote https://gitlab.com/BetterToBest-group/$r.git refs/heads/main | cut -f1)
  [ "$gh" = "$gl" ] && echo "ok   $r $gh" || echo "DIFF $r github=$gh gitlab=$gl"
done
```
