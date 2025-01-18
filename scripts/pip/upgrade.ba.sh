#!/bin/bash

set -e
set -x

python -m pip install --upgrade pip
python -m pip install --upgrade --requirement requirements.upgrade.txt

set +x
set +e
