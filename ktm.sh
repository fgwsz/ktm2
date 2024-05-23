#!/bin/bash
KTM_MODULE_DIR=$(dirname "$(readlink -f "$0")")
cd $KTM_MODULE_DIR
if ! type python &> /dev/null; then
    python3 -m ktm
else
    python -m ktm
fi
