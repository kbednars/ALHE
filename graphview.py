import networkx as nx
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

PADDING = 30


class GraphView(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.nodes = None
        self.bestPath = None
        self.nodeKeysList = None
        self.edges = None
        self.pheromoneMatrix = None
        self.maxPheromone = None
        self.maxX = 0
        self.maxY = 0

    def setGraph(self, graph: nx.Graph):
        self.maxX = 0
        self.maxY = 0
        if graph is None:
            self.nodes = None
            self.bestPath = None
            self.nodeKeysList = None
            self.edges = None
            self.pheromoneMatrix = None
            self.maxPheromone = None
            self.maxX = 0
            self.maxY = 0
        else:
            self.nodes = graph.nodes()._nodes
            self.edges = graph.edges()._adjdict
            for key, val in self.nodes.items():
                self.maxX = val['graphics']['x'] if val['graphics']['x'] > self.maxX else self.maxX
                self.maxY = val['graphics']['y'] if val['graphics']['y'] > self.maxY else self.maxY
            self.setText("")

    def setBestPath(self, bestPath, nodeKeysList):
        self.bestPath = bestPath
        self.nodeKeysList = nodeKeysList
        self.repaint()

    def setPheromones(self, pheromoneMatrix):
        self.pheromoneMatrix = pheromoneMatrix
        self.maxPheromone = self.pheromoneMatrix.max()
        self.repaint()

    # returns node coordinates with added padding, scaled to fit in current window size
    def getScaledCoordinates(self, nodeName):
        drawableWidth = self.width() - 2 * PADDING
        drawableHeight = self.height() - 2 * PADDING
        xFitRatio = self.maxX / drawableWidth
        yFitRatio = self.maxY / drawableHeight
        x = self.nodes[nodeName]['graphics']['x']
        y = self.nodes[nodeName]['graphics']['y']
        if xFitRatio <= 1 and yFitRatio <= 1:
            pass
        elif xFitRatio < yFitRatio:
            x /= yFitRatio
            y /= yFitRatio
        else:
            x /= xFitRatio
            y /= xFitRatio
        return QPoint(x + PADDING, y + PADDING)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.eraseRect(event.rect())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.white, 1))
        if self.nodes:
            for startKey in self.edges:
                startPoint = self.getScaledCoordinates(startKey)
                for endKey in self.edges[startKey]:
                    if self.nodeKeysList and self.pheromoneMatrix is not None:
                        startIndex = self.nodeKeysList.index(startKey)
                        endIndex = self.nodeKeysList.index(endKey)
                        pheromoneQuantity = self.pheromoneMatrix[startIndex][endIndex] + \
                                            self.pheromoneMatrix[endIndex][startIndex]
                        coefficient = (pheromoneQuantity / (2 * self.maxPheromone))
                        if coefficient > 1:
                            coefficient = 1
                        lineWidth = 10 * coefficient
                        if lineWidth < 1:
                            lineWidth = 1
                        painter.setPen(QPen(QColor(255 * (1 - coefficient), 255 * (1 - coefficient), 255), lineWidth))
                    painter.drawLine(startPoint, self.getScaledCoordinates(endKey))

        painter.setPen(QPen(Qt.green, 10))
        if self.bestPath:
            for index in range(0, len(self.bestPath) - 1):
                startPoint = self.getScaledCoordinates(self.nodeKeysList[self.bestPath[index]])
                endPoint = self.getScaledCoordinates(self.nodeKeysList[self.bestPath[index + 1]])
                painter.drawLine(startPoint, endPoint)

        if self.nodes:
            painter.setPen(Qt.darkBlue)
            for key in self.nodes:
                self.getScaledCoordinates(key)
                painter.drawText(self.getScaledCoordinates(key), key)
