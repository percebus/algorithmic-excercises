#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"


set -x

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/prepare.ba.sh
bash ./_scripts/setup.ba.sh
bash ./_scripts/poetry/install.ba.sh ci

set +x
set +e
