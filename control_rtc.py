from rtc_ui import *
import time
from grabacion.cameraRecord import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys

rootPreviews = "Previews/"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setPreviews()
        #self.pushButton.clicked.connect(self.changeProgress)
            
    def setPreviews(self):
        takePicture(0, rootPreviews + "img_0.jpg")
        takePicture(2, rootPreviews + "img_1.jpg")
        takePicture(4, rootPreviews + "img_2.jpg")
        self.previewSrc1.setPixmap(QtGui.QPixmap(rootPreviews + "img_0.jpg"))
        self.previewSrc2.setPixmap(QtGui.QPixmap(rootPreviews + "img_1.jpg"))
        self.previewSrc3.setPixmap(QtGui.QPixmap(rootPreviews + "img_2.jpg"))

        
        
    def getKeysAvailable(self):
        cameraKeys = []
        for i in self.camerasAvailable.keys():
            if self.camerasAvailable[i] == True:
                cameraKeys.append(i)
        return cameraKeys
    
    def toggleStateCamera(self, key):
        current = self.camerasAvailable[key]
        self.camerasAvailable[key] = not current
        
    ''' def checkPath(self):
        image_path = "img_0.jpg"
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene) '''
        
      
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
