import sys
import os
from os.path import join ,dirname
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSize
from PyQt5.uic import loadUiType

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

From_Main, _ = loadUiType(join(dirname(__file__), r'C:\File_PyQt5\showtbl.ui'))

class MainWindow(QWidget, From_Main) :
    def __init__ (self) :
        super(MainWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        
    def OpenFile(self) :
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*csv)')
        self.all_data = pd.read_csv(path[0])
        
    def showFile(self) :
        nums = self.spinbox.value()
        
        if nums == 0 :
            numRows = len(self.all_data.index)
            
        else :
            numRows = nums
            
        numColumns = len(self.all_data.columns)
            
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numColumns)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        
        for i in range(numRows) :
            for j in range(numColumns) :
                self.tableWidget.addItem(QTableWidgetItem(str(i,j,self.all_data.iat[i][j])))
        
        self.tableWidget.resizeColumnsToContents()
    
    def showDataVisualize(self, sumbuX, sumbuY) :
        scene = QGraphicsScene()
        fig, ax = plt.subplots()
        sns.regplot(data= self.all_data, x = sumbuX, y=sumbuY)
        
        canvas = FigureCanvas(fig)
        scene.addWidget(canvas)
        self.grafik_plot.setScene(scene)
        
        
    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        
    


