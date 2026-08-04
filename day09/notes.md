# Day 9 - Commit IDs and HEAD

## Commit ID

Every Git commit has a unique identifier called a commit ID or commit hash.

Example:

```text
a8e8195
```

# The short ID is displayed by:

git log --oneline


# The full commit ID is displayed by:

git log
HEAD

HEAD represents my current position in Git history.

# Normally:

HEAD → current branch → latest commit
Relative commit references
HEAD    = current commit
HEAD~1  = one commit before HEAD
HEAD~2  = two commits before HEAD
HEAD~3  = three commits before HEAD

# Important commands

git log --oneline
git log -3 --oneline
git show HEAD
git show HEAD~1
git show COMMIT_ID
git show --stat COMMIT_ID
git show --no-patch COMMIT_ID
git rev-parse HEAD
git rev-parse --short HEAD
git diff HEAD~1 HEAD


# Important lesson

A branch is a movable pointer to a commit.

When I create a new commit, the current branch moves forward to the new commit.


Save the file.

---

# 41. Stage and commit the Day 9 README

Run:

```bash
git add day-09/README.md

Inspect:

git diff --staged

Commit:

git commit -m "Add Day 9 commit ID notes"

Check:

git log -5 --oneline

Push:

git push
42. Day 9 practice challenge

Run:

git log -5 --oneline

Choose one older commit ID.

For example:

856519a Working Directory, Staging Area, and Repository

Inspect it:

git show 856519a

Show only its summary:

git show --stat 856519a

Show only its commit information:

git show --no-patch 856519a

Then inspect the current commit:

git show HEAD

# Inspect the previous commit:

git show HEAD~1







# Day 9 command checklist

git log
git log --oneline
git log -3 --oneline
git show
git show HEAD
git show HEAD~1
git show HEAD~2
git show COMMIT_ID
git show --stat COMMIT_ID
git show --no-patch COMMIT_ID
git rev-parse HEAD
git rev-parse --short HEAD
git diff HEAD~1 HEAD



# The main structure is:

HEAD
 ↓
main branch
 ↓
latest commit
 ↓
previous commit
 ↓
older commits



# Example:
HEAD → main → C4
               |
               C3
               |
               C2
               |
               C1



# Remember:

Commit ID uniquely identifies a commit.

HEAD represents the current Git position.

HEAD~1 means the previous commit.

git show displays the details and changes of a commit.

git log --oneline displays short commit history.


