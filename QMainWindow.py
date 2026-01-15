import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

app = QApplication(sys.argv)

# Qt sudah memiliki solusi untuk Anda -- QMainWindow. Ini adalah widget siap pakai yang menyediakan banyak fitur jendela standar yang akan Anda gunakan di aplikasi Anda, termasuk toolbar, menu, statusbar, widget yang dapat dipasang ke dok, dan banyak lagi. Kita akan melihat fitur-fitur canggih ini nanti, tapi untuk saat ini, kita akan menambahkan QMainWindow kosong sederhana ke aplikasi kita.
window = QMainWindow()
window.show()

app.exec_()