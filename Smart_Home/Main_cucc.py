import sys
# import time
from os import path
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish
# import paho.mqtt.subscribe as subscribe
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUiType




FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "Smart_Home_Main.ui"))
garden = "on"

class MainApp(QMainWindow, FORM_CLASS):
    
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
##    #sys.exit(app.exec_())

if __name__ == '__main__':
    main()