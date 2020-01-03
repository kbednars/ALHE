import sys

import networkx as nx
from PyQt5 import QtWidgets

from antColony import AntColony
from graphConverter import toArrayGraph
from myform import MyForm

graph = None


def onImportGraphClicked():
    graphPath = myapp.openFileNamesDialog()
    if graphPath == "":
        return
    print(graphPath)
    try:
        global graph
        graph = nx.read_gml(graphPath)
        myapp.ui.frameLabel.setGraph(graph)
    except nx.NetworkXError:
        myapp.showErrorDialog("The input cannot be parsed.")
        return


def onSolveClicked():
    if graph is not None:
        ant = AntColony(5, 12, 0.4, 0.5, 0.25, 1, toArrayGraph(graph))
        print(ant.antSolver())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()

    # connect buttons to functions
    myapp.ui.importButton.clicked.connect(onImportGraphClicked)
    myapp.ui.solveButton.clicked.connect(onSolveClicked)

    myapp.show()
    sys.exit(app.exec_())
