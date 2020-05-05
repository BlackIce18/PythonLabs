import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
from untitled import *
import re
from itertools import groupby
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.action.clicked.connect(self.printButtonPressed)
        #print(self.ui.menubar.addMenu('&File').addAction('&Открыть файл', self.browse))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main() #ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    statusBar = QtWidgets.QStatusBar()

    #QtWidgets.QMainWindow().menubar.action.clicked.connect(self.browse)

    #MainWindow.action.setText(QtWidgets._translate("MainWindow", "Открыть12 файл"))
    #ui.action.clicked.connect(browse)
    #filename = ""

    #print(ui.menubar)




    sys.exit(app.exec_())