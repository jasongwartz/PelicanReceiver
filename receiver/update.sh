#! /bin/bash
# Update Pelican

export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR
cd ..
pelican content
