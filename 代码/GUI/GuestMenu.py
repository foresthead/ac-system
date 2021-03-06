# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuestUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 424)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(389, 424))
        MainWindow.setMaximumSize(QtCore.QSize(389, 424))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Ac_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.Ac_settings.setGeometry(QtCore.QRect(10, 280, 371, 131))
        self.Ac_settings.setObjectName("Ac_settings")
        self.Power_btn = QtWidgets.QPushButton(self.Ac_settings)
        self.Power_btn.setGeometry(QtCore.QRect(300, 80, 61, 41))
        self.Power_btn.setObjectName("Power_btn")
        self.tem = QtWidgets.QGroupBox(self.Ac_settings)
        self.tem.setGeometry(QtCore.QRect(10, 30, 120, 80))
        self.tem.setObjectName("tem")
        self.TempUp_btn = QtWidgets.QPushButton(self.tem)
        self.TempUp_btn.setGeometry(QtCore.QRect(30, 20, 56, 17))
        self.TempUp_btn.setObjectName("TempUp_btn")
        self.TempDown_btn = QtWidgets.QPushButton(self.tem)
        self.TempDown_btn.setGeometry(QtCore.QRect(30, 50, 56, 17))
        self.TempDown_btn.setObjectName("TempDown_btn")
        self.windspeed = QtWidgets.QGroupBox(self.Ac_settings)
        self.windspeed.setGeometry(QtCore.QRect(150, 30, 120, 80))
        self.windspeed.setObjectName("windspeed")
        self.WindSpeed_Up = QtWidgets.QPushButton(self.windspeed)
        self.WindSpeed_Up.setGeometry(QtCore.QRect(30, 20, 56, 17))
        self.WindSpeed_Up.setObjectName("WindSpeed_Up")
        self.Windspeed_Down = QtWidgets.QPushButton(self.windspeed)
        self.Windspeed_Down.setGeometry(QtCore.QRect(30, 50, 56, 17))
        self.Windspeed_Down.setObjectName("Windspeed_Down")
        self.Mode_btn = QtWidgets.QPushButton(self.Ac_settings)
        self.Mode_btn.setGeometry(QtCore.QRect(300, 30, 61, 21))
        self.Mode_btn.setObjectName("Mode_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 371, 271))
        self.widget.setObjectName("widget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 371, 151))
        self.lcdNumber.setObjectName("lcdNumber")
        self.currentfee_label = QtWidgets.QLabel(self.widget)
        self.currentfee_label.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.currentfee_label.setObjectName("currentfee_label")
        self.targetTemp_label = QtWidgets.QLabel(self.widget)
        self.targetTemp_label.setGeometry(QtCore.QRect(10, 180, 91, 16))
        self.targetTemp_label.setObjectName("targetTemp_label")
        self.RunningTime_label = QtWidgets.QLabel(self.widget)
        self.RunningTime_label.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.RunningTime_label.setObjectName("RunningTime_label")
        self.currentFee_value = QtWidgets.QLabel(self.widget)
        self.currentFee_value.setGeometry(QtCore.QRect(330, 160, 31, 16))
        self.currentFee_value.setObjectName("currentFee_value")
        self.targetTemp_value = QtWidgets.QLabel(self.widget)
        self.targetTemp_value.setGeometry(QtCore.QRect(330, 180, 31, 16))
        self.targetTemp_value.setObjectName("targetTemp_value")
        self.runningTime_value = QtWidgets.QLabel(self.widget)
        self.runningTime_value.setGeometry(QtCore.QRect(330, 200, 31, 16))
        self.runningTime_value.setObjectName("runningTime_value")
        self.WindSpeed_label = QtWidgets.QLabel(self.widget)
        self.WindSpeed_label.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.WindSpeed_label.setObjectName("WindSpeed_label")
        self.WindSpeed_value = QtWidgets.QLabel(self.widget)
        self.WindSpeed_value.setGeometry(QtCore.QRect(330, 220, 21, 16))
        self.WindSpeed_value.setObjectName("WindSpeed_value")
        self.Mode_label = QtWidgets.QLabel(self.widget)
        self.Mode_label.setGeometry(QtCore.QRect(10, 240, 51, 16))
        self.Mode_label.setObjectName("Mode_label")
        self.Mode_value = QtWidgets.QLabel(self.widget)
        self.Mode_value.setGeometry(QtCore.QRect(330, 240, 26, 16))
        self.Mode_value.setObjectName("Mode_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.currentTemp = 0

        #--------------------------------------------------button events----------------------------------------
        self.TempUp_btn.clicked.connect(self.increaseTemp)
        self.TempDown_btn.clicked.connect(self.decreaseTemp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #---------------------------------------Events----------------------------------------------------------
    def increaseTemp(self):
            self.lcdNumber.display(self.currentTemp + 1)
            self.currentTemp += 1

    def decreaseTemp(self):
            self.lcdNumber.display(self.currentTemp - 1)
            self.currentTemp -= 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Ac_settings.setTitle(_translate("MainWindow", "Ac Settings"))
        self.Power_btn.setText(_translate("MainWindow", "Power"))
        self.tem.setTitle(_translate("MainWindow", "Temp"))
        self.TempUp_btn.setText(_translate("MainWindow", "UP"))
        self.TempDown_btn.setText(_translate("MainWindow", "DOWN"))
        self.windspeed.setTitle(_translate("MainWindow", "WindSpeed"))
        self.WindSpeed_Up.setText(_translate("MainWindow", "UP"))
        self.Windspeed_Down.setText(_translate("MainWindow", "DOWN"))
        self.Mode_btn.setText(_translate("MainWindow", "Mode"))
        self.currentfee_label.setText(_translate("MainWindow", "Current Fee :"))
        self.targetTemp_label.setText(_translate("MainWindow", "Target Room Temp :"))
        self.RunningTime_label.setText(_translate("MainWindow", "Running Time :"))
        self.currentFee_value.setText(_translate("MainWindow", "0.0"))
        self.targetTemp_value.setText(_translate("MainWindow", "32"))
        self.runningTime_value.setText(_translate("MainWindow", "23:4"))
        self.WindSpeed_label.setText(_translate("MainWindow", "Wind Speed :"))
        self.WindSpeed_value.setText(_translate("MainWindow", "H"))
        self.Mode_label.setText(_translate("MainWindow", "Mode :"))
        self.Mode_value.setText(_translate("MainWindow", "COLD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





'''# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COMMONMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Ui_HotelMenu(object):
    def setupUi(self, HotelMenu):
        HotelMenu.setObjectName("HotelMenu")
        HotelMenu.resize(450, 470)
        HotelMenu.setMinimumSize(QtCore.QSize(450, 470))
        HotelMenu.setMaximumSize(QtCore.QSize(450, 470))
        self.centralwidget = QtWidgets.QWidget(HotelMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        self.labelMain.setGeometry(QtCore.QRect(270, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(26)
        self.labelMain.setFont(font)
        self.labelMain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain.setObjectName("labelMain")
        self.frameManager = QtWidgets.QFrame(self.centralwidget)
        self.frameManager.setGeometry(QtCore.QRect(0, 10, 231, 251))
        self.frameManager.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameManager.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameManager.setObjectName("frameManager")
        self.rateSpin_L = QtWidgets.QDoubleSpinBox(self.frameManager)
        self.rateSpin_L.setGeometry(QtCore.QRect(140, 190, 41, 20))
        self.rateSpin_L.setDecimals(1)
        self.rateSpin_L.setMinimum(0.5)
        self.rateSpin_L.setMaximum(10.0)
        self.rateSpin_L.setSingleStep(0.5)
        self.rateSpin_L.setObjectName("rateSpin_L")
        self.PowerButton = QtWidgets.QPushButton(self.frameManager)
        self.PowerButton.setGeometry(QtCore.QRect(150, 20, 56, 17))
        self.PowerButton.setObjectName("PowerButton")
        self.PowerLabel = QtWidgets.QLabel(self.frameManager)
        self.PowerLabel.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.PowerLabel.setObjectName("PowerLabel")
        self.line = QtWidgets.QFrame(self.frameManager)
        self.line.setGeometry(QtCore.QRect(20, 50, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tempSpin_min = QtWidgets.QSpinBox(self.frameManager)
        self.tempSpin_min.setGeometry(QtCore.QRect(130, 100, 31, 16))
        self.tempSpin_min.setMinimum(16)
        self.tempSpin_min.setMaximum(28)
        self.tempSpin_min.setObjectName("tempSpin_min")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frameManager)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 81, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelMode_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelMode_2.setObjectName("labelMode_2")
        self.verticalLayout_2.addWidget(self.labelMode_2)
        self.label_Range_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_Range_2.setObjectName("label_Range_2")
        self.verticalLayout_2.addWidget(self.label_Range_2)
        self.label_rateH_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateH_2.setObjectName("label_rateH_2")
        self.verticalLayout_2.addWidget(self.label_rateH_2)
        self.label_rateM_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateM_2.setObjectName("label_rateM_2")
        self.verticalLayout_2.addWidget(self.label_rateM_2)
        self.label_rateL_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rateL_2.setObjectName("label_rateL_2")
        self.verticalLayout_2.addWidget(self.label_rateL_2)
        self.rateSpin_H = QtWidgets.QDoubleSpinBox(self.frameManager)
        self.rateSpin_H.setGeometry(QtCore.QRect(140, 130, 41, 20))
        self.rateSpin_H.setDecimals(1)
        self.rateSpin_H.setMinimum(0.5)
        self.rateSpin_H.setMaximum(10.0)
        self.rateSpin_H.setSingleStep(0.5)
        self.rateSpin_H.setObjectName("rateSpin_H")
        self.rateSpin_M = QtWidgets.QDoubleSpinBox(self.frameManager)
        self.rateSpin_M.setGeometry(QtCore.QRect(140, 160, 41, 20))
        self.rateSpin_M.setDecimals(1)
        self.rateSpin_M.setMinimum(0.5)
        self.rateSpin_M.setMaximum(10.0)
        self.rateSpin_M.setSingleStep(0.5)
        self.rateSpin_M.setObjectName("rateSpin_M")
        self.to_label = QtWidgets.QLabel(self.frameManager)
        self.to_label.setGeometry(QtCore.QRect(166, 100, 20, 20))
        self.to_label.setObjectName("to_label")
        self.ModeButton = QtWidgets.QPushButton(self.frameManager)
        self.ModeButton.setGeometry(QtCore.QRect(150, 70, 56, 17))
        self.ModeButton.setObjectName("ModeButton")
        self.rmb_C_label2 = QtWidgets.QLabel(self.frameManager)
        self.rmb_C_label2.setGeometry(QtCore.QRect(190, 160, 21, 16))
        self.rmb_C_label2.setObjectName("rmb_C_label2")
        self.tempSpin_max = QtWidgets.QSpinBox(self.frameManager)
        self.tempSpin_max.setGeometry(QtCore.QRect(180, 100, 31, 16))
        self.tempSpin_max.setMinimum(16)
        self.tempSpin_max.setMaximum(28)
        self.tempSpin_max.setProperty("value", 28)
        self.tempSpin_max.setObjectName("tempSpin_max")
        self.rmb_C_label1 = QtWidgets.QLabel(self.frameManager)
        self.rmb_C_label1.setGeometry(QtCore.QRect(190, 130, 21, 16))
        self.rmb_C_label1.setObjectName("rmb_C_label1")
        self.rmb_C_label3 = QtWidgets.QLabel(self.frameManager)
        self.rmb_C_label3.setGeometry(QtCore.QRect(190, 190, 21, 16))
        self.rmb_C_label3.setObjectName("rmb_C_label3")
        self.ConfirmButton_2 = QtWidgets.QPushButton(self.frameManager)
        self.ConfirmButton_2.setGeometry(QtCore.QRect(20, 220, 189, 17))
        self.ConfirmButton_2.setObjectName("ConfirmButton_2")
        self.groupBox_manager = QtWidgets.QGroupBox(self.frameManager)
        self.groupBox_manager.setGeometry(QtCore.QRect(10, 0, 211, 251))
        self.groupBox_manager.setObjectName("groupBox_manager")
        self.groupBox_manager.raise_()
        self.rateSpin_L.raise_()
        self.PowerButton.raise_()
        self.PowerLabel.raise_()
        self.line.raise_()
        self.tempSpin_min.raise_()
        self.verticalLayoutWidget.raise_()
        self.rateSpin_H.raise_()
        self.rateSpin_M.raise_()
        self.to_label.raise_()
        self.ModeButton.raise_()
        self.rmb_C_label2.raise_()
        self.tempSpin_max.raise_()
        self.rmb_C_label1.raise_()
        self.rmb_C_label3.raise_()
        self.ConfirmButton_2.raise_()
        self.frameReception = QtWidgets.QFrame(self.centralwidget)
        self.frameReception.setGeometry(QtCore.QRect(0, 260, 231, 211))
        self.frameReception.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameReception.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameReception.setObjectName("frameReception")
        self.textBrowser = QtWidgets.QTextBrowser(self.frameReception)
        self.textBrowser.setGeometry(QtCore.QRect(20, 31, 191, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.frameReception)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 191, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InvoiceButton = QtWidgets.QPushButton(self.frameReception)
        self.InvoiceButton.setGeometry(QtCore.QRect(21, 152, 189, 17))
        self.InvoiceButton.setObjectName("InvoiceButton")
        self.RDRbutton = QtWidgets.QPushButton(self.frameReception)
        self.RDRbutton.setGeometry(QtCore.QRect(21, 131, 189, 17))
        self.RDRbutton.setObjectName("RDRbutton")
        self.RDRPrintButton = QtWidgets.QPushButton(self.frameReception)
        self.RDRPrintButton.setGeometry(QtCore.QRect(21, 173, 189, 17))
        self.RDRPrintButton.setObjectName("RDRPrintButton")
        self.groupBox_reception = QtWidgets.QGroupBox(self.frameReception)
        self.groupBox_reception.setGeometry(QtCore.QRect(10, 10, 211, 191))
        self.groupBox_reception.setObjectName("groupBox_reception")
        self.groupBox_reception.raise_()
        self.textBrowser.raise_()
        self.layoutWidget.raise_()
        self.InvoiceButton.raise_()
        self.RDRbutton.raise_()
        self.RDRPrintButton.raise_()
        self.frameAdmin = QtWidgets.QFrame(self.centralwidget)
        self.frameAdmin.setGeometry(QtCore.QRect(240, 210, 211, 251))
        self.frameAdmin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAdmin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAdmin.setObjectName("frameAdmin")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frameAdmin)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 181, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frameAdmin)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 170, 181, 80))
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
        self.ButtonPrint = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonPrint.setObjectName("ButtonPrint")
        self.gridLayout.addWidget(self.ButtonPrint, 2, 0, 1, 1)
        self.groupBox_admin = QtWidgets.QGroupBox(self.frameAdmin)
        self.groupBox_admin.setGeometry(QtCore.QRect(0, 10, 201, 241))
        self.groupBox_admin.setObjectName("groupBox_admin")
        self.groupBox_admin.raise_()
        self.textBrowser_2.raise_()
        self.gridLayoutWidget.raise_()
        self.spinID = QtWidgets.QSpinBox(self.centralwidget)
        self.spinID.setGeometry(QtCore.QRect(250, 30, 191, 19))
        self.spinID.setMinimum(1)
        self.spinID.setMaximum(5)
        self.spinID.setObjectName("spinID")
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        self.labelID.setGeometry(QtCore.QRect(250, 10, 191, 16))
        self.labelID.setObjectName("labelID")
        HotelMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(HotelMenu)
        QtCore.QMetaObject.connectSlotsByName(HotelMenu)

    def retranslateUi(self, HotelMenu):
        _translate = QtCore.QCoreApplication.translate
        HotelMenu.setWindowTitle(_translate("HotelMenu", "Hotel Menu"))
        self.labelMain.setText(_translate("HotelMenu", "ACC SYSTEM"))
        self.PowerButton.setText(_translate("HotelMenu", "Switch"))
        self.PowerLabel.setText(_translate("HotelMenu", "Power state: ON"))
        self.labelMode_2.setText(_translate("HotelMenu", "Mode: Winter"))
        self.label_Range_2.setText(_translate("HotelMenu", "Temperature range"))
        self.label_rateH_2.setText(_translate("HotelMenu", "Fee rate (High)"))
        self.label_rateM_2.setText(_translate("HotelMenu", "Fee rate (Medium)"))
        self.label_rateL_2.setText(_translate("HotelMenu", "Fee rate (Low)"))
        self.to_label.setText(_translate("HotelMenu", "to"))
        self.ModeButton.setText(_translate("HotelMenu", "Switch"))
        self.rmb_C_label2.setText(_translate("HotelMenu", "元/1C°"))
        self.rmb_C_label1.setText(_translate("HotelMenu", "元/1C°"))
        self.rmb_C_label3.setText(_translate("HotelMenu", "元/1C°"))
        self.ConfirmButton_2.setText(_translate("HotelMenu", "Confirm"))
        self.groupBox_manager.setTitle(_translate("HotelMenu", "Manager"))
        self.textBrowser.setHtml(_translate("MainWindowR", "Invoice/RDR:"))
        self.InvoiceButton.setText(_translate("HotelMenu", "Invoice"))
        self.RDRbutton.setText(_translate("HotelMenu", "Detailed record"))
        self.RDRPrintButton.setText(_translate("HotelMenu", "Print detailed record"))
        self.groupBox_reception.setTitle(_translate("HotelMenu", "Reception"))
        self.ButtonMonth.setText(_translate("HotelMenu", "Month report"))
        self.ButtonWeek.setText(_translate("HotelMenu", "Week report"))
        self.ButtonYear.setText(_translate("HotelMenu", "Year report"))
        self.ButtonDaily.setText(_translate("HotelMenu", "Daily report"))
        self.ButtonPrint.setText(_translate("HotelMenu", "Print"))
        self.groupBox_admin.setTitle(_translate("HotelMenu", "Administrator"))
        self.labelID.setText(_translate("HotelMenu", "Room ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HotelMenu = QtWidgets.QMainWindow()
    ui = Ui_HotelMenu()
    ui.setupUi(HotelMenu)
    HotelMenu.show()
    sys.exit(app.exec_())'''
