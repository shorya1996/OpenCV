# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:29:12 2018

@author: ME DELL'
"""

import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('DSC01523.jpg', cv2.COLOR_BGR2GRAY)

faces = dataset.detectMultiScale(image, 1.3)
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)
    
cv2.imwrite('result.jpg',image)