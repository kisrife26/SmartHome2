import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QSlider
from PyQt5.uic import loadUi

lo = "off"
l = "off"
class Garden(QDialog):
    def __init__(self):
        super(Garden,self).__init__()
        loadUi('Garden.ui',self)
        self.setWindowTitle('Udvar')
        self.button_control()
        
    def button_control(self):
        self.lampbtn.clicked.connect(self.lamp)
        self.locsolo.clicked.connect(self.locs)
        self.pushButton.clicked.connect(self.vissza)
        
    def lamp(self):
        global l
        if(l == "off"):
            self.lampbtn.setText("ON")
            l = "on"
        else:
            self.lampbtn.setText("OFF")
            l = "off"
    def locs(self):
        global lo
        if(lo == "off"):
            self.locsolo.setText("ON")
            lo = "on"
        else:
            self.locsolo.setText("OFF")
            lo = "off"
        
    def vissza(self):
        self.close()