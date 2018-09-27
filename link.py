from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import sys
import numpy as np

def prediction(a):
    model = load_model('my_model.h5')
    p= model.predict_classes(a)
    return p

def loadimage():
    images = np.zeros((1,784))

    i = 0
    for no in [5]:
        # read the image
        gray = cv2.imread("test_image.png", 0)

        # resize the images and invert it (black background)
        gray = cv2.resize(255-gray, (28, 28))
        #(thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # save the processed images
        cv2.imwrite("image_"+str(no)+".png", gray)

        flat = gray.flatten() / 255.0

        images[i] = flat

        images = images.reshape(images.shape[0], 1, 28, 28).astype('float32')


    y = prediction(images)
    return y


