# -*- coding: utf-8 -*-
import os
import pynput
from . import load_config
from . import mouse
from . import hook

if __name__=="__main__":
    config_file_path=os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
    )+'/config.json'
    if load_config.load_config(config_file_path):
        mouse.Mouse.init()
        hook.init()
        with pynput.keyboard.Listener(
            on_press=hook.on_press,
            on_release=hook.on_release
        )as listener:
            listener.join()