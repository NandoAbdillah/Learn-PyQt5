from PyQt5.QtWidgets import QApplication, QWidget

#Hanya diperlukan untuk akses ke command line
import sys

#Anda memerlukan satu (dan hanya satu) pemanggilan kelas QApplication per satu aplikasi
#Memasukkan sys.argv untuk mengizinkan argumen command line untuk aplikasi anda
#Asal anda tahu, jika kamu tidak ingin menggunakan argumen command line, QApplicataion([]) juga berfungsi

#app = QApplication([])
app = QApplication(sys.argv)


#Membuat sebuah Qt widget, yang akan menjadi window/jendela aplikasi kita
window = QWidget()
#window-- adalh top level widget yang artinya dia tidak memiliki induk dan tidak disarangkan/dimasukkan ke widget lain, maka dari itu widget tanpa induk akan otomatis tersembunyi dan harus menggunakan .show() untuk menampilkannya

#Apa itu jendela? - Menyimpan antarmuka pengguna aplikasi Anda - Setiap aplikasi memerlukan setidaknya satu (...tapi bisa lebih) - Aplikasi akan (secara default) keluar ketika jendela terakhir ditutup
window.show() 

# Memulai perulangan even
app.exec()
#bisa juga app.exec_()


