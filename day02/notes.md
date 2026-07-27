# Day 2 - Git Configuration

## What I learned

Git configuration controls settings such as:

- Username
- Email
- Default branch
- Text editor
- Line endings
- Pull behaviour

## Configuration levels
1. System configuration affects all users.
2. Global configuration affects my user account.
3. Local configuration affects only the current repository.

Local configuration has higher priority than global configuration.

## Commands practised

```bash
git config --global user.name "Naveen Varma"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global core.autocrlf true
git config --global color.ui auto
git config --global pull.rebase false
git config --global --list
git config --list --show-origin