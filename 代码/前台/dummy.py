#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets

class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonPrint = QtGui.QPushButton(self)
        self.pushButtonPrint.setText("Click Me!")
        self.pushButtonPrint.clicked.connect(self.on_pushButtonPrint_clicked)

        self.textEdit = QtGui.QTextEdit(self)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPrint)
        self.layoutVertical.addWidget(self.textEdit)

    @QtCore.pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        print("Button Clicked!")

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    myStream = MyStream()
    myStream.message.connect(main.on_myStream_message)

    sys.stdout = myStream
    sys.exit(app.exec_())