import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QAction, QMenu


class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        
    
    #Klik kanan pada window untuk menampilkan pilihan konteks    
    def contextMenuEvent(self, e) :
        context = QMenu()
        context.addAction(QAction('test 1', self))
        context.addAction(QAction('test 2', self))
        context.addAction(QAction('test 3', self))
        context.exec(e.globalPos())
        
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()