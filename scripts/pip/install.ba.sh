#!/bin/bash

target_config=$1
echo "target_config:'${target_config}'"

requirements="requirements.txt"
if [[ "$target_config" == "prd" ]]; then
    echo "Installing ONLY prd requirements..."
    requirements="requirements.prd.txt"
else
    echo "Installing everything..."
fi

set -e
set -v

python -m pip install --verbose --upgrade --requirement requirements.upgrade.txt
python -m pip install --verbose --requirement ${requirements}
python -m pip install --verbose .

set +v
set +e
