import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow) :
    def __init__ (self) :
        super().__init__()
        
        self.setWindowTitle('My App')
        
        #membuat label disimpan di widget
        widget = QLabel('Hello')
        
        widget = QLabel('1')
        widget.setText('2') # untuk mengubah isi label yang awlanya 1 menjadi 2
        
        
        #membuat label
        label = QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        label.setFont(font)
        
        #Mengkombnasikan letak
        align_top_left = Qt.AlignLeft | Qt.AlignTop
        label.setAlignment(align_top_left)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.setCentralWidget(label)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()