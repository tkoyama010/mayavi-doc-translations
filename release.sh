#!/bin/sh

set -ex

# setup environment
SPHINXINTL_TRANSIFEX_USERNAME=api
SPHINXINTL_TRANSIFEX_PROJECT_NAME=mayavi
find mayavi -name "*.pyc" -exec rm {} \;
git checkout master
git submodule init
git submodule update
(cd mayavi; git fetch origin; git checkout origin/master)
pip install -r requirements.txt


# update transifex pot and local po files
sh ./locale/update.sh

# commit po(t) files
git add locale mayavi
git commit -m "[skip ci] update po(t) files"

# push changes
git checkout master
git submodule update
git push origin master
