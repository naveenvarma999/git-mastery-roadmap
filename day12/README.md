# day12 interactive staging 

# Day 12 - Interactive Staging

## What is interactive staging?

Interactive staging allows me to stage selected parts of a changed file.

The command is:

```bash
git add -p
```

# What is a hunk?
A hunk is a group of nearby changed lines.

Git shows each hunk and asks whether I want to stage it.

# Important options

y = stage this hunk
n = do not stage this hunk
s = split into smaller hunks
q = quit
a = stage this and all remaining hunks
d = skip this and all remaining hunks
e = manually edit the patch
? = show help



# command checklist

git status
git diff
git add -p
git add -p filename
git add -p folder
git diff --staged
git diff
git restore -p --staged
git restore --staged filename
git commit -m "Clear logical message"
git log --oneline
git push
Day 12 completion result

# The main difference is:

git add file
    = stage every change in the file

git add -p file
    = select individual hunks to stage


# The complete professional workflow is:

Several changes in one file
        ↓
git diff
        ↓
git add -p
        ↓
Select hunks using y, n, or s
        ↓
git diff --staged
        ↓
Commit one logical change
        ↓
Stage remaining hunks
        ↓
Create another logical commit

# Remember:

Interactive staging lets you commit changes—not just complete files.


# To stage only part of the changes, normally use:

s = split the current hunk into smaller parts

Then Git shows each smaller part separately.

# For each part:

y = stage this part
n = leave this part unstaged

# Example:

Stage this hunk [y,n,q,a,d,s,e,?]? s

# Git splits it:
First change? y
Second change? n

# Result:

First change  = staged
Second change = unstaged


# Meaning of the main options
y = stage the complete displayed hunk
n = do not stage the displayed hunk
s = split the hunk, then choose y or n for each smaller part
e = manually edit the patch for line-by-line control
d = skip this hunk and all remaining hunks

# So the easiest method for partial staging is:

git add -p app.py

# Then choose:

s
y
n

# Afterward, verify:

git diff --staged

This shows the selected staged part.

git diff

This shows the part left unstaged.

# If Git says the hunk cannot be split, use:

e
