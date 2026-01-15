# Saya mendapatkan tabel_widget.py dari terminal vs code lalu saya menulis pyuic5 tabel_widget.ui -o tabel_widget.py      
#Pastikan terminal beradda di folder direktori yang benar

from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidget, QTableWidgetItem
from tabel_widget import Ui_MainWindow
import sys

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProduct()
        
    def loadProduct(self):
        #Tabel Widget adalah nama untuk widget tabel yang kita buat
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)
        
        #Membuat label header/nama-nama kolom
        self.ui.tableWidget.setHorizontalHeaderLabels(['Brand','Price'])
        #bisa enggunakan tuple/list
        
        # Mengatur width/lebar kolom
        self.ui.tableWidget.setColumnWidth(0,120)
        self.ui.tableWidget.setColumnWidth(1,20)
        #syntaks -> indekskolom, ukuran
        
        #Mengisi item 
        #Syntaksnya -> indeksrow,indekskolom, QTableWidgwtItem('isi item)
        
        # Tapi dibwah ini terlalu ribet untuk membuat isian data maka ad acara lain yang lebih gampang
        
        '''
        self.ui.tableWidget.setItem(0,0, QTableWidgetItem('Phone1'))
        self.ui.tableWidget.setItem(0,1, QTableWidgetItem('1000'))
        
        self.ui.tableWidget.setItem(1,0, QTableWidgetItem('Phone2'))
        self.ui.tableWidget.setItem(1,1, QTableWidgetItem('1000'))
        
        self.ui.tableWidget.setItem(2,0, QTableWidgetItem('Phone3'))
        self.ui.tableWidget.setItem(2,1, QTableWidgetItem('1000'))
        '''
        
        #Menggunakan list dan dictionary
        produks = [
            #1 VFR = 30
            {'name':'Iphone', 'price' : '600,000 VFR'},
            {'name':'Huawei', 'price' : '450,000 VFR'},
            {'name':'Samsung', 'price' : '200,000 VFR'},
            {'name':'Xiaomi', 'price' : '100,000 VFR'},
            
        ]
        
        row_index = 0
        for produk in produks :
            self.ui.tableWidget.setItem(row_index,0,QTableWidgetItem(str(produk['name'])))
            self.ui.tableWidget.setItem(row_index,1,QTableWidgetItem(str(produk['price'])))
            
            row_index+=1
            
        
        
        
def create_app() :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
create_app()
    

