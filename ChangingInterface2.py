from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

kumpulan_judul = [
    'Aplikasiku',
    'Aplikasiku2',
    'MasihAplikasiku',
    'BukuCatatan',
    'AplikasiSkem',
    'AdaYangSalah'
]


class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        
        self.n_kali_diklik = 0
        
        self.setWindowTitle('My App')
        
        self.button = QPushButton('Klik ini')
        self.button.clicked.connect(self.button_diklik)
        self.setCentralWidget(self.button)
        
        self.windowTitleChanged.connect(self.judul_window_berubah)
        
        self.setCentralWidget(self.button)
        
    def button_diklik(self):
        print('diklik')
        judul_baru = choice(kumpulan_judul)
        
        print('Judul diatur : %s' % judul_baru)
        
        self.setWindowTitle(judul_baru)
        
    def judul_window_berubah(self, window_title) :
        #widow_title adalah argumen bawaan QMainWindow!
        print('Judul Window berubah : %s' % window_title)
        
        if (window_title == 'AdaYangSalah' or window_title =='AplikasiSkem'):
            #Akan mendisable otomatis ketika judul aplikasi diganti dengan apayang salah/skem
            self.button.setDisabled(True)
            


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
        
        