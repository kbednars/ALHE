import sys
from PyQt5 import QtWidgets
from mainwindow_ui import Ui_MainWindow


class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def on_import_graph_clicked():
    print('import_graph_button.clicked')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()

    # connect on click actions
    myapp.ui.import_graph_button.clicked.connect(on_import_graph_clicked)

    myapp.show()
    sys.exit(app.exec_())
