#!/bin/bash

set -e

filename="requirements.poetry-plugin.txt"
if [[ -z $(grep '[^[:space:]]' $filename) ]]; then
  echo "${filename} is empty, skipping..."
else
  set -v
  cat ${filename} | sed 's/.*/"&"/' | xargs -n 1 poetry self add
  set +v
fi

poetry self show plugins

set +e
