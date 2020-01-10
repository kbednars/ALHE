import sys

import networkx as nx
from PyQt5 import QtWidgets

from antColony import AntColony
from graphConverter import toArrayGraph
from myform import MyForm

graph = None
nodeKeysList = None
thread = None
generationsCount = 0


def onImportGraphClicked():
    graphPath = myapp.openFileNamesDialog()
    if graphPath == "":
        return
    myapp.ui.frameLabel.setGraph(None)
    try:
        global graph
        graph = nx.read_gml(graphPath)
        graph = graph.to_undirected()
        myapp.ui.frameLabel.setGraph(graph)
        myapp.ui.startNodeComboBox.clear()
        myapp.ui.endNodeComboBox.clear()
        myapp.ui.startNodeComboBox.addItems(graph.nodes())
        myapp.ui.endNodeComboBox.addItems(graph.nodes())
    except nx.NetworkXError:
        myapp.showErrorDialog("The input cannot be parsed.")
        return


def onSolveClicked():
    if graph is not None:
        global nodeKeysList
        global generationsCount
        generationsCount = myapp.ui.generationsQuantitySpinBox.value()
        weightedAdjacencyArray, nodeKeysList = toArrayGraph(graph)
        myapp.ui.frameLabel.setBestPath(None, nodeKeysList)
        ant = AntColony(myapp.ui.antsQuantitySpinBox.value(),
                        myapp.ui.generationsQuantitySpinBox.value(),
                        myapp.ui.alphaSpinBox.value(),
                        myapp.ui.betaSpinBox.value(),
                        myapp.ui.evaportationRatioSpinBox.value(),
                        myapp.ui.pheromoneZeroSpinBox.value(),
                        weightedAdjacencyArray,
                        graph,
                        nodeKeysList,
                        myapp.ui.startNodeComboBox.currentIndex(),
                        myapp.ui.endNodeComboBox.currentIndex(),
                        myapp.ui.intervalSpinBox.value()
                        )
        global thread
        if thread:
            thread.terminate()
        ant.pheromoneSignal.connect(onPheromoneUpdate)
        ant.bestPathSignal.connect(onBestPath)
        thread = ant
        ant.start()


def onPheromoneUpdate(pheromoneMatrix, generation):
    myapp.ui.frameLabel.setPheromones(pheromoneMatrix)
    myapp.ui.generationCounter.setText("Current generation: {0}/{1}".format(generation + 1, generationsCount))


def onBestPath(path, cost):
    print(path, cost)
    myapp.ui.frameLabel.setBestPath(path, nodeKeysList)
    myapp.ui.generationCounter.setText("Current generation: 0/0")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()

    # connect buttons to functions
    myapp.ui.importButton.clicked.connect(onImportGraphClicked)
    myapp.ui.solveButton.clicked.connect(onSolveClicked)

    myapp.show()
    sys.exit(app.exec_())
