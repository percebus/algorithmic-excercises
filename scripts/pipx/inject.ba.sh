#!/bin/bash

set -e
set -v

pipx inject poetry poetry-plugin-export

set +v
set +e
