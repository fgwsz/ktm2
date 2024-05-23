#!/bin/bash
if ! pip show pynput &> /dev/null; then
    pip install pynput
fi
if ! pip show pyautogui &> /dev/null; then
    pip install pyautogui
fi
sudo apt-get install python3-tk python3-dev #for linux pyautogui
