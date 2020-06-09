# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui_MainWindowAdmin(object):
    def setupUi(self, MainWindowAdmin):
        MainWindowAdmin.setObjectName("MainWindowAdmin")
        MainWindowAdmin.resize(270, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindowAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 140, 251, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonMonth = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonMonth.setObjectName("ButtonMonth")
        self.gridLayout.addWidget(self.ButtonMonth, 1, 0, 1, 1)
        self.ButtonWeek = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonWeek.setObjectName("ButtonWeek")
        self.gridLayout.addWidget(self.ButtonWeek, 0, 1, 1, 1)
        self.ButtonYear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonYear.setObjectName("ButtonYear")
        self.gridLayout.addWidget(self.ButtonYear, 1, 1, 1, 1)
        self.ButtonDaily = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonDaily.setObjectName("ButtonDaily")
        self.gridLayout.addWidget(self.ButtonDaily, 0, 0, 1, 1)
        self.ButtonBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonBack.setObjectName("ButtonBack")
        self.gridLayout.addWidget(self.ButtonBack, 2, 1, 1, 1)
        self.ButtonPrint = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonPrint.setObjectName("ButtonPrint")
        self.gridLayout.addWidget(self.ButtonPrint, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 251, 121))
        self.textBrowser.setObjectName("textBrowser")
        MainWindowAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowAdmin)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAdmin)

    def retranslateUi(self, MainWindowAdmin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowAdmin.setWindowTitle(_translate("MainWindowAdmin", "Administrator Menu"))
        self.textBrowser.setHtml(_translate("MainWindowR", "The report will appear here..."))
        self.ButtonMonth.setText(_translate("MainWindowAdmin", "Month report"))
        self.ButtonWeek.setText(_translate("MainWindowAdmin", "Week report"))
        self.ButtonYear.setText(_translate("MainWindowAdmin", "Year report"))
        self.ButtonDaily.setText(_translate("MainWindowAdmin", "Daily report"))
        self.ButtonBack.setText(_translate("MainWindowAdmin", "Back"))
        self.ButtonPrint.setText(_translate("MainWindowAdmin", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowAdmin = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAdmin()
    ui.setupUi(MainWindowAdmin)
    MainWindowAdmin.show()
    sys.exit(app.exec_())
