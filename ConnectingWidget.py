import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle('My App')
        
        #Membuat label
        self.label = QLabel()
        
        #Membuat input
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText) #Ini digunakan keteika kalian menulis di inputan , maka label akan otomatis mengikuti apa yang kalian tulis di inputan
        
        #Membuat Layout untuk input dan label
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        
        #Membuat Container untuk layout
        container = QWidget()
        container.setLayout(layout)
        
        #Mengatur letak container
        self.setCentralWidget(container)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()