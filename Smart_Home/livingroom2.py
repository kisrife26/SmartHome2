import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QSlider
from PyQt5.uic import loadUi

r = "off"
f = "off"
h = "off"
l = "off"
class Livingroom2(QDialog):
    def __init__(self):
        super(Livingroom2,self).__init__()
        loadUi('livingroom2.ui',self)
        self.setWindowTitle('Nappali')
        self.button_control()
        
    def button_control(self):
        self.redony.clicked.connect(self.shutter)
        self.fut.clicked.connect(self.hot)
        self.hut.clicked.connect(self.cooler)
        self.lamp.clicked.connect(self.livlamp)
        self.pushButton.clicked.connect(self.vissza)
        
    def shutter(self):
        global r
        if(r == "on"):
            print("on")
            self.redony.setText("OFF")
            r = "off"
        else:
            print("off")
            self.redony.setText("ON")
            r = "on"
            
    def hot(self):
        global f
        if(f == "on"):
            print("on")
            self.fut.setText("OFF")
            f = "off"
        else:
            print("off")
            self.fut.setText("ON")
            f = "on"
            
    def cooler(self):
        global h
        if(h == "on"):
            print("on")
            self.hut.setText("OFF")
            h = "off"
        else:
            print("off")
            self.hut.setText("ON")
            h = "on"
    
    def livlamp(self):
        global l
        if(l == "on"):
            print("on")
            self.lamp.setText("OFF")
            l = "off"
        else:
            print("off")
            self.lamp.setText("ON")
            l = "on"
    def vissza(self):
        self.close()
