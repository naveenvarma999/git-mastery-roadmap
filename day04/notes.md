# Day 4 - Creating a Git Repository

## What I learned

A normal folder becomes a Git repository when it contains a `.git` directory.

The `git init` command initializes a new local Git repository.

```bash
git init

# Useful commands

git status
git rev-parse --show-toplevel    Use it when you are inside many subfolders and want to know which repository Git is using.

git rev-parse --is-inside-work-tree       This means the current folder is inside a Git working tree. 

git rev-parse --git-dir



cd "C:\Users\NAVEEN VARMA\Downloads"
mkdir git-init-practice
cd git-init-practice
git status
git init
git status
dir /a
echo Learning git init > README.md
git add README.md
git commit -m "Add initial README"
git log --oneline