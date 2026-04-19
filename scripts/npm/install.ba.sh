#!/bin/bash

set -e
set -x

# TODO? Move to commons?
npm run setup
npm ci

set +x
set +e
