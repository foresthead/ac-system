# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuestMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui_MaiMenuG(object):
    def setupUi(self, MaiMenuG):
        MaiMenuG.setObjectName("MaiMenuG")
        MaiMenuG.resize(180, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(MaiMenuG.sizePolicy().hasHeightForWidth())
        MaiMenuG.setSizePolicy(sizePolicy)
        MaiMenuG.setMinimumSize(QtCore.QSize(180, 210))
        MaiMenuG.setMaximumSize(QtCore.QSize(180, 210))
        self.centralwidget = QtWidgets.QWidget(MaiMenuG)
        self.centralwidget.setObjectName("centralwidget")
        self.TempBox = QtWidgets.QSpinBox(self.centralwidget)
        self.TempBox.setGeometry(QtCore.QRect(120, 80, 42, 22))
        self.TempBox.setMinimum(16)
        self.TempBox.setMaximum(24)
        self.TempBox.setProperty("value", 24)
        self.TempBox.setObjectName("TempBox")
        self.TemperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.TemperatureLabel.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.TemperatureLabel.setObjectName("TemperatureLabel")
        self.SpeedSlider = QtWidgets.QSlider(self.centralwidget)
        self.SpeedSlider.setGeometry(QtCore.QRect(140, 110, 20, 31))
        self.SpeedSlider.setMaximum(2)
        self.SpeedSlider.setOrientation(QtCore.Qt.Vertical)
        self.SpeedSlider.setObjectName("SpeedSlider")
        self.WindSpeed = QtWidgets.QLabel(self.centralwidget)
        self.WindSpeed.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.WindSpeed.setObjectName("WindSpeed")
        self.PowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.PowerLabel.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.PowerLabel.setObjectName("PowerLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 141, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SetButton.setObjectName("SetButton")
        self.horizontalLayout.addWidget(self.SetButton)
        self.CloseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton)
        self.OnOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.OnOffButton.setGeometry(QtCore.QRect(120, 20, 41, 20))
        self.OnOffButton.setObjectName("OnOffButton")
        MaiMenuG.setCentralWidget(self.centralwidget)

        self.retranslateUi(MaiMenuG)
        QtCore.QMetaObject.connectSlotsByName(MaiMenuG)

    def retranslateUi(self, MaiMenuG):
        _translate = QtCore.QCoreApplication.translate
        MaiMenuG.setWindowTitle(_translate("MaiMenuG", "Guest Menu"))
        self.TemperatureLabel.setText(_translate("MaiMenuG", "Temperature"))
        self.WindSpeed.setText(_translate("MaiMenuG", "Wind Speed：Low"))
        self.PowerLabel.setText(_translate("MaiMenuG", "Power: OFF"))
        self.SetButton.setText(_translate("MaiMenuG", "Set"))
        self.CloseButton.setText(_translate("MaiMenuG", "Close"))
        self.OnOffButton.setText(_translate("MaiMenuG", "Switch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MaiMenuG = QtWidgets.QMainWindow()
    ui = Ui_MaiMenuG()
    ui.setupUi(MaiMenuG)
    MaiMenuG.show()
    sys.exit(app.exec_())
