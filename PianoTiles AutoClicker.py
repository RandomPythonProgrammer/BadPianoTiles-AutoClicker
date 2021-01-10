import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):
    if pyautogui.pixelMatchesColor(50, 450, (0, 0, 0)):
        click(50, 450)

    if pyautogui.pixelMatchesColor(150, 450, (0, 0, 0)):
        click(150, 450)

    if pyautogui.pixelMatchesColor(250, 450, (0, 0, 0)):
        click(250, 450)

    if pyautogui.pixelMatchesColor(350, 450, (0, 0, 0)):
        click(350, 450)
