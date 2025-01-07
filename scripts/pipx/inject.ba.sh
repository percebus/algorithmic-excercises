#!/bin/bash

set -e
set -v

pipx inject --requirement requirements.pipx_inject.txt

set +v
set +e
