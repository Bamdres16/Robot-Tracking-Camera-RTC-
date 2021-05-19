from rtc_ui import *
import time
#from grabacion.cameraRecord import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
            QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
            self.setupUi(self)
            self.camerasAvailable = {"0": True, "2": True, "3":True}
            #self.pushButton.clicked.connect(self.changeProgress)
            
            self.updateCombos()
            
            # Buttons events
            self.btnSrc1.clicked.connect(self.selectSource1)
            self.btnSrc2.clicked.connect(self.selectSource2)
            self.btnSrc3.clicked.connect(self.selectSource3)
            self.btnSrc4.clicked.connect(self.selectSourceExtra)


    def selectSource1(self, i):
        self.toggleStateCamera()
        #self.graphicsView
        #takePreviewImage(int(self.camerasAvailable[i]), "img_0.jpg")
        print("Ok 1")
    
    def selectSource2(self, i):
        #self.graphicsView_3
        #takePreviewImage(int(self.camerasAvailable[i]), "img_0.jpg")
        print("Ok 2")
        
    def selectSource3(self, i):
        #self.graphicsView_2
        #takePreviewImage(int(self.camerasAvailable[i]), "img_0.jpg")
        print("Ok 3")
        
    def selectSourceExtra(self, i):
        #self.graphicsView_4
        #takePreviewImage(int(self.camerasAvailable[i]), "img_0.jpg")
        print("Ok 4")
        
    def updateCombos(self):
        cameraKeys = self.getKeysAvailable()
        self.comboSrc1.addItems(cameraKeys)
        self.comboSrc2.addItems(cameraKeys)
        self.comboSrc3.addItems(cameraKeys)
        self.comboSrc4.addItems(cameraKeys)
    
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
