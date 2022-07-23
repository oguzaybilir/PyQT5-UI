from PyQt5.QtWidgets import*
from design_python import Ui_HSV
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import cv2
import numpy as np
import sys

class trackbarcode(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_HSV()
        self.ui.setupUi(self)

        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)

        self.lower_1 = 0
        self.lower_2 = 0
        self.lower_3 = 0
        self.upper_1 = 180
        self.upper_2 = 255
        self.upper_3 = 255
        self.a = 0

    def lower_h_func(self,lower_1): 
        self.lower_1 = lower_1

    def lower_s_func(self,lower_2):
        self.lower_2 = lower_2

    def lower_v_func(self,lower_3): 
        self.lower_3 = lower_3

    def upper_h_func(self,upper_1):
        self.upper_1 = upper_1

    def upper_s_func(self,upper_2): 
        self.upper_2 = upper_2
        
    def upper_v_func(self,upper_3): 
        self.upper_3 = upper_3

    def open_camera(self):

        print("kamera açıldı")

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, frame = cap.read()

            if ret is True:

                img = cv2.flip(frame, 1)
                img_copy = frame.copy()
                
                img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                img_original = cv2.resize(img_copy,(280,280))
                img_copy = cv2.resize(img_copy,(280,280))

                ConvertToFormat = QImage(img_original.data, img_original.shape[1], img_original.shape[0], QImage.Format_RGB888)
                self.ui.label.setPixmap(QPixmap.fromImage(ConvertToFormat))
                self.ui.label.setScaledContents(True)
                cv2.waitKey(0)
                # ----------------------------------------------------------------------------------------------------------------------
                hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
                lower_values = (self.lower_1, self.lower_2, self.lower_3)
                upper_values = (self.upper_1, self.upper_2, self.upper_3)
                print(lower_values)
                print(upper_values)
                print(hsv.shape)

                mask = cv2.inRange(hsv, lower_values, upper_values)

                mask = cv2.dilate(mask, (5,5), iterations=7)
                mask = cv2.erode(mask, (5,5), iterations=7)
                mask_original = cv2.resize(mask,(280,280))
                
                mask_show = QImage(mask_original.data, mask_original.shape[1], mask_original.shape[0], QImage.Format_Grayscale8)
                self.ui.label_2.setPixmap(QPixmap.fromImage(mask_show))
                self.ui.label_2.setScaledContents(True)
                # ----------------------------------------------------------------------------------------------------------------------
                img_copy = cv2.resize(img_copy,(280,280))
                bwise = cv2.bitwise_and(img_copy, img_copy, mask=mask)
                bwise_org = cv2.resize(bwise,(280,280))

                bwise_show = QImage(bwise_org.data, bwise_org.shape[1], bwise_org.shape[0], QImage.Format_RGB888)
                self.ui.label_3.setPixmap(QPixmap.fromImage(bwise_show ))
                self.ui.label_3.setScaledContents(True)
                # ----------------------------------------------------------------------------------------------------------------------
                cnts,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for c in cnts:
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # ----------------------------------------------------------------------------------------------------------------------
                # img_original = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
                img_original = cv2.resize(img_copy,(280,280))

                copy_show = QImage(img_original.data, img_original.shape[1], img_original.shape[0], QImage.Format_RGB888)
                self.ui.label_4.setPixmap(QPixmap.fromImage(copy_show))
                self.ui.label_4.setScaledContents(True)
                # ----------------------------------------------------------------------------------------------------------------------
                cv2.waitKey(0)
                # ----------------------------------------------------------------------------------------------------------------------
            if ret is False:
                print("KAMERA FRAME ALAMIYOR")
                pass

    def close_camera(self):
        
        print("kapatma tuşuna basıldı")
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)
        sys.exit()

def start():
    app = QApplication(sys.argv)
    form = trackbarcode()
    form.show()
    app.exec_()

start()

