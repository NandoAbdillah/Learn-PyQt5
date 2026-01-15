# Yang kita perlukan adalah cara menghubungkan tindakan menekan tombol dengan mewujudkan sesuatu. Di Qt, ini disediakan oleh signal dan slot atau event.

# Sinyal adalah notifikasi yang dikeluarkan oleh widget ketika terjadi sesuatu. Sesuatu itu bisa berupa apa saja, mulai dari menekan tombol, mengubah teks kotak input, hingga mengubah teks jendela. Banyak sinyal yang dipicu oleh tindakan pengguna, namun ini bukanlah suatu aturan.

import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) :
        
        super().__init__()
        self.setFixedSize(QSize(400,720))
        self.setWindowTitle('My App')
        button = QPushButton('Press on me')
        button.setFixedSize(QSize(100,50))
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.button_diklik)
        # clicked adalah sinyalnya, lalu diarahkan ke fungsi def button_klik

        
        
    def button_diklik (self) :
        print('button diklik') #Menampilkan di terminal

app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()