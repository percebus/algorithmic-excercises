#!/bin/bash

set -e
set -x

shopt -s globstar
python -m doctest -v src/**/*.md
python -m doctest -v src/**/*.rst

set +x
set +e
