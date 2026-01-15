import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt


class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        self.label  = QLabel('Mouse Event')
        self.button = QPushButton('Klik ini')
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton :
            self.label.setText('MousePressEvent LEFT')
            
            
        elif e.button() == Qt.MiddleButton :
            self.label.setText('MousePressEvent MIDDLE')
            
        elif e.button() == Qt.RightButton :
            self.label.setText('MousePressEvent RIGHT')
            
        #Qt.NoButton -> binary : 0(000) -> tidak ada button yang ditekan/ event tidak terkait dengan penekanan button
        #Qt.LeftButton -> Binary : 1(001) -> button kiri ditekan
        #Qt.RightButton -> Binary : 2 (010) -> button kanan
        #Qt.MiddleButton -> Bianry(100) -> button tengah ditekan
            

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec() 