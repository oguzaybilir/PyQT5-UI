# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/oguza/Documents/GitHub/userInterface/PyQT5-UI/yolov4_predict/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weightline = QtWidgets.QLineEdit(self.centralwidget)
        self.weightline.setGeometry(QtCore.QRect(120, 870, 581, 22))
        self.weightline.setObjectName("weightline")
        self.cfgButton = QtWidgets.QPushButton(self.centralwidget)
        self.cfgButton.setGeometry(QtCore.QRect(10, 830, 101, 28))
        self.cfgButton.setObjectName("cfgButton")
        self.weightButton = QtWidgets.QPushButton(self.centralwidget)
        self.weightButton.setGeometry(QtCore.QRect(10, 870, 101, 28))
        self.weightButton.setObjectName("weightButton")
        self.cfgline = QtWidgets.QLineEdit(self.centralwidget)
        self.cfgline.setGeometry(QtCore.QRect(120, 830, 581, 22))
        self.cfgline.setObjectName("cfgline")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.label.setObjectName("label")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(10, 910, 101, 28))
        self.imageButton.setObjectName("imageButton")
        self.imageline = QtWidgets.QLineEdit(self.centralwidget)
        self.imageline.setGeometry(QtCore.QRect(120, 910, 581, 22))
        self.imageline.setObjectName("imageline")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(710, 830, 131, 41))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(710, 890, 131, 41))
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cfgButton.setText(_translate("MainWindow", ".cfg dosyası ara"))
        self.weightButton.setText(_translate("MainWindow", ".weights dosyası ara"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.imageButton.setText(_translate("MainWindow", "Test Görüntüleri"))
        self.startButton.setText(_translate("MainWindow", "Başlat"))
        self.stopButton.setText(_translate("MainWindow", "Durdur"))

