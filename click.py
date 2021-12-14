import pyautogui as auto
import win32api
import time

state = win32api.GetKeyState(0x01)
while True:
    left = win32api.GetKeyState(0x01)
    if left != state:
        state = left
        print(left)
        if left < 0:
            print("press")
            print(auto.position())
        else:
            print("release")
    time.sleep(0.01)

