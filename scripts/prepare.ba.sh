#!/bin/bash

set -e

environment=${1}
echo "environment: ${environment}"

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

if [ "${environment}" == "pre-docker" ]; then
    rm ${scripts_path}/setup.ba.sh
fi

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/gil/setup.ba.sh

bash ./repos/commons/scripts/prepare.ba.sh

set +x
set +e
