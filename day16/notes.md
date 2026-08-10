command checklist
git status

git ls-files filename

git check-ignore -v filename

git rm --cached filename

git rm -r --cached folder/

git add .gitignore

git diff --staged

git commit -m "Stop tracking file"

git push



# Remember this clearly:

Already tracked file
        ↓
Add it to .gitignore
        ↓
git rm --cached file
        ↓
Git stops tracking it
        ↓
File stays on your computer



# And the most important comparison:

git rm
= remove from Git + delete local file

git rm --cached
= remove from Git tracking + KEEP local file