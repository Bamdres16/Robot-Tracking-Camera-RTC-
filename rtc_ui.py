# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rtc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 641, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.previewSrc1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.previewSrc1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewSrc1.sizePolicy().hasHeightForWidth())
        self.previewSrc1.setSizePolicy(sizePolicy)
        self.previewSrc1.setText("")
        self.previewSrc1.setPixmap(QtGui.QPixmap("nodisponible.png"))
        self.previewSrc1.setScaledContents(True)
        self.previewSrc1.setObjectName("previewSrc1")
        self.gridLayout.addWidget(self.previewSrc1, 1, 0, 1, 1)
        self.previewSrc4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.previewSrc4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewSrc4.sizePolicy().hasHeightForWidth())
        self.previewSrc4.setSizePolicy(sizePolicy)
        self.previewSrc4.setText("")
        self.previewSrc4.setPixmap(QtGui.QPixmap("nodisponible.png"))
        self.previewSrc4.setScaledContents(True)
        self.previewSrc4.setObjectName("previewSrc4")
        self.gridLayout.addWidget(self.previewSrc4, 3, 1, 1, 1)
        self.previewSrc2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.previewSrc2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewSrc2.sizePolicy().hasHeightForWidth())
        self.previewSrc2.setSizePolicy(sizePolicy)
        self.previewSrc2.setText("")
        self.previewSrc2.setPixmap(QtGui.QPixmap("nodisponible.png"))
        self.previewSrc2.setScaledContents(True)
        self.previewSrc2.setObjectName("previewSrc2")
        self.gridLayout.addWidget(self.previewSrc2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.previewSrc3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.previewSrc3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewSrc3.sizePolicy().hasHeightForWidth())
        self.previewSrc3.setSizePolicy(sizePolicy)
        self.previewSrc3.setText("")
        self.previewSrc3.setPixmap(QtGui.QPixmap("nodisponible.png"))
        self.previewSrc3.setScaledContents(True)
        self.previewSrc3.setObjectName("previewSrc3")
        self.gridLayout.addWidget(self.previewSrc3, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 10, 181, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.searchBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchBtn.setObjectName("searchBtn")
        self.verticalLayout_3.addWidget(self.searchBtn)
        self.errorLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.errorLabel.setEnabled(True)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_3.addWidget(self.errorLabel)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.comboQuality = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboQuality.setObjectName("comboQuality")
        self.verticalLayout_3.addWidget(self.comboQuality)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.fpsSB = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.fpsSB.setEnabled(True)
        self.fpsSB.setMinimum(1)
        self.fpsSB.setMaximum(30)
        self.fpsSB.setProperty("value", 1)
        self.fpsSB.setObjectName("fpsSB")
        self.horizontalLayout.addWidget(self.fpsSB)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.getFPSBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getFPSBtn.setObjectName("getFPSBtn")
        self.verticalLayout_3.addWidget(self.getFPSBtn)
        self.saveBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout_3.addWidget(self.saveBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.startBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setEnabled(False)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout_3.addWidget(self.startBtn)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(645, 10, 31, 521))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 641, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reloadCamerasBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reloadCamerasBtn.setObjectName("reloadCamerasBtn")
        self.horizontalLayout_2.addWidget(self.reloadCamerasBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RTC Control"))
        self.label_4.setText(_translate("MainWindow", "Cámara 2"))
        self.label_7.setText(_translate("MainWindow", "Cámara Adicional"))
        self.label_3.setText(_translate("MainWindow", "Cámara 1"))
        self.label_6.setText(_translate("MainWindow", "Cámara 3"))
        self.label.setText(_translate("MainWindow", "Código fuente"))
        self.searchBtn.setText(_translate("MainWindow", "Buscar"))
        self.errorLabel.setText(_translate("MainWindow", "Debe agregar un archivo Json válido"))
        self.label_9.setText(_translate("MainWindow", "Configuración"))
        self.label_5.setText(_translate("MainWindow", "Calidad de grabación"))
        self.label_8.setText(_translate("MainWindow", "FPS"))
        self.getFPSBtn.setText(_translate("MainWindow", "Actualizar FPS"))
        self.saveBtn.setText(_translate("MainWindow", "Guardar Cambios"))
        self.startBtn.setText(_translate("MainWindow", "Iniciar"))
        self.label_2.setText(_translate("MainWindow", "Progreso"))
        self.reloadCamerasBtn.setText(_translate("MainWindow", "Actualizar cámaras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

