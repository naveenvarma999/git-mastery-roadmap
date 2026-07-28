# Day 8 - Creating Good Git Commits

## What is a commit?

A commit is a saved snapshot of staged project changes.

## Basic workflow

```bash
git status
git add filename
git diff --staged
git commit -m "Clear commit message"
git push
```


# Important points

A commit includes only staged changes.
A commit is saved locally.
git push uploads commits to GitHub.
One commit should represent one logical change.
Commit messages should clearly explain what changed.

# Good messages

Add user login validation
Fix incorrect payment calculation
Update API documentation
Remove unused configuration
Refactor database connection logic

# Weak messages

changes
update
fix
final
work


# Recommended message format

Action + what changed


# completion result

The main workflow is:

Edit files
    ↓
git status
    ↓
git add selected-files
    ↓
git diff --staged
    ↓
git commit -m "Clear message"
    ↓
git log --oneline
    ↓
git push



# Remember:

A good commit saves one logical change.
A good commit message clearly explains that change.
Only staged changes enter the commit.
The commit stays local until you push it.