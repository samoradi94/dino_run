import pyautogui
import webbrowser
import time


url = "https://chromedino.com/"

webbrowser.open(url, new=0, autoraise=True)

time.sleep(3)
for i in range(1, 50):
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')