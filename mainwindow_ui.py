# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1061, 574)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_graph_button = QtWidgets.QPushButton(self.centralWidget)
        self.import_graph_button.setObjectName("import_graph_button")
        self.horizontalLayout.addWidget(self.import_graph_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frameLabel = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLabel.sizePolicy().hasHeightForWidth())
        self.frameLabel.setSizePolicy(sizePolicy)
        self.frameLabel.setMinimumSize(QtCore.QSize(1, 1))
        self.frameLabel.setMaximumSize(QtCore.QSize(1472, 828))
        self.frameLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frameLabel.setScaledContents(True)
        self.frameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLabel.setObjectName("frameLabel")
        self.verticalLayout.addWidget(self.frameLabel)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ant Colony Graph Solver"))
        self.import_graph_button.setText(_translate("MainWindow", "Import graph"))
        self.frameLabel.setText(_translate("MainWindow", "Imported graph will be displayed here."))


