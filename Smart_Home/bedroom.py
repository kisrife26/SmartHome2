import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QSlider
from PyQt5.uic import loadUi

ertek = 0
bedlamp = "off"
class Bedroom(QDialog):
    def __init__(self):
        super(Bedroom,self).__init__()
        loadUi('bedroom.ui',self)
        self.setWindowTitle('Hálószoba')
        # self.lampSlider.valueChanged[int].connect(self.Slider_change)
        self.button_control()
        
    
    def button_control(self):    
        self.lampbtn.clicked.connect(self.lamp)
        self.pushButton.clicked.connect(self.vissza)
        
    def lamp(self):
        print("Button has been pushed")
        global bedlamp
        global ertek
        if(bedlamp == "on"):
            self.lampbtn.setText("OFF")
            print("set to OFF")
            bedlamp = "off"
            
        else:
            self.lampbtn.setText("ON")
            print("set to ON")
            bedlamp = "on"
            
    def vissza(self):
        self.close()
            # ertek = self.lampSlider.value()
            # print("Ertek: " + ertek)
            
    # def Slider_change(self):
    #     print("Button has been pushed")
    #     global bedlamp
    #     global ertek
    #     ertek = self.lampSlider.value()
    #     if(bedlamp == "on"):
    #         print("Value: " + ertek)
 
        
