import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton

class MainWindow(QMainWindow) :
    def __init__ (self) :
        super().__init__()
        
        self.button = CustomButton('Klik')
        
        self.setCentralWidget(self.button)
        
class CustomButton(QPushButton):
    def mousePressEvent(self, e):
        e.ignore()
        # self.setText('clicked')
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
