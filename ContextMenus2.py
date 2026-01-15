import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

#Kode dibawah ini , kegunaannya sama kayak yang contextmenu1, cuman bedanya disini kita membuat fungsinya sendiri bukan bawaan QMain
class MainWindow(QMainWindow) :
    def __init__ (self) :
        super().__init__()
        
        self.show()
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction('test1', self))
        context.addAction(QAction('test2', self))
        context.addAction(QAction('test3', self))
        context.exec(self.mapToGlobal(pos))
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
