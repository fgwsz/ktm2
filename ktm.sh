#!/bin/bash
KTM_MODULE_DIR=$(dirname "$(readlink -f "$0")")
cd $KTM_MODULE_DIR
if ! pip show pynput &> /dev/null; then
    pip install pynput
fi
python -m ktm
