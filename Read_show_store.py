# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:18:51 2018

@author: ME DELL'
"""

"""Use the function cv2.imread() to read an image. The image should be in the
 working directory or a full path of image should be given.

Second argument is a flag which specifies the way image should be read.

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be
                         neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel"""

"""Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively."""

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('ict.jpg',0)

"""se the function cv2.imshow() to display an image in a window. 
The window automatically fits to the image size.

First argument is a window name which is a string. second argument is our image.
 You can create as many windows as you wish, but with different window names."""

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""Use the function cv2.imwrite() to save an image.

First argument is the file name, second argument is the image you want to save."""

cv2.imwrite('ict1.png',img)






