#!/bin/bash
git add ./ktm/*.py
git add ./ktm/*.json
git add ./git_push.sh
git add ./git_push.ps1
git add ./ktm.sh
git add ./ktm.ps1
git add ./README.md
read -p "Input Git Commit Info: " commit_info
git commit -m "$commit_info"
git push
