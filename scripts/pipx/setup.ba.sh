#!/bin/bash

set -e
set -v

parent_folder="$(dirname "$(readlink -f "$0")")"
bash ${parent_folder}/install.ba.sh
bash ${parent_folder}/inject.ba.sh

set +v
set +e
