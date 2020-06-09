# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RDRoutput.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutputWindowR(object):
    def setupUi(self, OutputWindowR):
        OutputWindowR.setObjectName("OutputWindowR")
        OutputWindowR.resize(170, 60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OutputWindowR.sizePolicy().hasHeightForWidth())
        OutputWindowR.setSizePolicy(sizePolicy)
        OutputWindowR.setMinimumSize(QtCore.QSize(170, 60))
        OutputWindowR.setMaximumSize(QtCore.QSize(170, 60))
        self.centralwidget = QtWidgets.QWidget(OutputWindowR)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SelectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectionLabel.setObjectName("SelectionLabel")
        self.verticalLayout.addWidget(self.SelectionLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OnScreenButton = QtWidgets.QPushButton(self.centralwidget)
        self.OnScreenButton.setObjectName("OnScreenButton")
        self.horizontalLayout.addWidget(self.OnScreenButton)
        self.PrintButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrintButton.setObjectName("PrintButton")
        self.horizontalLayout.addWidget(self.PrintButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        OutputWindowR.setCentralWidget(self.centralwidget)

        self.retranslateUi(OutputWindowR)
        QtCore.QMetaObject.connectSlotsByName(OutputWindowR)

    def retranslateUi(self, OutputWindowR):
        _translate = QtCore.QCoreApplication.translate
        OutputWindowR.setWindowTitle(_translate("OutputWindowR", "Detailed Record Output"))
        self.SelectionLabel.setText(_translate("OutputWindowR", "Please, select the output type:"))
        self.OnScreenButton.setText(_translate("OutputWindowR", "On Screen"))
        self.PrintButton.setText(_translate("OutputWindowR", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindowR = QtWidgets.QMainWindow()
    ui = Ui_OutputWindowR()
    ui.setupUi(OutputWindowR)
    OutputWindowR.show()
    sys.exit(app.exec_())
