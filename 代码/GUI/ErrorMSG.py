# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorMSG.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorPopup(object):
    def setupUi(self, ErrorPopup):
        ErrorPopup.setObjectName("ErrorPopup")
        ErrorPopup.resize(150, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorPopup.sizePolicy().hasHeightForWidth())
        ErrorPopup.setSizePolicy(sizePolicy)
        ErrorPopup.setMinimumSize(QtCore.QSize(150, 50))
        ErrorPopup.setMaximumSize(QtCore.QSize(150, 50))
        self.centralwidget = QtWidgets.QWidget(ErrorPopup)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        ErrorPopup.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorPopup)
        QtCore.QMetaObject.connectSlotsByName(ErrorPopup)

    def retranslateUi(self, ErrorPopup):
        _translate = QtCore.QCoreApplication.translate
        ErrorPopup.setWindowTitle(_translate("ErrorPopup", "Error"))
        self.label.setText(_translate("ErrorPopup", "Error!"))
        self.pushButton.setText(_translate("ErrorPopup", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorPopup = QtWidgets.QMainWindow()
    ui = Ui_ErrorPopup()
    ui.setupUi(ErrorPopup)
    ErrorPopup.show()
    sys.exit(app.exec_())
