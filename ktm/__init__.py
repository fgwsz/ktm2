# -*- coding: utf-8 -*-
import os
from . import load_config
from . import mouse
from . import hook

g_config_json_path=os.path.abspath(
    os.path.dirname(os.path.abspath(__file__))
)+'/config.json'
g_config_json_load_failed=not load_config.load_config(g_config_json_path)
mouse.Mouse.init()
hook.init()