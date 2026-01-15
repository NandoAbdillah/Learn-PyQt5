import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        self.widget = QLabel('Pussy Cat')
        
        self.image_shown = False
        
        self.setCentralWidget(self.widget)
        
        #Digunakan untuk menyesuaikan konten dengan ukuran yang baru
        self.widget.setScaledContents(True)
        
    def mousePressEvent(self, e) :
        if self.image_shown :
            self.widget.setPixmap(QPixmap(r'C:\File_PyQt5\belajar_pyqt5\kocheng.webp'))
        
        else :
            self.widget.setPixmap(QPixmap(r'C:\File_PyQt5\belajar_pyqt5\kocheng2.jpg'))

        self.image_shown = not self.image_shown
        print(self.image_shown)
        
        
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
