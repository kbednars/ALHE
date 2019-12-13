import sys

import networkx as nx
from PyQt5 import QtWidgets

from myform import MyForm


def onImportGraphClicked():
    graphPath = myapp.openFileNamesDialog()
    if graphPath == "":
        return
    print(graphPath)
    try:
        graph = nx.read_gml(graphPath)
    except nx.NetworkXError:
        myapp.showErrorDialog("The input cannot be parsed.")
        return
    myapp.ui.frameLabel.setGraph(graph)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()

    # connect buttons to functions
    myapp.ui.import_graph_button.clicked.connect(onImportGraphClicked)

    myapp.show()
    sys.exit(app.exec_())
