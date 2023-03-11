import pyautogui
import webbrowser
import time
import numpy as np


# def get_mouse_position():

#     for i in range(0, 50):
#         x1, y = pyautogui.position()
#         x2 = x1 + 10

#         for x in range(x1, x2):
#             r, g, b = pyautogui.pixel(x, y)
            


def main():
    url = "https://chromedino.com/"
    
    webbrowser.open(url, new=0, autoraise=True)
    time.sleep(3)
    
    # space to start the game
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


    for i in range(1, 600):
        
        thresh = 200
        fn = lambda x : 255 if x > thresh else 0
  
        im1 = pyautogui.screenshot(region=(351,200, 695, 150)).convert('L').point(fn, mode='1')
        # dino position: 109 124   rgb = 247, 247, 247

        # obj = im1.crop(box=(181, 92, 282, 140))
        # obj = im1.crop(box=(163, 93, 277, 148)) # 6100    
        # obj = im1.crop(box=(137, 93, 277,  148)) # 7520 best score 491
        # obj = im1.crop(box=(163, 93, 287,  148)) #  6650
        # obj = im1.crop(box=(163, 93, 270,  148)) #  5700 best score 504
        obj = im1.crop(box=(153, 93, 270,  148)) #  6270  best score 323
        # obj = im1.crop(box=(154, 93, 277, 148)) # 6600
        # obj = im1.crop(box=(157, 87, 265,147)) # 6300
        
        
        # obj.save(f'obj_{np.asarray(obj, dtype="int32").sum()}.png')

        if np.asarray(obj, dtype="int32").sum() < 6270    :
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
        
main()
# get_mouse_position()

