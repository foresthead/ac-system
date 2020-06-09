# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReceptionMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui_MainWindowR(object):
    def setupUi(self, MainWindowR):
        MainWindowR.setObjectName("MainWindowR")
        MainWindowR.resize(230, 190)
        MainWindowR.setMinimumSize(QtCore.QSize(230, 190))
        self.centralwidget = QtWidgets.QWidget(MainWindowR)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.RDRbutton = QtWidgets.QPushButton(self.centralwidget)
        self.RDRbutton.setObjectName("RDRbutton")
        self.verticalLayout.addWidget(self.RDRbutton)
        self.InvoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.InvoiceButton.setObjectName("InvoiceButton")
        self.verticalLayout.addWidget(self.InvoiceButton)
        self.BackButtonR = QtWidgets.QPushButton(self.centralwidget)
        self.BackButtonR.setObjectName("BackButtonR")
        self.verticalLayout.addWidget(self.BackButtonR)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindowR.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowR)
        QtCore.QMetaObject.connectSlotsByName(MainWindowR)

    def retranslateUi(self, MainWindowR):
        _translate = QtCore.QCoreApplication.translate
        MainWindowR.setWindowTitle(_translate("MainWindowR", "Reception Menu"))
        self.textBrowser.setHtml(_translate("MainWindowR", "Detailed record or invoice will appear here..."))
        self.RDRbutton.setText(_translate("MainWindowR", "Detailed record"))
        self.InvoiceButton.setText(_translate("MainWindowR", "Invoice"))
        self.BackButtonR.setText(_translate("MainWindowR", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowR = QtWidgets.QMainWindow()
    ui = Ui_MainWindowR()
    ui.setupUi(MainWindowR)
    MainWindowR.show()
    sys.exit(app.exec_())
