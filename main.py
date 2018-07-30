import sys
import csv
import ntpath
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QLineEdit, QFileDialog, QListWidgetItem
from PyQt5.QtCore import (QCoreApplication, Qt, QEvent)
from mainUI import Ui_MainWindow
from data_extractor import *

"""
C&W Networks
Juan Diego
Jorge Ortega
"""

#pyuic5 mainWindow.ui -o mainUI.py


class Qfile(QListWidgetItem):
    def __init__(self, path, parent=None):
        self.path = path
        self.filename = os.path.basename(self.path)
        super().__init__(self.filename)

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.listIndex = -1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_fileB.triggered.connect(self.openFileNameDialog)
        self.ui.pushButton.clicked.connect(self.extract_data)
        self.ui.listWidget.itemSelectionChanged.connect(self.test)

    def test(self):
        self.listIndex = self.ui.listWidget.currentRow()
        print(self.ui.listWidget.currentRow())

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Escape:
            QCoreApplication.quit()
        elif key == Qt.Key_Delete:
            print(self.ui.listWidget.currentRow())
            if self.listIndex>=0:
                item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                item = None
                for i in range(self.ui.listWidget.count()):
                    self.ui.listWidget.item(i).setSelected(False)
                self.listIndex = -1
                self.ui.pushButton.setFocus()

    def mousePressEvent(self, event):
        #print("X:",event.x(),", Y:",event.y())
        for i in range(self.ui.listWidget.count()):
            self.ui.listWidget.item(i).setSelected(False)
        self.listIndex = -1
        self.ui.pushButton.setFocus()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileNames, _ = QFileDialog.getOpenFileNames(self,"Abrir TXT", "","TXT (*.txt)", options=options)
        if fileNames:
            for i in fileNames:
                self.ui.listWidget.addItem(Qfile(i))
        self.ui.pushButton.setFocus()

    def extract_data(self):
        outFile = 'Resultado_SAPs'
        final_data = [["Name", "Service", "Saps", "Ports"]]

        if os.path.isfile(outFile +'.csv'):
            index = 0
            print("Problem")
            while True:
                if os.path.isfile(outFile + '_' + str(index) + '.csv'):
                    index = index + 1
                else:
                    outFile = outFile + '_' + str(index)
                    break;
                print( outFile + '_' + str(index) + '.csv')


        with open(outFile +'.csv', 'w', newline='') as f:
            for i in range(self.ui.listWidget.count()):
                #print(self.ui.listWidget.item(i).text())
                data = extract(self.ui.listWidget.item(i).path)
                final_data = final_data + data + [["","","",""]]

            writer = csv.writer(f)
            writer.writerows(final_data)

        self.ui.listWidget.clear()


app = QApplication(sys.argv)
w = AppWindow()
w.show()

sys.exit(app.exec_())
w.end()
