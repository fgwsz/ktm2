#!/bin/bash
if ! pip show pynput &> /dev/null; then
    pip install pynput
fi

if ! pip show pyautogui &> /dev/null; then
    pip install pyautogui
fi

#for linux pyautogui
if ! dpkg -l python3-tk &> /dev/null; then
    sudo apt-get install python3-tk
fi
if ! dpkg -l python3-dev &> /dev/null; then
    sudo apt-get install python3-dev
fi
