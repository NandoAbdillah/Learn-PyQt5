import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle('My App')
        button = QPushButton('Klik ini')
        self.setCentralWidget(button)
        # Kita telah mendengar bahwa sinyal juga dapat mengirimkan data untuk memberikan lebih banyak informasi tentang apa yang baru saja terjadi. Sinyal .clicked tidak terkecuali, juga menyediakan status dicentang (atau dialihkan) untuk tombol tersebut. Untuk tombol normal ini selalu False, jadi slot pertama kita mengabaikan data ini. Namun, kita dapat membuat tombol kita dapat dicentang dan melihat efeknya.
        
        button.setCheckable(True)
        button.clicked.connect(self.button_sudah_diklik)
        button.clicked.connect(self.button_sudah_dialihkan)
        
    
    def button_sudah_diklik(self) :
        print('diklik!')
        
    def button_sudah_dialihkan(self, checked) :
        # Status awal true , jika diklik jadi false, diklik lagi jadi true lagi , berulang-ulang
        print('dicek?', checked)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()