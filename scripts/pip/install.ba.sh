#!/bin/bash

set -e

target_config=$1
echo "target_config:'${target_config}'"

PIP_CLI_OPTS=""
requirements="requirements.txt"
if [[ "$target_config" == "release" ]]; then
    echo "Installing ONLY prd requirements..."
    requirements="requirements.release.txt"
else
    PIP_CLI_OPTS="-e"
    echo "Installing everything..."
fi

set -v

# pip upgrades pip
python -m pip install --verbose --upgrade pip

# pip upgrades pipx
python -m pip install --verbose --upgrade --requirement requirements.upgrade.txt

# all pip dependencies (generated w/ poetry)
python -m pip install --verbose --requirement ${requirements}

# The project itself (to use src)
python -m pip install --verbose ${PIP_CLI_OPTS} .

set +v
set +e
