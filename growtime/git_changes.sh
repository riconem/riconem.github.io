#!/bin/bash

cd "$( dirname "$BASH_SOURCE" )"

git add -A
git commit -m "auto-pi: adding picture of $(date +%H:%M:%S-%d.%m.%y)"
git push origin master
