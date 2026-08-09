# Environment variables
.env

# Python virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.pyc

# Logs
*.log

# Test cache
.pytest_cache/

# Coverage
.coverage
htmlcov/

# Ruff
.ruff_cache/

# Mypy
.mypy_cache/


# Day 15 - .gitignore

## What is .gitignore?

`.gitignore` tells Git which untracked files and folders it should ignore.

## Example

```gitignore
```
.env
venv/
__pycache__/
*.pyc
*.log



# Important patterns
.env
= ignore .env

*.log
= ignore all .log files

venv/
= ignore the venv folder

__pycache__/
= ignore Python cache