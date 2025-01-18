#!/bin/bash

set -e

enironment=$1
echo "enironment:'${enironment}'"

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/gil/setup.ba.sh

if [[ "${enironment}" == "ci" ]]; then
    mv ${scripts_path}/setup/ci.ba.sh setup.ba.sh
fi

bash ./repos/commons/scripts/prepare.ba.sh

set +x
set +e
