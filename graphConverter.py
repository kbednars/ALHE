import math
import networkx as nx
import numpy as np


def toArrayGraph(nxGraph: nx.Graph):
    nodesList = list(nxGraph.nodes().keys())
    size = (len(nodesList), len(nodesList))
    weightedAdjacencyArray = np.zeros(size).astype(int)
    adjArr = np.squeeze(np.asarray(nx.to_numpy_matrix(nxGraph)))
    for fromKey in nodesList:
        for toKey in nodesList:
            weightedAdjacencyArray[nodesList.index(fromKey)][nodesList.index(toKey)] = \
                getWeight(nxGraph.nodes()._nodes, fromKey, toKey) * \
                adjArr[nodesList.index(fromKey)][nodesList.index(toKey)]
    return weightedAdjacencyArray, nodesList


def getWeight(nodes, firstKey, secondKey):
    x1 = nodes[firstKey]['graphics']['x']
    y1 = nodes[firstKey]['graphics']['y']
    x2 = nodes[secondKey]['graphics']['x']
    y2 = nodes[secondKey]['graphics']['y']
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
