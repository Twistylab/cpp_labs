#!/bin/bash

git checkout dev

git pull origin dev

git pull orogon dev

git checkout stg
git pull origin stg

git merge dev -m "Auto merge dev to stg"

TAG="stg-$(date +%Y-%m-%d-%H%M%S)"
git tag -a "$TAG" -m "Moved to stg $TAG"

git push origin stg
git push origin "$TAG"

echo "Moved dev -> stg with tag $TAG"
