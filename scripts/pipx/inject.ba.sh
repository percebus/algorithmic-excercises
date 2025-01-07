#!/bin/bash

set -e
set -v

pipx inject -r requirements.pipx_inject.txt

set +v
set +e
