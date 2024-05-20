$KTM_MODULE_DIR = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Set-Location $KTM_MODULE_DIR
if(-not(pip show pynput 2>&1)){
    pip install pynput
}
python -m ktm
