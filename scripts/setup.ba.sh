#!/bin/bash

set -e

target_config=$1
echo "target_config:'${target_config}'"

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -v

# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/pip/upgrade.ba.sh

# pipx installs CLI executables, like poetry
bash ${scripts_path}/pipx/setup.ba.sh

# poetry has its own plugins
bash ${scripts_path}/poetry/plugin/add.ba.sh

# Install dependencies from requirements{.release}.txt
bash ${scripts_path}/pip/install.ba.sh ${target_config}
bash ${scripts_path}/pip/freeze.ba.sh

set +v
set +e
