import networkx as nx
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GraphView(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        # self.setStyleSheet('QFrame {background-color:white;}')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.nodes = None
        self.edges = None

    def setGraph(self, graph: nx.Graph):
        self.nodes = graph.nodes()._nodes
        self.edges = graph.edges()._adjdict
        self.setText("")

    # returns node coordinates with added padding
    def getCoordinates(self, nodeName):
        x = self.nodes[nodeName]['graphics']['x'] + 30
        y = self.nodes[nodeName]['graphics']['y'] + 30
        return QPoint(x, y)

    def paintEvent(self, event):
        super().paintEvent(event)
        width = self.width()
        height = self.height()
        painter = QPainter(self)
        painter.setPen(Qt.black)
        if self.nodes:
            for startKey in self.edges:
                startPoint = self.getCoordinates(startKey)
                for endKey in self.edges[startKey]:
                    painter.drawLine(startPoint, self.getCoordinates(endKey))
            painter.setPen(Qt.darkBlue)
            for key in self.nodes:
                self.getCoordinates(key)
                painter.drawText(self.getCoordinates(key), key)
