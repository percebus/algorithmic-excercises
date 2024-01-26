#!/bin/bash

SCRIPTS_PATH="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${SCRIPTS_PATH}"

set -e
set -v

python -m pip install --upgrade --verbose --requirement requirements.upgrade.txt
bash ${SCRIPTS_PATH}/pipx/install.ba.sh
bash ${SCRIPTS_PATH}/pipx/inject.ba.sh
python -m pip install --verbose --requirement requirements.txt
python -m pip install --verbose .

set +v
set +e
