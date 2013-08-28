#!/bin/bash

# Update nikola
pushd $HOME/packages/nikola
git reset --hard
git checkout master
git pull origin master
popd

# Publish site
source "/home/ec2-user/.virtualenvs/ultimate-sport/bin/activate"
prefix=`dirname "$0"`
pushd $prefix
python -c 'from github_listen import publish_site; publish_site()'
popd
