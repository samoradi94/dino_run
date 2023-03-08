import pyautogui
import webbrowser
import time


def get_mouse_position():
    for i in range(0, 50):

        x1, y = pyautogui.position()
        x2 = x1 + 10

        for x in range(x1, x2):
            r, g, b = pyautogui.pixel(x, y)
            if r == 83 and g == 83 and b == 83:
                print('obj')

        # position: x = 1028 1045 y = 709
        # color : BG= 247 247 247     object = 83 83 83


def main():
    url = "https://chromedino.com/"

    webbrowser.open(url, new=0, autoraise=True)

    time.sleep(3)

    # space to start the game
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


    for i in range(1, 50):
        # x, y = pyautogui.position()
        # dino_x, dino_y = pyautogui.position()
        # a_x = dino_x + 200
        # a_y = dino_y
        # px = pyautogui.pixel(a_x, a_y)
        # if px.red == 83 and px.green == 83 and px.blue == 83:
        #     print('yes')
        #     pyautogui.keyDown('space')
        #     pyautogui.keyUp('space')


        # x, y = 821, 722
        # print(x,y)
        # print(pyautogui.pixel(x,y))
        #
        # if pyautogui.pixel(x + 20, y).blue == 83:
        #     pyautogui.keyDown('space')
        #     pyautogui.keyUp('space')

        dino_x = 794  #842
        dino_y = 722
        # if pyautogui.pixel(dino_x + 50, dino_y).blue == 83:
        #     print('d')
        #     pyautogui.keyDown('space')
        #     pyautogui.keyUp('space')
        # for x in range(dino_x + 300 , dino_x + 400):
        #     px = pyautogui.pixel(x  , dino_y)
        #     if px.red == 83 and px.green == 83 and px.blue == 83:
        #         print('yes')
        #         pyautogui.keyDown('space')
        #         pyautogui.keyUp('space')
        # if px.red != 247 and px.green != 247 and px.blue != 247:
        #     pyautogui.keyDown('space')
        #     pyautogui.keyUp('space')


get_mouse_position()

