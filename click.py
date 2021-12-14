import pyautogui as auto
import win32api
import time
import csv

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    dataset = []
    j = 1
    state = win32api.GetKeyState(0x01)
    while True:
        position = [j]
        for i in range(3):
            left = win32api.GetKeyState(0x01)
            if left != state:
                state = left
                if left < 0:
                    print("press")
                    position.append(auto.position())
            else:
                continue
            time.sleep(0.1)
        writer.writerow(position)
        j += 1
