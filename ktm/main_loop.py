# -*- coding: utf-8 -*-
import pynput
from . import hook

def execute():
    with pynput.keyboard.Listener(
        on_press=hook.on_press,
        on_release=hook.on_release
    )as listener:
        listener.join()
