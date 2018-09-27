import cv2
import link
def enter1():
    ramp_frames = 28
    cap = cv2.VideoCapture(0)

    def takepicture():
        camera_capture = gray
        a = cv2.imwrite("test_image.png", camera_capture)
        return a

    while (True):
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 28)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 28)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    pic = takepicture()
    cap.release()


def enter():

     p = link.loadimage()
     label = Label(master,text=p).pack()
     return


from tkinter import *

master = Tk()
button1 = Button(master,text='Take a picture',bg='red',command=enter1)
button1.pack()
button2 = Button(master,text='Predict',bg='red',command=enter)
button2.pack()
mainloop()

