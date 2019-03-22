# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvO.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from watson_developer_cloud import VisualRecognitionV3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
visual_recognition = VisualRecognitionV3(version='{version}',iam_apikey='{apikey}')
import json
import os
from watson_developer_cloud import VisualRecognitionV3
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='Enter_your_apikey')

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 160, 411, 251))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(210, 160, 301, 211))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(220, 40, 261, 71))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(430, 430, 341, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 430, 351, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        self.menuWhichFruit = QtWidgets.QMenu(self.menubar)
        self.menuWhichFruit.setObjectName("menuWhichFruit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHOME = QtWidgets.QAction(MainWindow)
        self.actionHOME.setObjectName("actionHOME")
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")
        self.actionApples_vs_Oranges = QtWidgets.QAction(MainWindow)
        self.actionApples_vs_Oranges.setObjectName("actionApples_vs_Oranges")
        self.menuMENU.addAction(self.actionHOME)
        self.menuMENU.addAction(self.actionEXIT)
        self.menuWhichFruit.addAction(self.actionApples_vs_Oranges)
        self.menubar.addAction(self.menuMENU.menuAction())
        self.menubar.addAction(self.menuWhichFruit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "imagelabel"))
        self.label_2.setText(_translate("MainWindow", "INPUT IMAGE"))
        self.pushButton.setText(_translate("MainWindow", "upload image"))
        self.pushButton_2.setText(_translate("MainWindow", "Classify "))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU"))
        self.menuWhichFruit.setTitle(_translate("MainWindow", "WhichFruit"))
        self.actionHOME.setText(_translate("MainWindow", "HOME"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))
        self.actionApples_vs_Oranges.setText(_translate("MainWindow", "Apples vs Oranges"))
        self.actionHOME.triggered.connect(self.home)
        self.actionEXIT.triggered.connect(self.end)
        self.actionApples_vs_Oranges.triggered.connect(self.show_classify)
        self.pushButton.clicked.connect(self.chooseImage)
        self.pushButton_2.clicked.connect(self.classify)

    def home(self):
        self.frame.show()
        self.frame_2.hide()
    def end(self):
        sys.exit()

    def show_classify(self):
        self.frame_2.show()
        self.frame.show()
    def chooseImage(self):
        location = QtWidgets.QFileDialog.getOpenFileName(self,'Select File')
        loc = location[0]
        self.filePath = os.path.normpath(loc)
        
        self.ict = QtGui.QPixmap(self.filePath)
        self.ict = self.ict.scaled(self.label_2.width(),self.label_2.height())
        self.label_2.setPixmap(self.ict)
    def classify(self):
        with open(self.filePath, 'rb') as images_file:
            classes = visual_recognition.classify(images_file,threshold='0.6',classifier_ids='ApplesvsOranges_172328479').get_result()
            df = pd.DataFrame(classes)
            print(df)
            self.textEdit.setText(json.dumps(classes["images"][0]["classifiers"][0]["classes"][0]["class"],indent = 2))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

