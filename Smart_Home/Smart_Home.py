import sys
## import paho.mqtt.client as mqtt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class untitled(QDialog):
    def __init__(self):
        super(untitled,self).__init__()
        loadUi('Smart_Home_dialog.ui',self)
        self.setWindowTitle('Smart Home')
        self.bedroombtn.clicked.connect(self.bedroom)
        self.gardenbtn.clicked.connect(self.garden)
        self.livingroombtn.clicked.connect(self.livingroom)
        self.garagebtn.clicked.connect(self.garage)
    @pyqtSlot()
    def bedroom(self):
        from bedroom import Bedroom
        theclass = Bedroom()
        print(theclass)
        theclass.exec_()
    def garden(self):
        from garden import Garden
        theclass = Garden()
        print(theclass)
        theclass.exec_()
    def livingroom(self):
        from livingroom2 import Livingroom2
        theclass = Livingroom2()
        print(theclass)
        theclass.exec_()
    def garage(self):
        from garage import Garage
        theclass = Garage()
        print(theclass)
        theclass.exec_()
        
        
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscrible("mqtt/test/fogad")
    
    def on_message(client, userdata, msg, self):
        if(msg.topic == "mqtt/test/fogad"):
            self.livingroomtemp.setText(msg.payload.decode("UTF-8") + "°C")
            
        
app=QApplication(sys.argv)
widget=untitled()
widget.show()
sys.exit(app.exec_())