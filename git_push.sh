git add ./ktm/*.py
git add ./ktm/*.json
git add ./git_push.sh
read -p "Input Git Commit Info: " commit_info
git commit -m $commit_info
git push
