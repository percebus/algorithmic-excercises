#!/bin/bash

set -e

environment=${1}
echo "environment: ${environment}"

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"


if [ "${environment}" == "pre-docker" ]; then
    set -x
    rm ${scripts_path}/setup.ba.sh
    set +x
fi

set -x

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/pip/upgrade.ba.sh
gil clone
bash ./repos/commons/scripts/prepare.ba.sh

set +x
set +e
