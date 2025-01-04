#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

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

python -m pip install --upgrade --verbose pip
python -m pip install --upgrade --verbose --requirement requirements.upgrade.txt

# pipx installs CLI executables, like poetry
bash ${scripts_path}/pipx/setup.ba.sh

# poetry has its own plugins
bash ${scripts_path}/poetry/plugin/add.ba.sh


python -m pip install --verbose --requirement requirements.txt
python -m pip install --verbose .

set +v
set +e
