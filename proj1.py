import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PyQt5.uic import loadUi

from welly import Well


class AppMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)


        loadUi("calgeopy_march27.ui", self)

        self.btnGetfilename.clicked.connect(self.getfilename)
        self.btnPlotlas.clicked.connect(self.plotlas)


    def getfilename(self):
        dir = sys.path[-1]
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            dir, "LAS file (*.las)")
        self.le_filename.setText(str(fname[0].replace('\\', '/')))

    def plotlas(self):
        filename = self.le_filename.text()

        w = Well.from_las(filename)

        x = w.data['GR']
        #y=w.df().index.values
        #y=w.data['GR'].basis
        y=w.survey_basis()



        self.gvPlot1.plot(x,y,pen=(1, 4))
        self.gvPlot1.invertY(True)
        self.gvPlot1.setTitle("Gamma")
        self.gvPlot1.setMouseEnabled(x=False, y=True)

        x = w.data['DT']
        self.gvPlot2.plot(x, y,pen=(2, 4))
        self.gvPlot2.invertY(True)
        self.gvPlot2.setTitle("Sonic")
        self.gvPlot2.setYLink(self.gvPlot1)
        self.gvPlot2.setMouseEnabled(x=False, y=True)

        x = w.data['RHOB']
        self.gvPlot3.plot(x, y,pen=(3, 4))
        self.gvPlot3.invertY(True)
        self.gvPlot3.setTitle("Density")
        self.gvPlot3.setYLink(self.gvPlot1)
        self.gvPlot3.setMouseEnabled(x=False, y=True)

        x = w.data['DPHI_SAN']
        self.gvPlot4.plot(x, y,pen=(4, 4))
        self.gvPlot4.invertY(True)
        self.gvPlot4.setTitle("Porosity")
        self.gvPlot4.setYLink(self.gvPlot1)
        self.gvPlot4.setMouseEnabled(x=False, y=True)

        # self.gvPlot

        tops=[["Tops1",400],['Top2',600],['Top3',800]]


        for tp in tops:
            self.gvPlot1.addLine(x=None, y=tp[1])
            tp_txt=pg.TextItem(text=tp[0])
            self.gvPlot1.addItem(tp_txt)
            tp_txt.setPos(15,tp[1],)
            self.gvPlot2.addLine(x=None, y=tp[1])
            self.gvPlot3.addLine(x=None, y=tp[1])
            self.gvPlot4.addLine(x=None, y=tp[1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = AppMainWindow()

    # Attach the File->Exit menu item to the slot to close the window
    mainWnd.actionExit.triggered.connect(mainWnd.close)

    # Show the window
    mainWnd.show()

    # Start the main messageloop
    sys.exit(app.exec_())