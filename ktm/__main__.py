# -*- coding: utf-8 -*-
import pynput
from . import hook

def main():
    with pynput.keyboard.Listener(
        on_press=hook.on_press,
        on_release=hook.on_release
    )as listener:
        listener.join()

if __name__=="__main__":
    main()