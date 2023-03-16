#!/usr/bin/env bash

set -e

here=$(dirname $0)
pids=()

for proj in ${here}/*; do
    if [ ! -d "$proj" ]; then
        continue
    fi
    
    echo "Testing $proj"
    pushd "$proj"
    mix test
    popd
done
