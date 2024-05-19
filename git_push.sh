git add ./ktm/*.py
git add ./*.py
git add ./*.sh
read -p "Input Git Commit Info: " commit_info
git commit -m $commit_info
git push
