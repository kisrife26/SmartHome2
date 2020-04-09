import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class Livingroom(QDialog):
    def __init__(self):
        super(Livingroom,self).__init__()
        loadUi('livingroom.ui',self)
        self.setWindowTitle('Livingroom')
        
 
        
