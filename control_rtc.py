from rtc_ui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from grabacion.cameraRecord import *
from Herramientas.compileJson import *
import os

rootPreviews = "Previews/"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.camerasAvailable = checkCameras()
        self.previewSrcAvailable = [self.previewSrc1, self.previewSrc2, self.previewSrc3, self.previewSrc4]
        self.setPreviews()
        self.lineEdit.textChanged.connect(self.isReadyToStart)
        self.searchBtn.clicked.connect(self.open)
        self.startBtn.clicked.connect(self.startRecording)
        self.startBtnState = False
        self.errorLabel.setVisible(False)
        
        
            
    def setPreviews(self):
        index = 0
        print(self.camerasAvailable)
        for i in self.camerasAvailable:
            image = "img_" + str(i) + ".jpg"
            takePicture(i, rootPreviews + image)
            self.previewSrcAvailable[index].setPixmap(QtGui.QPixmap(rootPreviews + image))
            index += 1 
    
    def startRecording (self):
        
        filePath = self.lineEdit.text()
        jsonData = getAtributes(filePath)
        studentName = jsonData["student"].replace(" ", "-")
        institution =  jsonData["institution"].replace(" ", "-")
        teacher = jsonData["teacher"].replace(" ", "-")
        fileVideoName = studentName + "_" + institution + "_" + teacher
        code = jsonData["code"]
        cameras = code["cameras"]
        duration = code["duration"]
        folder = ""
        currentVideo = 0
        totalVideos = len(cameras) + 1
        for camID, durationCam in zip(cameras, duration):
            folder = recordVideo(fileVideoName, camID, durationCam)
            self.progressBar.setValue((currentVideo / totalVideos) * 100)
            currentVideo += 1
        
        generateVideo(fileVideoName + "/" + folder)
        currentVideo += 1
        self.progressBar.setValue((currentVideo / totalVideos) * 100)
        
        
    def isReadyToStart (self):
        text = self.lineEdit.text()
        pathExists = os.path.exists(text)
        
        if (pathExists and (text[-5:] == ".json")):
            self.errorLabel.setVisible(False)
            self.startBtn.setEnabled(True)
            self.cbCode.setCheckState(True)
        elif(not pathExists):
            self.errorLabel.setText("Debe elegir un archivo existente")
            self.errorLabel.setVisible(True)
            self.startBtn.setEnabled(False)
            self.cbCode.setCheckState(False)
        elif (text[-5:] != ".json"):
            self.errorLabel.setText("Debe elegir un archivo json válido")
            self.errorLabel.setVisible(True)
            self.startBtn.setEnabled(False)
            self.cbCode.setCheckState(False)
            
        
            
        
            
    def open(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.lineEdit.setText(fileName[0])
        
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
