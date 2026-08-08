git add filename
= stage whole file

git add -p
= stage selected parts

git commit
= create new commit

git commit --amend
= replace latest commit

git diff
= unstaged changes

git diff --staged
= staged changes

git log --oneline
= short commit history

HEAD
= current Git position

HEAD~1
= previous commit



# Day 14 interview check

# You should now be able to answer these without looking:

# What is the staging area?
The place where we prepare changes before committing.

# Difference between git add and git commit?
git add stages changes; git commit saves staged changes to local history.

# Difference between git diff and git diff --staged?
git diff shows unstaged changes; git diff --staged shows staged changes.

# What is HEAD?
It represents the current position in Git history and normally points through the current branch to the latest commit.

# What does git add -p do?
It lets you stage selected parts of changed files.

# What does git commit --amend do?
It replaces the latest commit with a corrected version.

# Does git commit upload to GitHub?
No. git push uploads commits.

# What does git log --oneline show?
Short commit IDs and commit messages.

# What does git status show?
Current branch and file states such as untracked, modified and staged.

# Why make small logical commits?
They are easier to review, understand, debug and undo.