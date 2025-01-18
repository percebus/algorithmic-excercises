#!/bin/bash

set -e

enironment=$1
echo "enironment:'${enironment}'"

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

if [[ "${enironment}" == "ci" ]]; then
    rm ${scripts_path}/setup.ba.sh
    mv ${scripts_path}/setup/ci.ba.sh ${scripts_path}/setup.ba.sh
fi

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/gil/setup.ba.sh

bash ./repos/commons/scripts/prepare.ba.sh

set +x
set +e
