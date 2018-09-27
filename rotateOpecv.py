# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:19:32 2018

@author: ME DELL'
"""

import cv2
import numpy as np

img = cv2.imread('ict.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()