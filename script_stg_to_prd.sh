#!/bin/bash

git checkout stg
git pull origin stg

git checkout prd
git pull origin prd

gir merge stg -m "Auto merge stg to prd"

TAG="prd-$(date +%Y-%m-%d-%H%M%S)"
git tag -a "$TAG" -m "Moved to prd $TAG"

git push origin prd
git push origin "$TAG"

echo "Moved stg -> prd with tag $TAG"
