#!/bin/bash

set -e

filename="requirements.pipx_inject.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
  exit 0
fi

set -v

# pipx inject --requirement requirements.pipx_inject.txt # FIXME
cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 pipx inject

set +v
set +e
