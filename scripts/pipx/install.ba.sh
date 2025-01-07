#!/bin/bash

set -e

filename="requirements.pipx.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
else
  set -v
  cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 pipx install
  set +v
fi

set +e
