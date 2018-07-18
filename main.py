import sys
import csv
import ntpath
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QLineEdit, QFileDialog
from mainUI import Ui_MainWindow

"""
C&W Networks
Juan Diego
Jorge Ortega
"""

#pyuic5 mainWindow.ui -o mainUI.py

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_fileB.triggered.connect(self.openFileNameDialog)
        self.ui.pushButton.clicked.connect(self.remove_item)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames(self,"Abrir CSV", "","CSV (*.csv)", options=options)
        if fileName:
            self.ui.listWidget.addItem(ntpath.basename(fileName))
            print(self.ui.listWidget.count())
            print(self.ui.listWidget.item(0))

    def remove_item(self):
        print(self.ui.listWidget.currentRow())
        if self.ui.listWidget.currentRow()>=0:
            item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            item = None

app = QApplication(sys.argv)
w = AppWindow()
w.show()

sys.exit(app.exec_())
w.end()
