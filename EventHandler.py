# mouseMoveEvent -> kursor bergerak diatas obj
# mousePressEvent -> menekan obj
# mouseReleaseEvent -> melaepas obj
# mouseDoubleClickEvent -> double klik objek

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel, QTextEdit

class MainWindow(QMainWindow) :
    def __init__(self) :
        
        super().__init__()
        
        self.setWindowTitle('My App')
        
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)
        
    def mouseMoveEvent(self, e):
        self.label.setText('mouseMoveEvent')
        
    def mousePressEvent(self, e):
        self.label.setText('mousePressEvent')
        
    def mouseReleaseEvent(self, e):
        self.label.setText('mouseReleaseEvent')
        
    def mouseDoubleClickEvent(self, e) :
        self.label.setText('mouseDoubleClickEvent')
        
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()


