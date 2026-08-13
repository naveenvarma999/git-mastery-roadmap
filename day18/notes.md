git status -- .

git mv old.txt new.txt

git mv file.txt folder/file.txt

git status --short -- .

git diff --staged --summary

git commit -m "Rename file"

git log --follow --oneline -- filename



# Remember this:

git mv old.txt new.txt
        ↓
File renamed/moved
        +
Change staged automatically
        ↓
git commit
        ↓
Rename saved in Git history


git rm
= remove file

git mv
= rename or move file