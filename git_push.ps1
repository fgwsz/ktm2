git add ./ktm/*.py
git add ./ktm/*.json
git add ./*.sh
git add ./*.ps1
git add ./README.md
$commit_info=Read-Host -prompt "Input Git Commit Info"
git commit -m $commit_info
git push
