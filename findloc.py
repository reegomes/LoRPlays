import cv2 as cv
import numpy as np
import pyautogui
import os
from windowcapture import WindowCapture
from vision import Vision

class FindLoc:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    wincap = WindowCapture('Legends of Runeterra')
    #vision_IP = Vision('img\minalegal.jpg')
    
    haystack_img = cv.imread('img\este1.jpg', cv.IMREAD_UNCHANGED)
    needle_img = cv.imread('img\crimsondisciple.jpg', cv.IMREAD_UNCHANGED)

    result = cv.matchTemplate(wincap.get_screenshot(), needle_img, cv.TM_CCOEFF_NORMED)
    
    #cv.imshow('Result', result)
    #cv.waitKey()

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print('Best match top left position: %s' % str(max_loc))
    print('Best match confidence: %s' % max_val)
    print('ScreenPosition: %s' % str(wincap.get_screen_position(max_loc)))
    
    threshold = 0.5
    if max_val >= threshold:
        print('Found button.')

        # pega as dimensões da imagem pequena
        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1], needle_h)

        #cv.rectangle(needle_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        # cv.drawMarker(needle_img, max_loc, (255,255,0), markerType=None, markerSize=None, thickness=None, line_type=None)
        # cv.circle(needle_img, max_loc, 5, color=(255,255,0), thickness=2, lineType=cv.LINE_4, shift=None)

        #cv.imshow('Result', haystack_img)
        #cv.waitKey()

        # Aqui é onde o programa captura a imagem e vai
        # pyautogui.click(top_left, clicks=1, interval=1, duration=0.1);

        # Start()
        # Replace("4 2 3 1")
    else:
        print('Image not found.')