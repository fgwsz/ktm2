$KTM_MODULE_DIR = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Set-Location $KTM_MODULE_DIR
python -m ktm
