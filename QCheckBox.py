import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        
        widget = QCheckBox('Check me')
        widget.setCheckState(Qt.Unchecked)
        # checked = 2, unchecked = 0, and partially checked = 1
        
        widget.stateChanged.connect(self.show_state)
        
        self.setCentralWidget(widget)
        
        
    def show_state(self, s) :
        print(s)
        print(Qt.Checked)
        print(s==Qt.Checked)
        print(s)
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
