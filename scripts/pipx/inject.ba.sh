#!/bin/bash

set -e
set -v

cat requirements.pipx_inject.txt | xargs -n 1 "pipx inject"

set +v
set +e
