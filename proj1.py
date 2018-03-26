import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import sys
#import welly
from welly import Well

from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.uic import loadUi

class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)


        loadUi("calgeopy.ui", self)

        self.btnPlotlas.clicked.connect(self.plotlas)

    def plotlas(self):
        filename = self.le_filename.text()

        w = Well.from_las(filename)

        x = w.data['GR']
        y=w.df().index.values

        print(x.shape, y.shape)

        self.gvPlot.plot(x,y)
        self.gvPlot.invertY(True)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = AppMainWindow()

    # Attach the File->Exit menu item to the slot to close the window
    mainWnd.actionExit.triggered.connect(mainWnd.close)

    # Show the window
    mainWnd.show()

    # Start the main messageloop
    sys.exit(app.exec_())