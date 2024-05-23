#!/bin/bash
git add ./ktm/*.py
git add ./ktm/*.json
git add ./*.sh
git add ./*.ps1
git add ./README.md
read -p "Input Git Commit Info: " commit_info
git commit -m "$commit_info"
git push
