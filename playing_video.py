# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:51:05 2018

@author: ME DELL'
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('038 Algorithm Analysis and Big O Section Overview.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()