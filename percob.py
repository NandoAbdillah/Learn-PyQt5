import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle('My App')
        
        self.label = QLabel('label')
        self.button = MyButton('klik')
        self.button.clicked.connect(self.button_diklik)
    
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        
        
    def button_diklik (self) :
        self.label.setText('Button terklik')
        
    def mousePressEvent(self, event) :
        print('Mouse Pressed!')
        super().contextMenuEvent(event)
        
    
class MyButton(QPushButton) :

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.RightButton :
            self.setText('Raif Dobel klik!')
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()