
SCRIPTS_PATH="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${SCRIPTS_PATH}"

set -e
set -v

bash ${SCRIPTS_PATH}/pipx/install.ba.sh
bash ${SCRIPTS_PATH}/pipx/inject.ba.sh

set +v
set +e
