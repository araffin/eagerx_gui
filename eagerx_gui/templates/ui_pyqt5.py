"""
 Mostly copy paste from https://github.com/pyqtgraph/pyqtgraph/blob/master/pyqtgraph/flowchart/FlowchartCtrlTemplate_pyqt5.py
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(217, 499)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.loadBtn = QtWidgets.QPushButton(Form)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 1, 0, 1, 1)
        self.saveBtn = FeedbackButton(Form)
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout.addWidget(self.saveBtn, 1, 1, 1, 2)
        self.saveAsBtn = FeedbackButton(Form)
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.gridLayout.addWidget(self.saveAsBtn, 1, 3, 1, 1)
        self.checkValidityBtn = FeedbackButton(Form)
        self.checkValidityBtn.setObjectName("checkValidityBtn")
        self.gridLayout.addWidget(self.checkValidityBtn, 4, 0, 1, 1)
        self.showChartBtn = QtWidgets.QPushButton(Form)
        self.showChartBtn.setCheckable(True)
        self.showChartBtn.setObjectName("showChartBtn")
        self.gridLayout.addWidget(self.showChartBtn, 4, 3, 1, 1)
        # self.showCompatibleBridgesBtn = QtWidgets.QPushButton(Form)
        # self.showCompatibleBridgesBtn.setObjectName("showCompatibleBridgesBtn")
        # self.gridLayout.addWidget(self.showCompatibleBridgesBtn, 4, 3, 1, 1)
        self.ctrlList = TreeWidget(Form)
        self.ctrlList.setObjectName("ctrlList")
        self.ctrlList.headerItem().setText(0, "1")
        self.ctrlList.header().setVisible(False)
        self.ctrlList.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.ctrlList, 3, 0, 1, 4)
        self.fileNameLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setText("")
        self.fileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EAGERx"))
        self.loadBtn.setText(_translate("Form", "Load.."))
        self.saveBtn.setText(_translate("Form", "Save"))
        self.saveAsBtn.setText(_translate("Form", "As.."))
        self.checkValidityBtn.setText(_translate("Form", "Check Validity"))
        self.showChartBtn.setText(_translate("Form", "Show Graph"))
        # self.showCompatibleBridgesBtn.setText(_translate("Form", "Compatible Bridges"))


from pyqtgraph.widgets.FeedbackButton import FeedbackButton
from pyqtgraph.widgets.TreeWidget import TreeWidget
