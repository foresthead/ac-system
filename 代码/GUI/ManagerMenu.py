# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowM(object):
    def setupUi(self, MainWindowM):
        MainWindowM.setObjectName("MainWindowM")
        MainWindowM.resize(230, 260)
        MainWindowM.setMinimumSize(QtCore.QSize(230, 260))
        MainWindowM.setMaximumSize(QtCore.QSize(230, 260))
        self.centralwidget = QtWidgets.QWidget(MainWindowM)
        self.centralwidget.setObjectName("centralwidget")
        self.PowerButton = QtWidgets.QPushButton(self.centralwidget)
        self.PowerButton.setGeometry(QtCore.QRect(150, 20, 56, 17))
        self.PowerButton.setObjectName("PowerButton")
        self.PowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.PowerLabel.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.PowerLabel.setObjectName("PowerLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 81, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelMode = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelMode.setObjectName("labelMode")
        self.verticalLayout.addWidget(self.labelMode)
        self.label_Range = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_Range.setObjectName("label_Range")
        self.verticalLayout.addWidget(self.label_Range)
        self.label_rateH = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateH.setObjectName("label_rateH")
        self.verticalLayout.addWidget(self.label_rateH)
        self.label_rateM = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateM.setObjectName("label_rateM")
        self.verticalLayout.addWidget(self.label_rateM)
        self.label_rateL = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateL.setObjectName("label_rateL")
        self.verticalLayout.addWidget(self.label_rateL)
        self.ModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ModeButton.setGeometry(QtCore.QRect(150, 70, 56, 17))
        self.ModeButton.setObjectName("ModeButton")
        self.tempSpin_min = QtWidgets.QSpinBox(self.centralwidget)
        self.tempSpin_min.setGeometry(QtCore.QRect(130, 100, 31, 16))
        self.tempSpin_min.setMinimum(16)
        self.tempSpin_min.setMaximum(28)
        self.tempSpin_min.setObjectName("tempSpin_min")
        self.tempSpin_max = QtWidgets.QSpinBox(self.centralwidget)
        self.tempSpin_max.setGeometry(QtCore.QRect(180, 100, 31, 16))
        self.tempSpin_max.setMinimum(16)
        self.tempSpin_max.setMaximum(28)
        self.tempSpin_max.setProperty("value", 28)
        self.tempSpin_max.setObjectName("tempSpin_max")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(166, 100, 20, 20))
        self.to_label.setObjectName("to_label")
        self.rmb_C_label1 = QtWidgets.QLabel(self.centralwidget)
        self.rmb_C_label1.setGeometry(QtCore.QRect(190, 130, 21, 16))
        self.rmb_C_label1.setObjectName("rmb_C_label1")
        self.rmb_C_label2 = QtWidgets.QLabel(self.centralwidget)
        self.rmb_C_label2.setGeometry(QtCore.QRect(190, 160, 21, 16))
        self.rmb_C_label2.setObjectName("rmb_C_label2")
        self.rmb_C_label3 = QtWidgets.QLabel(self.centralwidget)
        self.rmb_C_label3.setGeometry(QtCore.QRect(190, 190, 21, 16))
        self.rmb_C_label3.setObjectName("rmb_C_label3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 191, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConfirmButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.horizontalLayout.addWidget(self.ConfirmButton)
        self.BackButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BackButton.setObjectName("BackButton")
        self.horizontalLayout.addWidget(self.BackButton)
        self.rateSpin_H = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateSpin_H.setGeometry(QtCore.QRect(140, 130, 41, 20))
        self.rateSpin_H.setDecimals(1)
        self.rateSpin_H.setMinimum(0.5)
        self.rateSpin_H.setMaximum(10.0)
        self.rateSpin_H.setSingleStep(0.5)
        self.rateSpin_H.setObjectName("rateSpin_H")
        self.rateSpin_M = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateSpin_M.setGeometry(QtCore.QRect(140, 160, 41, 20))
        self.rateSpin_M.setDecimals(1)
        self.rateSpin_M.setMinimum(0.5)
        self.rateSpin_M.setMaximum(10.0)
        self.rateSpin_M.setSingleStep(0.5)
        self.rateSpin_M.setObjectName("rateSpin_M")
        self.rateSpin_L = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateSpin_L.setGeometry(QtCore.QRect(140, 190, 41, 20))
        self.rateSpin_L.setDecimals(1)
        self.rateSpin_L.setMinimum(0.5)
        self.rateSpin_L.setMaximum(10.0)
        self.rateSpin_L.setSingleStep(0.5)
        self.rateSpin_L.setObjectName("rateSpin_L")
        MainWindowM.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowM)
        QtCore.QMetaObject.connectSlotsByName(MainWindowM)

    def retranslateUi(self, MainWindowM):
        _translate = QtCore.QCoreApplication.translate
        MainWindowM.setWindowTitle(_translate("MainWindowM", "Manager menu"))
        self.PowerButton.setText(_translate("MainWindowM", "Switch"))
        self.PowerLabel.setText(_translate("MainWindowM", "Power state: ON"))
        self.labelMode.setText(_translate("MainWindowM", "Mode: Winter"))
        self.label_Range.setText(_translate("MainWindowM", "Temperature range"))
        self.label_rateH.setText(_translate("MainWindowM", "Fee rate (High)"))
        self.label_rateM.setText(_translate("MainWindowM", "Fee rate (Medium)"))
        self.label_rateL.setText(_translate("MainWindowM", "Fee rate (Low)"))
        self.ModeButton.setText(_translate("MainWindowM", "Switch"))
        self.to_label.setText(_translate("MainWindowM", "to"))
        self.rmb_C_label1.setText(_translate("MainWindowM", "元/1C°"))
        self.rmb_C_label2.setText(_translate("MainWindowM", "元/1C°"))
        self.rmb_C_label3.setText(_translate("MainWindowM", "元/1C°"))
        self.ConfirmButton.setText(_translate("MainWindowM", "Confirm"))
        self.BackButton.setText(_translate("MainWindowM", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowM = QtWidgets.QMainWindow()
    ui = Ui_MainWindowM()
    ui.setupUi(MainWindowM)
    MainWindowM.show()
    sys.exit(app.exec_())
