import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QSlider
from PyQt5.uic import loadUi

g = "off"
class Garage(QDialog):
    def __init__(self):
        super(Garage,self).__init__()
        loadUi('Garage.ui',self)
        self.setWindowTitle('Nappali')
        self.button_control()
        
    def button_control(self):
        self.garagebtn.clicked.connect(self.garage)
        self.pushButton.clicked.connect(self.vissza)
    def garage(self):
        global g
        if(g == "off"):
            self.garagebtn.setText("Nyitva")
            g = "on"
        else:
            self.garagebtn.setText("Zárva")
            g = "off"
        
        
        
    def vissza(self):
        self.close()