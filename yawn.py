# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yawn.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import cv2
import dlib
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import json
import pyttsx3 
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 609)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 160, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 350, 111, 51))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(400, 350, 91, 51))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        self.menuOPTION = QtWidgets.QMenu(self.menubar)
        self.menuOPTION.setObjectName("menuOPTION")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHOME = QtWidgets.QAction(MainWindow)
        self.actionHOME.setObjectName("actionHOME")
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.actionYAWN_DETECTION = QtWidgets.QAction(MainWindow)
        self.actionYAWN_DETECTION.setObjectName("actionYAWN_DETECTION")
        self.menuOPTION.addAction(self.actionHOME)
        self.menuOPTION.addAction(self.actionEXIT)
        self.menuMENU.addAction(self.actionYAWN_DETECTION)
        self.menubar.addAction(self.menuOPTION.menuAction())
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DETECT YAWN"))
        self.label.setText(_translate("MainWindow", "      TOTAL YAWNS"))
        self.menuOPTION.setTitle(_translate("MainWindow", "OPTION"))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.actionHOME.setText(_translate("MainWindow", "HOME"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))
        self.actionYAWN_DETECTION.setText(_translate("MainWindow", "YAWN DETECTION "))
        self.actionHOME.triggered.connect(self.home)
        self.actionEXIT.triggered.connect(self.end)
        self.pushButton.clicked.connect(self.DetectYawn)
        self.actionYAWN_DETECTION.triggered.connect(self.ShowYawnDetection)
   
    def home(self):
        self.frame.show()
   
    def end(self):
        sys.exit()      
   
    def ShowYawnDetection(self):
        self.frame.show()
    
    def DetectYawn(self):
        engine = pyttsx3.init('sapi5') 
        PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
        predictor = dlib.shape_predictor(PREDICTOR_PATH)
        detector = dlib.get_frontal_face_detector()


        def get_landmarks(im):
            rects = detector(im, 1)
        
            if len(rects) > 1:
                return "error"
            if len(rects) == 0:
                return "error"
            return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])


        def annotate_landmarks(im, landmarks):
            im = im.copy()
            for idx, point in enumerate(landmarks):
                pos = (point[0, 0], point[0, 1])
                cv2.putText(im, str(idx), pos,
                            fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                            fontScale=0.4,
                            color=(0, 0, 255))
                cv2.circle(im, pos, 3, color=(0, 255, 255))
            return im

        def top_lip(landmarks):
            top_lip_pts = []
            for i in range(50,53):
                top_lip_pts.append(landmarks[i])
            for i in range(61,64):
                top_lip_pts.append(landmarks[i])
            top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
            top_lip_mean = np.mean(top_lip_pts, axis=0)
            return int(top_lip_mean[:,1])

        def bottom_lip(landmarks):
            bottom_lip_pts = []
            for i in range(65,68):
                bottom_lip_pts.append(landmarks[i])
            for i in range(56,59):
                bottom_lip_pts.append(landmarks[i])
            bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
            bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
            return int(bottom_lip_mean[:,1])

        def mouth_open(image):
            landmarks = get_landmarks(image)
            
            if landmarks == "error":
                return image, 0
            
            image_with_landmarks = annotate_landmarks(image, landmarks)
            top_lip_center = top_lip(landmarks)
            bottom_lip_center = bottom_lip(landmarks)
            lip_distance = abs(top_lip_center - bottom_lip_center)
            return image_with_landmarks, lip_distance

        cap = cv2.VideoCapture(0)
        yawns = 0
        yawn_status = False 

        while True:
            ret, frame = cap.read()   
            image_landmarks, lip_distance = mouth_open(frame)
            
            prev_yawn_status = yawn_status  
            
            if lip_distance > 20:
                yawn_status = True 
                
                cv2.putText(frame, "Subject is Yawning", (50,450), 
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                
        
                output_text = " Yawn Count: " + str(yawns + 1)
        
                cv2.putText(frame, output_text, (50,50),
                            cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                
            else:
                yawn_status = False 
                 
            if prev_yawn_status == True and yawn_status == False:
                yawns += 1
        
            cv2.imshow('Live Landmarks', image_landmarks )
            cv2.imshow('Yawn Detection', frame )
            
            if cv2.waitKey(33) == ord('a'):
                break
                
        cap.release()
        cv2.destroyAllWindows() 
        self.textEdit.setText(str(yawns))
        mytext = "Total Yawns: "+ str(yawns)
        engine.say(mytext) 
        engine.runAndWait() 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

