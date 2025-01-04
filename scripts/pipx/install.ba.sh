#!/bin/bash

set -e
set -v

filename="requirements.pipx.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
else
  cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 pipx install
fi

set +v
set +e
