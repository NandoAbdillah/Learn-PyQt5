'''
# Cara import file ui 1
import sys
import os
from os.path import join,dirname
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import loadUiType
#atau bisa jika file table_widget.ui di parse dulu ke py maka yang ditulis from nya seperti dibawah ini
#from table_widget import Ui_MainWindow

From_Main, _ = loadUiType(join(dirname(__file__),'table_widget.ui'))
'''

#Cara ke2 import file ui

import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class Ui_MainWindow(QMainWindow) :
    def __init__(self) :
        super(Ui_MainWindow,self).__init__()
        loadUi(r'C:\File_PyQt5\belajar_pyqt5\tabel_widget.ui', self)
        

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Program percobaan')


app = QApplication(sys.argv)
window = Ui_MainWindow()
window.show()
app.exec()
        

