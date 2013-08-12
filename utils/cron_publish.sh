#!/bin/bash

source "/home/ec2-user/.virtualenvs/ultimate-sport/bin/activate"
prefix=`dirname "$0"`
pushd $prefix
python -c 'from github_listen import publish_site; publish_site()'
popd
