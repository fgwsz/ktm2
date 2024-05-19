# -*- coding: utf-8 -*-
from . import config
from . import mouse

g_leader_is_press=False

def leader_is_press():
    global g_leader_is_press
    return g_leader_is_press

def leader_up():
    global g_leader_is_press
    g_leader_is_press=False

def leader_down():
    global g_leader_is_press
    g_leader_is_press=True

def is_normal_key(key):
    ret=True
    try:
        ret=key.char
    except AttributeError:
        ret=False
    return ret

def is_shortcut_of_leader(key):
    return key==config.Shortcut.leader

callback_table={
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
    config.Shortcut.mouse_dpixel_double    :mouse.Mouse.dpixel_double    ,
    config.Shortcut.mouse_dpixel_halve     :mouse.Mouse.dpixel_halve     ,
}

def on_press(key):
    if not is_normal_key(key):
        if is_shortcut_of_leader(key):
            leader_down()
    elif key.char in callback_table:
        callback_table[key.char]()

def on_release(key):
    if not is_normal_key(key):
        if is_shortcut_of_leader(key):
            leader_up()
