from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from mainwindow_ui import Ui_MainWindow


class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def openFileNamesDialog(self) -> str:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select graph to load", "",
                                                   "Graph Modelling Language (*.gml)", options=options)
        return file_path

    def showErrorDialog(self, errorMessage):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorMessage)
        msg.setWindowTitle("Error")
        msg.exec_()
