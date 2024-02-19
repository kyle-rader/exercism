#!/usr/bin/env bash

here=$(dirname $0)
pids=()

for proj in ${here}/*; do
    if [ ! -d "$proj" ]; then
        continue
    fi
    
    echo "Testing $proj"
    pushd "$proj"
    mix test > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "❌ $proj"
    else
        echo "✅ $proj"
    fi
    popd
done
