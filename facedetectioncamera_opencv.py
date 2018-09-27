# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:30:03 2018

@author: ME DELL'
"""

import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    if ret:
        gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(gray)
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        if cv2.waitKey(2) ==27:
            break
        cv2.imshow('result',img)
    else:
        print('some error')
cv2.destroyAllWindows()
cap.release()    