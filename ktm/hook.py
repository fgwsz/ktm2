# -*- coding: utf-8 -*-
from . import config
from . import mouse

g_callback_table={}
g_leader_is_press=False
g_app_is_pause=False

def init():
    global g_callback_table
    g_callback_table={
        config.Shortcut.mouse_move_up          :mouse.Mouse.move_up          ,
        config.Shortcut.mouse_move_down        :mouse.Mouse.move_down        ,
        config.Shortcut.mouse_move_left        :mouse.Mouse.move_left        ,
        config.Shortcut.mouse_move_right       :mouse.Mouse.move_right       ,
        config.Shortcut.mouse_left_click       :mouse.Mouse.left_click       ,
        config.Shortcut.mouse_left_double_click:mouse.Mouse.left_double_click,
        config.Shortcut.mouse_left_down        :mouse.Mouse.left_down        ,
        config.Shortcut.mouse_left_up          :mouse.Mouse.left_up          ,
        config.Shortcut.mouse_right_click      :mouse.Mouse.right_click      ,
        config.Shortcut.mouse_right_down       :mouse.Mouse.right_down       ,
        config.Shortcut.mouse_right_up         :mouse.Mouse.right_up         ,
        config.Shortcut.mouse_wheel_down       :mouse.Mouse.wheel_down       ,
        config.Shortcut.mouse_wheel_up         :mouse.Mouse.wheel_up         ,
        config.Shortcut.mouse_distance_double  :mouse.Mouse.distance_double  ,
        config.Shortcut.mouse_distance_halve   :mouse.Mouse.distance_halve   ,
    }

def is_normal_key(key):
    ret=True
    try:
        ret=key.char
    except AttributeError:
        ret=False
    return ret

def is_shortcut_of_leader(key):
    return key==config.Shortcut.leader

def on_press(key):
    global g_leader_is_press
    global g_app_is_pause
    global g_callback_table
    if not is_normal_key(key):
        if key==config.Shortcut.leader:
            g_leader_is_press=True
    elif not g_app_is_pause \
        and g_leader_is_press \
        and key.char in g_callback_table:
        g_callback_table[key.char]()
    elif key.char==config.Shortcut.app_pause:
        g_app_is_pause=True
    elif key.char==config.Shortcut.app_restart:
        g_app_is_pause=False
    elif key.char==config.Shortcut.app_close:
        return False

def on_release(key):
    global g_leader_is_press
    if not is_normal_key(key):
        if key==config.Shortcut.leader:
            g_leader_is_press=False
