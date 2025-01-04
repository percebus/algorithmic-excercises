#!/bin/bash

set -e
set -v

filename="requirements.pipx_inject.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
else
  cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 pipx inject
fi

set +v
set +e
