#!/bin/bash
KTM_MODULE_DIR=$(dirname "$(readlink -f "$0")")
cd $KTM_MODULE_DIR
if ! pip show pynput &> /dev/null; then
    pip3 install pynput
fi
python3 -m ktm
