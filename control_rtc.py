from rtc_ui import *
import time
from grabacion.cameraRecord import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
            QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
            self.setupUi(self)
            # Añadir función a botón
            #self.pushButton.clicked.connect(self.changeProgress)
            
      
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()