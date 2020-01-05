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
    myapp.ui.frameLabel.setGraph(None)
    try:
        global graph
        graph = nx.read_gml(graphPath)
        graph = graph.to_undirected()
        myapp.ui.frameLabel.setGraph(graph)
    except nx.NetworkXError:
        myapp.showErrorDialog("The input cannot be parsed.")
        return


def onSolveClicked():
    if graph is not None:
        weightedAdjacencyArray, nodeKeysList = toArrayGraph(graph)
        ant = AntColony(myapp.ui.antsQuantitySpinBox.value(),
                        myapp.ui.generationsQuantitySpinBox.value(),
                        myapp.ui.alphaSpinBox.value(),
                        myapp.ui.betaSpinBox.value(),
                        myapp.ui.evaportationRatioSpinBox.value(),
                        myapp.ui.evaportationRatioSpinBox.value(),
                        weightedAdjacencyArray,
                        graph,
                        nodeKeysList,
                        startNode,
                        finishNode)
        path, cost = ant.antSolver()
        print(path, cost)
        myapp.ui.frameLabel.setBestPath(path, nodeKeysList)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()

    # connect buttons to functions
    myapp.ui.importButton.clicked.connect(onImportGraphClicked)
    myapp.ui.solveButton.clicked.connect(onSolveClicked)

    myapp.show()
    sys.exit(app.exec_())
