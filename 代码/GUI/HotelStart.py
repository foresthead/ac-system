# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HotelStart.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(150, 150)
        MainWindow.setMinimumSize(QtCore.QSize(150, 150))
        MainWindow.setMaximumSize(QtCore.QSize(150, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(150, 110))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 111, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonR = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonR.setObjectName("ButtonR")
        self.verticalLayout.addWidget(self.ButtonR)
        self.ButtonM = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonM.setObjectName("ButtonM")
        self.verticalLayout.addWidget(self.ButtonM)
        self.ButtonA = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonA.setObjectName("ButtonA")
        self.verticalLayout.addWidget(self.ButtonA)
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        self.labelMain.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(22)
        self.labelMain.setFont(font)
        self.labelMain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain.setObjectName("labelMain")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACC SYSTEM"))
        self.ButtonR.setText(_translate("MainWindow", "Reception"))
        self.ButtonM.setText(_translate("MainWindow", "Manager"))
        self.ButtonA.setText(_translate("MainWindow", "Administrator"))
        self.labelMain.setText(_translate("MainWindow", "ACC SYSTEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
