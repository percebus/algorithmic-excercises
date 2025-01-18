#!/bin/bash

set -e
set -x

python -m pip install --upgrade pip
python -m pip install pipx
python -m pipx install gil
gil clone
bash ./repos/commons/scripts/prepare.ba.sh

set +x
set +e
