# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'install.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BrowserWindow(object):
    def setupUi(self, BrowserWindow):
        BrowserWindow.setObjectName(_fromUtf8("BrowserWindow"))
        BrowserWindow.resize(429, 396)
        self.centralwidget = QtGui.QWidget(BrowserWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 361, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 110, 261, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 103, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 180, 361, 121))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 101, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        BrowserWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BrowserWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BrowserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(BrowserWindow)

    def retranslateUi(self, BrowserWindow):
        BrowserWindow.setWindowTitle(_translate("BrowserWindow", "MainWindow", None))
        self.pushButton.setText(_translate("BrowserWindow", "Install", None))
        self.pushButton_2.setText(_translate("BrowserWindow", "browse", None))
        self.label_2.setText(_translate("BrowserWindow", "File Paket", None))
        self.label_3.setText(_translate("BrowserWindow", "Install Paket", None))
        self.label_4.setText(_translate("BrowserWindow", "Folder Tujuan", None))

