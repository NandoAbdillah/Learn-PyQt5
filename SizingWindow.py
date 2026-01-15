import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        button = QPushButton('Push Me')
        self.setCentralWidget(button)
        
        #self.setFixedSize(QSize(500,700))
        #QSize itu Width,Height
        # Selain .setFixedSize() Anda juga dapat memanggil .setMinimumSize() dan .setMaximumSize() untuk menyetel masing-masing ukuran minimum dan maksimum. 
        self.setFixedSize(QSize(720,450)) #Ukuran Awal
        self.setMaximumSize(QSize(800,500)) #Ukuran Maksimum, tidak bisa lebih dilebarkan
        self.setMinimumSize(QSize(300,300)) #Ukuran Minimum, tidak bisa lebih dikecilkan
        
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()