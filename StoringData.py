import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        self.button_di_cek = False #Variabel 
        self.setWindowTitle('MyApp')
        
        self.button = QPushButton('Tekan tombol')
        self.button.setCheckable(True) # Metode ini digunakan untuk mengatur apakah tombol adala tombol toggle/bukan
        self.button.clicked.connect(self.button_telah_dialihkan) # memanggil ke fungsi
        self.button.setChecked(self.button_di_cek) # Metode ini digunakan untuk mengubah status kotak centang. Secara default, kotak centang tidak dicentang(False). Setelah mengklik widget kotak centang(True), statusnya berubah menjadi dicentang
        
        self.setCentralWidget(self.button)
        
    def button_telah_dialihkan(self, checked) :
        self.button_di_cek = checked # memasukkan variabel checked yang berisi kebalikan kondisi True-> False , False->True ke variabel button_di_cek
        # atau menggunakan dibawah ini, jika di argumen fungsi tidak ingin menambahkan checked
        #self.button_di_cek = self.button.isChecked()
        print(self.button_di_cek) # Menampilkan hasil variabel button di cek
    
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
