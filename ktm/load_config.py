# -*- coding: utf-8 -*-
import json
import pynput
from ktm import config

g_special_key_string_to_pynput_key={
    'alt':pynput.keyboard.Key.alt,
    'alt_l':pynput.keyboard.Key.alt_l,
    'alt_r':pynput.keyboard.Key.alt_r,
    'alt_gr':pynput.keyboard.Key.alt_gr,
    'backspace':pynput.keyboard.Key.backspace,
    'caps_lock':pynput.keyboard.Key.caps_lock,
    'cmd':pynput.keyboard.Key.cmd,
    'cmd_l':pynput.keyboard.Key.cmd_l,
    'cmd_r':pynput.keyboard.Key.cmd_r,
    'ctrl':pynput.keyboard.Key.ctrl,
    'ctrl_l':pynput.keyboard.Key.ctrl_l,
    'ctrl_r':pynput.keyboard.Key.ctrl_r,
    'delete':pynput.keyboard.Key.delete,
    'down':pynput.keyboard.Key.down,
    'end':pynput.keyboard.Key.end,
    'enter':pynput.keyboard.Key.enter,
    'esc':pynput.keyboard.Key.esc,
    'f1':pynput.keyboard.Key.f1,
    'f2':pynput.keyboard.Key.f2,
    'f3':pynput.keyboard.Key.f3,
    'f4':pynput.keyboard.Key.f4,
    'f5':pynput.keyboard.Key.f5,
    'f6':pynput.keyboard.Key.f6,
    'f7':pynput.keyboard.Key.f7,
    'f8':pynput.keyboard.Key.f8,
    'f9':pynput.keyboard.Key.f9,
    'f10':pynput.keyboard.Key.f10,
    'f11':pynput.keyboard.Key.f11,
    'f12':pynput.keyboard.Key.f12,
    'f13':pynput.keyboard.Key.f13,
    'f14':pynput.keyboard.Key.f14,
    'f15':pynput.keyboard.Key.f15,
    'f16':pynput.keyboard.Key.f16,
    'f17':pynput.keyboard.Key.f17,
    'f18':pynput.keyboard.Key.f18,
    'f19':pynput.keyboard.Key.f19,
    'f20':pynput.keyboard.Key.f20,
    'home':pynput.keyboard.Key.home,
    'left':pynput.keyboard.Key.left,
    'page_down':pynput.keyboard.Key.page_down,
    'page_up':pynput.keyboard.Key.page_up,
    'right':pynput.keyboard.Key.right,
    'shift':pynput.keyboard.Key.shift,
    'shift_l':pynput.keyboard.Key.shift_l,
    'shift_r':pynput.keyboard.Key.shift_r,
    'space':pynput.keyboard.Key.space,
    'tab':pynput.keyboard.Key.tab,
    'up':pynput.keyboard.Key.up,
    'media_play_pause':pynput.keyboard.Key.media_play_pause,
    'media_volume_mute':pynput.keyboard.Key.media_volume_mute,
    'media_volume_down':pynput.keyboard.Key.media_volume_down,
    'media_volume_up':pynput.keyboard.Key.media_volume_up,
    'media_previous':pynput.keyboard.Key.media_previous,
    'media_next':pynput.keyboard.Key.media_next,
    'insert':pynput.keyboard.Key.insert,
    'menu':pynput.keyboard.Key.menu,
    'num_lock':pynput.keyboard.Key.num_lock,
    'pause':pynput.keyboard.Key.pause,
    'print_screen':pynput.keyboard.Key.print_screen,
    'scroll_lock':pynput.keyboard.Key.scroll_lock,
}

g_normal_key_string_set={
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0',
    '`','-','=','[',']','\\',';','\'',',','.','/',
    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"',
    '<','>','?',
}

def load_config(config_file_path):
    global g_special_key_string_to_pynput_key
    global g_normal_key_string_set
    try:
        with open(config_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return False
    except json.JSONDecodeError:
        print("JSON file format error. Please check the syntax of the JSON file.")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

    if 'mouse_init_move_distance' in data \
        and(isinstance(data['mouse_init_move_distance'],int)) \
        and(data['mouse_init_move_distance']>0):
        config.Constant.mouse_init_move_distance=data['mouse_init_move_distance']
    else:
        print('[config failed]:mouse_init_move_distance')
        return False

    if 'mouse_init_scroll_distance' in data \
        and(isinstance(data['mouse_init_scroll_distance'],int)) \
        and(data['mouse_init_scroll_distance']>0):
        config.Constant.mouse_init_scroll_distance=data['mouse_init_scroll_distance']
    else:
        print('[config failed]:mouse_init_scroll_distance')
        return False

    if 'leader' in data \
        and(isinstance(data['leader'],str)) \
        and(data['leader'] in g_special_key_string_to_pynput_key):
        config.Shortcut.leader=g_special_key_string_to_pynput_key[data['leader']]
    else:
        print('[config failed]:leader')
        return False

    shortcut_normal_key_set=set()

    if 'mouse_move_up' in data \
        and(isinstance(data['mouse_move_up'],str)) \
        and(data['mouse_move_up'] in g_normal_key_string_set):
        config.Shortcut.mouse_move_up=data['mouse_move_up']
        shortcut_normal_key_set.add(config.Shortcut.mouse_move_up)
    else:
        print('[config failed]:mouse_move_up')
        return False

    if 'mouse_move_down' in data \
        and(isinstance(data['mouse_move_down'],str)) \
        and(data['mouse_move_down'] in g_normal_key_string_set) \
        and(data['mouse_move_down'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_move_down=data['mouse_move_down']
        shortcut_normal_key_set.add(config.Shortcut.mouse_move_down)
    else:
        print('[config failed]:mouse_move_down')
        return False

    if 'mouse_move_left' in data \
        and(isinstance(data['mouse_move_left'],str)) \
        and(data['mouse_move_left'] in g_normal_key_string_set) \
        and(data['mouse_move_left'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_move_left=data['mouse_move_left']
        shortcut_normal_key_set.add(config.Shortcut.mouse_move_left)
    else:
        print('[config failed]:mouse_move_left')
        return False

    if 'mouse_move_right' in data \
        and(isinstance(data['mouse_move_right'],str)) \
        and(data['mouse_move_right'] in g_normal_key_string_set) \
        and(data['mouse_move_right'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_move_right=data['mouse_move_right']
        shortcut_normal_key_set.add(config.Shortcut.mouse_move_right)
    else:
        print('[config failed]:mouse_move_right')
        return False

    if 'mouse_left_click' in data \
        and(isinstance(data['mouse_left_click'],str)) \
        and(data['mouse_left_click'] in g_normal_key_string_set) \
        and(data['mouse_left_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_left_click=data['mouse_left_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_left_click)
    else:
        print('[config failed]:mouse_left_click')
        return False

    if 'mouse_left_double_click' in data \
        and(isinstance(data['mouse_left_double_click'],str)) \
        and(data['mouse_left_double_click'] in g_normal_key_string_set) \
        and(data['mouse_left_double_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_left_double_click=data['mouse_left_double_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_left_double_click)
    else:
        print('[config failed]:mouse_left_double_click')
        return False

    if 'mouse_left_down' in data \
        and(isinstance(data['mouse_left_down'],str)) \
        and(data['mouse_left_down'] in g_normal_key_string_set) \
        and(data['mouse_left_down'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_left_down=data['mouse_left_down']
        shortcut_normal_key_set.add(config.Shortcut.mouse_left_down)
    else:
        print('[config failed]:mouse_left_down')
        return False

    if 'mouse_left_up' in data \
        and(isinstance(data['mouse_left_up'],str)) \
        and(data['mouse_left_up'] in g_normal_key_string_set) \
        and(data['mouse_left_up'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_left_up=data['mouse_left_up']
        shortcut_normal_key_set.add(config.Shortcut.mouse_left_up)
    else:
        print('[config failed]:mouse_left_up')
        return False

    if 'mouse_right_click' in data \
        and(isinstance(data['mouse_right_click'],str)) \
        and(data['mouse_right_click'] in g_normal_key_string_set) \
        and(data['mouse_right_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_right_click=data['mouse_right_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_right_click)
    else:
        print('[config failed]:mouse_right_click')
        return False

    if 'mouse_right_double_click' in data \
        and(isinstance(data['mouse_right_double_click'],str)) \
        and(data['mouse_right_double_click'] in g_normal_key_string_set) \
        and(data['mouse_right_double_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_right_double_click=data['mouse_right_double_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_right_double_click)
    else:
        print('[config failed]:mouse_right_double_click')
        return False

    if 'mouse_right_down' in data \
        and(isinstance(data['mouse_right_down'],str)) \
        and(data['mouse_right_down'] in g_normal_key_string_set) \
        and(data['mouse_right_down'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_right_down=data['mouse_right_down']
        shortcut_normal_key_set.add(config.Shortcut.mouse_right_down)
    else:
        print('[config failed]:mouse_right_down')
        return False

    if 'mouse_right_up' in data \
        and(isinstance(data['mouse_right_up'],str)) \
        and(data['mouse_right_up'] in g_normal_key_string_set) \
        and(data['mouse_right_up'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_right_up=data['mouse_right_up']
        shortcut_normal_key_set.add(config.Shortcut.mouse_right_up)
    else:
        print('[config failed]:mouse_right_up')
        return False

    if 'mouse_middle_click' in data \
        and(isinstance(data['mouse_middle_click'],str)) \
        and(data['mouse_middle_click'] in g_normal_key_string_set) \
        and(data['mouse_middle_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_middle_click=data['mouse_middle_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_middle_click)
    else:
        print('[config failed]:mouse_middle_click')
        return False

    if 'mouse_middle_double_click' in data \
        and(isinstance(data['mouse_middle_double_click'],str)) \
        and(data['mouse_middle_double_click'] in g_normal_key_string_set) \
        and(data['mouse_middle_double_click'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_middle_double_click=data['mouse_middle_double_click']
        shortcut_normal_key_set.add(config.Shortcut.mouse_middle_double_click)
    else:
        print('[config failed]:mouse_middle_double_click')
        return False

    if 'mouse_middle_down' in data \
        and(isinstance(data['mouse_middle_down'],str)) \
        and(data['mouse_middle_down'] in g_normal_key_string_set) \
        and(data['mouse_middle_down'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_middle_down=data['mouse_middle_down']
        shortcut_normal_key_set.add(config.Shortcut.mouse_middle_down)
    else:
        print('[config failed]:mouse_middle_down')
        return False

    if 'mouse_middle_up' in data \
        and(isinstance(data['mouse_middle_up'],str)) \
        and(data['mouse_middle_up'] in g_normal_key_string_set) \
        and(data['mouse_middle_up'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_middle_up=data['mouse_middle_up']
        shortcut_normal_key_set.add(config.Shortcut.mouse_middle_up)
    else:
        print('[config failed]:mouse_middle_up')
        return False

    if 'mouse_scroll_down' in data \
        and(isinstance(data['mouse_scroll_down'],str)) \
        and(data['mouse_scroll_down'] in g_normal_key_string_set) \
        and(data['mouse_scroll_down'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_scroll_down=data['mouse_scroll_down']
        shortcut_normal_key_set.add(config.Shortcut.mouse_scroll_down)
    else:
        print('[config failed]:mouse_scroll_down')
        return False

    if 'mouse_scroll_up' in data \
        and(isinstance(data['mouse_scroll_up'],str)) \
        and(data['mouse_scroll_up'] in g_normal_key_string_set) \
        and(data['mouse_scroll_up'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_scroll_up=data['mouse_scroll_up']
        shortcut_normal_key_set.add(config.Shortcut.mouse_scroll_up)
    else:
        print('[config failed]:mouse_scroll_up')
        return False

    if 'mouse_distance_double' in data \
        and(isinstance(data['mouse_distance_double'],str)) \
        and(data['mouse_distance_double'] in g_normal_key_string_set) \
        and(data['mouse_distance_double'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_distance_double=data['mouse_distance_double']
        shortcut_normal_key_set.add(config.Shortcut.mouse_distance_double)
    else:
        print('[config failed]:mouse_distance_double')
        return False

    if 'mouse_distance_halve' in data \
        and(isinstance(data['mouse_distance_halve'],str)) \
        and(data['mouse_distance_halve'] in g_normal_key_string_set) \
        and(data['mouse_distance_halve'] not in shortcut_normal_key_set):
        config.Shortcut.mouse_distance_halve=data['mouse_distance_halve']
        shortcut_normal_key_set.add(config.Shortcut.mouse_distance_halve)
    else:
        print('[config failed]:mouse_distance_halve')
        return False

    if 'app_pause' in data \
        and(isinstance(data['app_pause'],str)) \
        and(data['app_pause'] in g_normal_key_string_set) \
        and(data['app_pause'] not in shortcut_normal_key_set):
        config.Shortcut.app_pause=data['app_pause']
        shortcut_normal_key_set.add(config.Shortcut.app_pause)
    else:
        print('[config failed]:app_pause')
        return False

    if 'app_restart' in data \
        and(isinstance(data['app_restart'],str)) \
        and(data['app_restart'] in g_normal_key_string_set) \
        and(data['app_restart'] not in shortcut_normal_key_set):
        config.Shortcut.app_restart=data['app_restart']
        shortcut_normal_key_set.add(config.Shortcut.app_restart)
    else:
        print('[config failed]:app_restart')
        return False

    if 'app_close' in data \
        and(isinstance(data['app_close'],str)) \
        and(data['app_close'] in g_normal_key_string_set) \
        and(data['app_close'] not in shortcut_normal_key_set):
        config.Shortcut.app_close=data['app_close']
        shortcut_normal_key_set.add(config.Shortcut.app_close)
    else:
        print('[config failed]:app_close')
        return False

    return True
