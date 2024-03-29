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
        MainWindow.resize(1100, 574)
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
        self.importButton = QtWidgets.QPushButton(self.centralWidget)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.intervalSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.intervalSpinBox.setMaximum(9.99)
        self.intervalSpinBox.setSingleStep(0.01)
        self.intervalSpinBox.setProperty("value", 0.1)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.horizontalLayout.addWidget(self.intervalSpinBox)
        self.generationCounter = QtWidgets.QLabel(self.centralWidget)
        self.generationCounter.setMinimumSize(QtCore.QSize(140, 0))
        self.generationCounter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generationCounter.setAutoFillBackground(False)
        self.generationCounter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.generationCounter.setObjectName("generationCounter")
        self.horizontalLayout.addWidget(self.generationCounter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.antsQuantitySpinBox = QtWidgets.QSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antsQuantitySpinBox.sizePolicy().hasHeightForWidth())
        self.antsQuantitySpinBox.setSizePolicy(sizePolicy)
        self.antsQuantitySpinBox.setMinimum(1)
        self.antsQuantitySpinBox.setMaximum(9999)
        self.antsQuantitySpinBox.setProperty("value", 5)
        self.antsQuantitySpinBox.setObjectName("antsQuantitySpinBox")
        self.horizontalLayout_2.addWidget(self.antsQuantitySpinBox)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.generationsQuantitySpinBox = QtWidgets.QSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generationsQuantitySpinBox.sizePolicy().hasHeightForWidth())
        self.generationsQuantitySpinBox.setSizePolicy(sizePolicy)
        self.generationsQuantitySpinBox.setMinimum(1)
        self.generationsQuantitySpinBox.setMaximum(9999)
        self.generationsQuantitySpinBox.setProperty("value", 100)
        self.generationsQuantitySpinBox.setObjectName("generationsQuantitySpinBox")
        self.horizontalLayout_2.addWidget(self.generationsQuantitySpinBox)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.alphaSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alphaSpinBox.sizePolicy().hasHeightForWidth())
        self.alphaSpinBox.setSizePolicy(sizePolicy)
        self.alphaSpinBox.setMaximum(1.0)
        self.alphaSpinBox.setSingleStep(0.01)
        self.alphaSpinBox.setProperty("value", 0.4)
        self.alphaSpinBox.setObjectName("alphaSpinBox")
        self.horizontalLayout_2.addWidget(self.alphaSpinBox)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.betaSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.betaSpinBox.sizePolicy().hasHeightForWidth())
        self.betaSpinBox.setSizePolicy(sizePolicy)
        self.betaSpinBox.setMaximum(1.0)
        self.betaSpinBox.setSingleStep(0.01)
        self.betaSpinBox.setProperty("value", 0.5)
        self.betaSpinBox.setObjectName("betaSpinBox")
        self.horizontalLayout_2.addWidget(self.betaSpinBox)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.evaportationRatioSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evaportationRatioSpinBox.sizePolicy().hasHeightForWidth())
        self.evaportationRatioSpinBox.setSizePolicy(sizePolicy)
        self.evaportationRatioSpinBox.setMaximum(1.0)
        self.evaportationRatioSpinBox.setSingleStep(0.01)
        self.evaportationRatioSpinBox.setProperty("value", 0.25)
        self.evaportationRatioSpinBox.setObjectName("evaportationRatioSpinBox")
        self.horizontalLayout_2.addWidget(self.evaportationRatioSpinBox)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.pheromoneZeroSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pheromoneZeroSpinBox.sizePolicy().hasHeightForWidth())
        self.pheromoneZeroSpinBox.setSizePolicy(sizePolicy)
        self.pheromoneZeroSpinBox.setMaximum(1.0)
        self.pheromoneZeroSpinBox.setSingleStep(0.01)
        self.pheromoneZeroSpinBox.setProperty("value", 0.05)
        self.pheromoneZeroSpinBox.setObjectName("pheromoneZeroSpinBox")
        self.horizontalLayout_2.addWidget(self.pheromoneZeroSpinBox)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.startNodeComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.startNodeComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.startNodeComboBox.setObjectName("startNodeComboBox")
        self.horizontalLayout_2.addWidget(self.startNodeComboBox)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.endNodeComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.endNodeComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.endNodeComboBox.setObjectName("endNodeComboBox")
        self.horizontalLayout_2.addWidget(self.endNodeComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.solveButton = QtWidgets.QPushButton(self.centralWidget)
        self.solveButton.setObjectName("solveButton")
        self.horizontalLayout_2.addWidget(self.solveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frameLabel = GraphView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameLabel.sizePolicy().hasHeightForWidth())
        self.frameLabel.setSizePolicy(sizePolicy)
        self.frameLabel.setMinimumSize(QtCore.QSize(1, 200))
        self.frameLabel.setMaximumSize(QtCore.QSize(1472, 828))
        self.frameLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frameLabel.setStyleSheet("QWidget { background:rgb(200,200,200); }")
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
        self.importButton.setText(_translate("MainWindow", "Import graph"))
        self.label_9.setText(_translate("MainWindow", "Generation interval [s]"))
        self.generationCounter.setText(_translate("MainWindow", "Current generation: 0/100"))
        self.label.setText(_translate("MainWindow", "Ants"))
        self.label_2.setText(_translate("MainWindow", "Generations"))
        self.label_3.setText(_translate("MainWindow", "α"))
        self.label_4.setText(_translate("MainWindow", "β"))
        self.label_5.setText(_translate("MainWindow", "Evaporation ratio"))
        self.label_6.setText(_translate("MainWindow", "Evaporation zero"))
        self.label_7.setText(_translate("MainWindow", "Start Node"))
        self.label_8.setText(_translate("MainWindow", "End Node"))
        self.solveButton.setText(_translate("MainWindow", "Solve"))
        self.frameLabel.setText(_translate("MainWindow", "Imported graph will be displayed here."))


from graphview import GraphView
