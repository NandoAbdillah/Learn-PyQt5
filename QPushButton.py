import sys
from PyQt5.QtWidgets import QApplication,QPushButton

app = QApplication(sys.argv)

# Anda akan mendapatkan jendela dengan satu tombol yang dapat ditekan di dalamnya.
window = QPushButton('Press on me!')
window.show()

app.exec_()

