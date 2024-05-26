# -*- coding: utf-8 -*-
from ktm import config
from ktm import mouse

g_callback_table={}
g_leader_is_press=False
g_app_is_pause=False

def init():
    global g_callback_table
    g_callback_table={
        config.Shortcut.mouse_move_up            :mouse.Mouse.move_up            ,
        config.Shortcut.mouse_move_down          :mouse.Mouse.move_down          ,
        config.Shortcut.mouse_move_left          :mouse.Mouse.move_left          ,
        config.Shortcut.mouse_move_right         :mouse.Mouse.move_right         ,
        config.Shortcut.mouse_left_click         :mouse.Mouse.left_click         ,
        config.Shortcut.mouse_left_double_click  :mouse.Mouse.left_double_click  ,
        config.Shortcut.mouse_left_press         :mouse.Mouse.left_press         ,
        config.Shortcut.mouse_left_release       :mouse.Mouse.left_release       ,
        config.Shortcut.mouse_right_click        :mouse.Mouse.right_click        ,
        config.Shortcut.mouse_right_double_click :mouse.Mouse.right_double_click ,
        config.Shortcut.mouse_right_press        :mouse.Mouse.right_press        ,
        config.Shortcut.mouse_right_release      :mouse.Mouse.right_release      ,
        config.Shortcut.mouse_middle_click       :mouse.Mouse.middle_click       ,
        config.Shortcut.mouse_middle_double_click:mouse.Mouse.middle_double_click,
        config.Shortcut.mouse_middle_press       :mouse.Mouse.middle_press       ,
        config.Shortcut.mouse_middle_release     :mouse.Mouse.middle_release     ,
        config.Shortcut.mouse_scroll_down        :mouse.Mouse.scroll_down        ,
        config.Shortcut.mouse_scroll_up          :mouse.Mouse.scroll_up          ,
        config.Shortcut.mouse_distance_double    :mouse.Mouse.distance_double    ,
        config.Shortcut.mouse_distance_halve     :mouse.Mouse.distance_halve     ,
    }

def is_normal_key(key):
    ret=True
    try:
        ret=key.char
    except AttributeError:
        ret=False
    return ret

def on_press(key):
    global g_leader_is_press
    global g_app_is_pause
    global g_callback_table
    if not is_normal_key(key):
        if key==config.Shortcut.leader:
            g_leader_is_press=True
    elif g_leader_is_press:
        if key.char==config.Shortcut.app_pause:
            g_app_is_pause=True
        elif key.char==config.Shortcut.app_restart:
            g_app_is_pause=False
        elif key.char==config.Shortcut.app_close:
            return False
        elif (not g_app_is_pause) and key.char in g_callback_table:
            g_callback_table[key.char]()

def on_release(key):
    global g_leader_is_press
    if not is_normal_key(key):
        if key==config.Shortcut.leader:
            g_leader_is_press=False
