import sys

from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Jika Anda ingin membuat jendela khusus, pendekatan terbaik adalah dengan membuat subkelas QMainWindow dan kemudian menyertakan pengaturan untuk jendela tersebut di blok __init__. Hal ini memungkinkan perilaku jendela menjadi mandiri. Kita dapat menambahkan subkelas QMainWindow kita sendiri — sebut saja MainWindow agar semuanya tetap sederhana.


#Kelas MainWindow adalah inherit dari class utama QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 
        #Saat Anda membuat subkelas kelas Qt, Anda harus selalu memanggil fungsi super __init__ agar Qt dapat menyiapkan objek.
        self.setWindowTitle("My App") #Untuk nama jendela aplikasi
        button = QPushButton("Press on me!")
        self.setCentralWidget(button)
        
        
app = QApplication(sys.argv)

window = MainWindow() #Tidak menggunakan QMainWindow lagi tapi merujuk ke class MainWindow
window.show()

app.exec()

