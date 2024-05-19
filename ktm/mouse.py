# -*- coding: utf-8 -*-
import pynput

class Mouse:
    current_dpixel_=32

    @staticmethod
    def current_position():
        mouse=pynput.mouse.Controller()
        x,y=mouse.position
        return x,y

    @staticmethod
    def current_dpixel():
        return Mouse.current_dpixel_

    @staticmethod
    def left_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.left)

    @staticmethod
    def right_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.right)

    @staticmethod
    def left_double_click():
        mouse=pynput.mouse.Controller()
        mouse.click(pynput.mouse.Button.left,2)

    @staticmethod
    def left_down():
        mouse=pynput.mouse.Controller()
        mouse.press(pynput.mouse.Button.left)

    @staticmethod
    def right_down():
        mouse=pynput.mouse.Controller()
        mouse.press(pynput.mouse.Button.right)

    @staticmethod
    def left_up():
        mouse=pynput.mouse.Controller()
        mouse.release(pynput.mouse.Button.left)

    @staticmethod
    def right_up():
        mouse=pynput.mouse.Controller()
        mouse.release(pynput.mouse.Button.right)

    @staticmethod
    def _move(dx,dy):
        mouse=pynput.mouse.Controller()
        mouse.move(dx,dy)

    @staticmethod
    def move_up():
        Mouse._move(0,-Mouse.current_dpixel_)

    @staticmethod
    def move_down():
        Mouse._move(0,Mouse.current_dpixel_)

    @staticmethod
    def move_left():
        Mouse._move(-Mouse.current_dpixel_,0)

    @staticmethod
    def move_right():
        Mouse._move(Mouse.current_dpixel_,0)

    @staticmethod
    def dpixel_double():
        Mouse.current_dpixel_=Mouse.current_dpixel_*2

    @staticmethod
    def dpixel_halve():
        if Mouse.current_dpixel_>1:
            Mouse.current_dpixel_=int(Mouse.current_dpixel_/2)

    @staticmethod
    def wheel_up():
        mouse=pynput.mouse.Controller()
        mouse.scroll(0,Mouse.current_dpixel_)

    @staticmethod
    def wheel_down():
        mouse=pynput.mouse.Controller()
        mouse.scroll(0,-Mouse.current_dpixel_)
