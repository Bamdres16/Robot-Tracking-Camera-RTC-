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
        self.width = 1920
        self.height = 1080
        self.fps = 20.0
        self.setConfiguration()
        self.comboQuality.currentTextChanged.connect(self.onChangeOption)
        
        
    def setConfiguration(self):
        jsonData = getAtributes("configuracion.json")
        keys = list(jsonData["calidades"].keys())
        self.comboQuality.addItems(keys)
        defaultQuality = jsonData["calidadDefecto"]
        self.comboQuality.setCurrentText(defaultQuality)
        values = jsonData["calidades"][defaultQuality]
        self.width = values[0]
        self.height = values[1]
    
    def onChangeOption(self):
        text = self.comboQuality.currentText()
        jsonData = getAtributes("configuracion.json")
        jsonData["calidadDefecto"] = text
        setConfiguration(jsonData)
        defaultQuality = jsonData["calidadDefecto"]
        values = jsonData["calidades"][defaultQuality]
        self.width = values[0]
        self.height = values[1]
         
    def setPreviews(self):
        index = 0
        for i in self.camerasAvailable:
            image = "img_" + str(i) + ".jpg"
            takePicture(i, rootPreviews + image)
            self.previewSrcAvailable[index].setPixmap(QtGui.QPixmap(rootPreviews + image))
            index += 1 
    
    def startRecording (self):
        self.progressBar.setValue(0)
        filePath = self.lineEdit.text()
        jsonData = getAtributes(filePath)
        studentName = jsonData["student"].replace(" ", "-")
        institution =  jsonData["institution"].replace(" ", "-")
        teacher = jsonData["teacher"].replace(" ", "-")
        algorithmName = jsonData["algorithmName"].replace(" ", "-")
        fileVideoName = studentName + "_" + institution + "_" + teacher
        code = jsonData["code"]
        cameras = code["cameras"]
        duration = code["duration"]
        if not os.path.exists("Videos/" + fileVideoName):
            os.makedirs("Videos/" + fileVideoName)
        lenFolders = len([n for n in os.listdir("Videos/" + fileVideoName) if algorithmName in n])
        folderName = algorithmName + "_" + str(lenFolders)
        currentVideo = 0
        totalVideos = len(cameras) + 2
        for camID, durationCam in zip(cameras, duration):
            recordVideo(fileVideoName, folderName, self.camerasAvailable[camID], durationCam)
            currentVideo += 1
            self.progressBar.setValue((currentVideo / totalVideos) * 100)
            
        generateVideo(fileVideoName, folderName, "o")
        currentVideo += 1
        self.progressBar.setValue((currentVideo / totalVideos) * 100)
        generateVideo(fileVideoName, folderName, "s", self.width, self.height, self.fps)
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
