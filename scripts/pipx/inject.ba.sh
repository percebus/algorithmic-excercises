#!/bin/bash

set -e

filename="requirements.pipx_inject.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
fi

set -v

cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 pipx inject

set +v
set +e
