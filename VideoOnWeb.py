# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:29:19 2018

@author: ME DELL'
"""

def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()