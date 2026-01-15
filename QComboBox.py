import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        widget = QComboBox()
        #Menambahkan pilihan
        widget.addItems(['One', 'Two', 'Three'])
        
        #currentIndexChanged disebut signal
        widget.currentIndexChanged.connect(self.index_changed)
        
        widget.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)
        
    def index_changed(self, i) : #i adalah  sebuah integer
        print(i)
        
    def text_changed(self, s) : #s adalah sebuah string
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()