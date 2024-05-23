# -*- coding: utf-8 -*-
import pynput
import pyautogui
from ktm import config

class Mouse:
    move_distance_=0
    wheel_distance_=0

    @staticmethod
    def init():
        Mouse.move_distance_=config.Constant.mouse_init_move_distance
        Mouse.wheel_distance_=config.Constant.mouse_init_wheel_distance

    @staticmethod
    def _move(dx,dy):
        mouse=pynput.mouse.Controller()
        mouse.move(dx,dy)

    @staticmethod
    def move_up():
        Mouse._move(0,-Mouse.move_distance_)

    @staticmethod
    def move_down():
        Mouse._move(0,Mouse.move_distance_)

    @staticmethod
    def move_left():
        Mouse._move(-Mouse.move_distance_,0)

    @staticmethod
    def move_right():
        Mouse._move(Mouse.move_distance_,0)

    @staticmethod
    def left_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.left)

    @staticmethod
    def left_double_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.left,2)

    @staticmethod
    def left_down():
        mouse=pynput.mouse.Controller()

    @staticmethod
    def left_up():
        mouse=pynput.mouse.Controller()
        mouse.release(pynput.mouse.Button.left)
        mouse.press(pynput.mouse.Button.left)

    @staticmethod
    def right_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.right)

    @staticmethod
    def right_double_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.right,2)

    @staticmethod
    def right_down():
        mouse=pynput.mouse.Controller()
        mouse.press(pynput.mouse.Button.right)

    @staticmethod
    def right_up():
        mouse=pynput.mouse.Controller()
        mouse.release(pynput.mouse.Button.right)

    @staticmethod
    def middle_click():
        pyautogui.click(button='middle')

    @staticmethod
    def middle_double_click():
        pyautogui.doubleClick(button='middle')

    @staticmethod
    def middle_down():
        mouse=pynput.mouse.Controller()
        mouse.press(pynput.mouse.Button.middle)

    @staticmethod
    def middle_up():
        mouse=pynput.mouse.Controller()
        mouse.release(pynput.mouse.Button.middle)

    @staticmethod
    def wheel_up():
        mouse=pynput.mouse.Controller()
        mouse.scroll(0,Mouse.wheel_distance_)

    @staticmethod
    def wheel_down():
        mouse=pynput.mouse.Controller()
        mouse.scroll(0,-Mouse.wheel_distance_)

    @staticmethod
    def distance_double():
        Mouse.move_distance_=Mouse.move_distance_*2
        Mouse.wheel_distance_=Mouse.wheel_distance_*2

    @staticmethod
    def distance_halve():
        if Mouse.move_distance_>1:
            Mouse.move_distance_=int(Mouse.move_distance_/2)

        if Mouse.wheel_distance_>1:
            Mouse.wheel_distance_=int(Mouse.wheel_distance_/2)
