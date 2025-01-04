#!/bin/bash

set -e
set -v

filename="requirements.poetry-plugin.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
else
  cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 poetry self add
fi

poetry self show plugins

set +v
set +e
