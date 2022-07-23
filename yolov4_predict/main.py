from PyQt5.QtWidgets import*
from design_python import Ui_MainWindow
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import cv2
import numpy as np
import sys
import os
from glob import glob
from prediction_ import yolov4_predict


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cfgButton.clicked.connect(self.fileBrowser)
        self.ui.weightButton.clicked.connect(self.secondfileBrowser)
        self.ui.imageButton.clicked.connect(self.thirdfileBrowser)
        self.ui.startButton.clicked.connect(self.predict)
        self.ui.stopButton.clicked.connect(self.stop)

        self.yolov4_cfg = None
        self.yolov4_weights = None
        self.images = None
        self.path = None

    def fileBrowser(self):

        fname=QFileDialog.getOpenFileName(self,
        'Open file',
        'C:/Users/oguza/Documents/GitHub/userInterface/PyQT5-UI/yolov4_predict',
        'All Types (*.cfg)')

        self.yolov4_cfg = fname[0]
        print(fname[0])

        self.ui.cfgline.setText(self.yolov4_cfg)
        
    def secondfileBrowser(self):

        fname=QFileDialog.getOpenFileName(self,
        'Open file',
        'C:/Users/oguza/Documents/GitHub/userInterface/PyQT5-UI/yolov4_predict',
        'All Types (*.weights)')

        self.yolov4_weights = fname[0]
        print(fname[0])

        self.ui.weightline.setText(self.yolov4_weights)


    def thirdfileBrowser(self):

        if self.yolov4_cfg is None:
            QMessageBox.about(self, "Hata", "Yolov4 cfg dosyası seçilmedi.")
            hata = "CFG dosyası seçilemedi, lütfen tekrar deneyiniz."
            return hata
        
        if self.yolov4_weights is None:
            QMessageBox.about(self, "Hata", "Yolov4 weights dosyası seçilmedi.")
            hata = "Weights dosyası seçilemedi, lütfen tekrar deneyiniz."
            return hata

        fname=QFileDialog.getExistingDirectory(self, "Select Directory")
    
        #dir_path=QFileDialog.getExistingDirectory(self,"Choose Directory","D:\\")

        self.images = fname[0]
        #self.dir_path = dir_path[0]
        #print(dir_path[0])
        print(fname[0])

        self.ui.imageline.setText(self.images)


        # ##### SEÇİLEN DOSYADAN DOSYA YOLU İÇERİSİNDEKİ TÜM GÖRSELLERİ AL #####
        # #self.images = glob(self.dir_path + '/*.jpg')
        # #print(self.images)

        # self.images = glob(self.images + '/*.png')
        # #self.images.extend(glob(self.images + '/*.jpg'))
        # print(self.images)


    def predict(self):

        for i in range(0,len(self.images)):

            img = cv2.imread(self.images[i])
            img, start_x, start_y, end_x, end_y, label = yolov4_predict(self.images, self.yolov4_cfg, self.yolov4_weights)
            img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            cv2.rectangle(img_copy,(start_x,start_y),(end_x,end_y),(0,0,255),3)
            cv2.putText(img_copy,label,(start_x,start_y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3) 

            img_original = cv2.resize(img_copy,(1280,720))
            img_copy = cv2.resize(img_copy,(1280,720))

            ConvertToFormat = QImage(img_original.data, img_original.shape[1], img_original.shape[0], QImage.Format_RGB888)
            self.ui.label.setPixmap(QPixmap.fromImage(ConvertToFormat))
            self.ui.label.setScaledContents(True)

    def stop():
        print("Görseldeki nesneler tespit edilmiştir.")
        sys.exit()

def start():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

start()