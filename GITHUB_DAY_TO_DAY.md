# Git and GitHub day-to-day lab

This guide uses the Hello World DevOps Lab to practice the Git and GitHub commands you will use regularly. Git tracks your local files and history. GitHub hosts the shared repository and adds issues, pull requests, reviews, and workflow runs.

Run commands yourself in PowerShell. Read `git status` and inspect diffs before staging or committing.

## 1. Check your tools and set your commit identity

```powershell
git --version
gh --version
```

If `gh` is installed, sign in through its browser-based flow and check the result:

```powershell
gh auth login
gh auth status
```

Set the name and email Git will put on your commits. Replace the example values. If you want to avoid publishing your personal email in commits, use the GitHub-provided noreply address shown in your GitHub email settings.

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --list
```

## 2. Make the first local commit

Move into this project folder:

```powershell
cd "C:\Users\saiku\Documents\Codex\2026-11-03\le\opslab"
```

Initialize the repository and inspect it:

```powershell
git init -b main
git status
```

Stage the project files, inspect exactly what will be committed, then commit:

```powershell
git add README.md GITHUB_DAY_TO_DAY.md app.py requirements.txt .gitignore
git status
git diff --cached
git commit -m "Initialize Hello World web app"
git log --oneline
```

Key idea: `git add` stages the changes; `git commit` saves the staged snapshot to local history. A commit does not upload anything to GitHub.

## 3. Create the GitHub remote and push

On GitHub, create a **private** repository named `hello-world-devops`. Leave it empty: do not initialize it with a README, license, or `.gitignore`, since those files already exist locally.

Connect your local repository and publish its `main` branch:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/hello-world-devops.git
git remote -v
git push -u origin main
gh repo view --web
```

Replace `YOUR-USERNAME` with your GitHub username. `origin` is the conventional name for the remote. `-u` records which remote branch this local branch tracks, so later `git push` and `git pull` can omit the remote and branch names.

## 4. The normal change, branch, and pull request loop

First, sync `main` and create a short-lived branch for one change:

```powershell
git switch main
git pull --ff-only
git switch -c docs/improve-setup-guide
git status
```

Make a small change to `README.md` in your editor. Review it before staging:

```powershell
git diff
git status
git add -p README.md
git diff --cached
git commit -m "Improve local setup instructions"
git push -u origin docs/improve-setup-guide
```

`git add -p` lets you stage selected parts of a file. This is useful when one file contains both relevant and unrelated changes.

Open a pull request and inspect it:

```powershell
gh pr create --fill
gh pr status
gh pr view
gh pr diff
gh pr checks
```

On your first pull request, GitHub may ask you to choose the base and compare branches or enter a title and description. Review the diff on GitHub, wait for required checks, and merge it there or with `gh pr merge --squash` if you are ready. Do not use `--admin` to bypass required checks.

After merging, update local `main` and remove the finished local branch:

```powershell
git switch main
git pull --ff-only
git branch -d docs/improve-setup-guide
git branch -vv
```

## 5. Common GitHub CLI commands

Issues:

```powershell
gh issue list
gh issue view 1
gh issue create
gh issue close 1
```

Pull requests:

```powershell
gh pr list
gh pr status
gh pr view 1
gh pr diff 1
gh pr checks 1
gh pr review 1
gh pr update-branch
gh pr merge 1 --squash
```

Repository and automation runs:

```powershell
gh repo view
gh run list
gh run view RUN_ID
```

Replace example issue, PR, and run numbers with real ones. `gh pr review` has interactive options; inspect `gh pr review --help` before submitting a review.

## 6. Inspect, compare, and recover

Useful inspection commands:

```powershell
git status --short
git log --oneline --graph --decorate --all
git show COMMIT_ID
git diff
git diff --staged
git branch -a
git remote -v
git fetch origin
git status -sb
```

`git fetch` downloads remote information without merging it into your current branch. `git pull` fetches and then integrates the tracked remote branch. Use `git pull --ff-only` when you want Git to stop instead of creating an unexpected merge commit.

Recover from common mistakes:

```powershell
git restore --staged README.md
git stash push -m "work in progress"
git stash list
git stash pop
git revert COMMIT_ID
```

- `git restore --staged` unstages a file but keeps your edits.
- `git stash` temporarily shelves uncommitted changes; `git stash pop` reapplies them.
- `git revert` creates a new commit that reverses an earlier commit, which is safer for changes already shared with others.
- `git restore README.md` discards unstaged edits to that file. Use it only when you are sure you do not need those edits.

We will learn `reset`, rebasing, conflict resolution, tags, releases, and GitHub Actions in separate exercises. Avoid `git reset --hard` while learning: it can permanently discard local work.

## Day-to-day command map

| Task | Commands to reach for |
|---|---|
| Check what changed | `git status`, `git diff` |
| Stage and save work | `git add -p`, `git diff --staged`, `git commit` |
| Start or change branches | `git switch -c`, `git switch`, `git branch` |
| Sync with GitHub | `git fetch`, `git pull --ff-only`, `git push` |
| Review shared work | `gh pr list`, `gh pr view`, `gh pr diff`, `gh pr checks` |
| Track work | `gh issue list`, `gh issue view`, `gh issue create` |
| Recover safely | `git restore --staged`, `git stash`, `git revert` |


