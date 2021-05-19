from rtc_ui import *
import time
from grabacion.cameraRecord import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
            QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.camerasAvailable = checkCameras()
            self.camerasUsed = []
            # Añadir función a botón
            #self.pushButton.clicked.connect(self.changeProgress)
            self.comboBox.addItems(self.camerasAvailable)
            self.comboBox.currentIndexChanged.connect(self.selectCamera)
            self.btnSrc1.clicked.connect(self.checkPath)

    def selectCamera(self, i):
        
        takePreviewImage(int(self.camerasAvailable[i]), "img_0.jpg")
        
        
    def checkPath(self):
        image_path = "img_0.jpg"
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)
        
      
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
