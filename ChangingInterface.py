import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle('My App')
        
        self.button = QPushButton('Klik!')
        
        self.button.clicked.connect(self.diklik)
        self.button.setCheckable(True)
        
        self.setCentralWidget(self.button)
        
    def diklik(self) :
        self.button.setText('Kamu udah ngeklik ini')
        self.button.setEnabled(False) # Menonaktifkan klik sehingga button hanya boleh diklik sekali
        
        self.setWindowTitle('Ur App') # Mengubah aplikasi
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()