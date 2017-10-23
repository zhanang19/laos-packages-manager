# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(562, 563)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pentestBtn = QtGui.QPushButton(self.centralwidget)
        self.pentestBtn.setGeometry(QtCore.QRect(120, 240, 151, 31))
        self.pentestBtn.setObjectName(_fromUtf8("pentestBtn"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 140, 91, 91))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/2scl.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 290, 91, 91))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/3scl.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 290, 91, 91))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("img/4scl.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 140, 91, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img/1scl.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.studentBtn = QtGui.QPushButton(self.centralwidget)
        self.studentBtn.setGeometry(QtCore.QRect(290, 240, 151, 32))
        self.studentBtn.setObjectName(_fromUtf8("studentBtn"))
        self.devBtn = QtGui.QPushButton(self.centralwidget)
        self.devBtn.setGeometry(QtCore.QRect(120, 390, 151, 32))
        self.devBtn.setObjectName(_fromUtf8("devBtn"))
        self.designBtn = QtGui.QPushButton(self.centralwidget)
        self.designBtn.setGeometry(QtCore.QRect(290, 390, 151, 32))
        self.designBtn.setObjectName(_fromUtf8("designBtn"))
        self.welcome = QtGui.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(100, 10, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.welcome.setFont(font)
        self.welcome.setObjectName(_fromUtf8("welcome"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 80, 251, 20))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 500, 251, 50))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LaOS Package Manager", None))
        self.pentestBtn.setText(_translate("MainWindow", "install Pentest Pack", None))
        self.studentBtn.setText(_translate("MainWindow", "install Student Pack", None))
        self.devBtn.setText(_translate("MainWindow", "install Dev Pack", None))
        self.designBtn.setText(_translate("MainWindow", "install Design Pack", None))
        self.welcome.setText(_translate("MainWindow", "Welcome To Laos Package Manager", None))
        self.label_6.setText(_translate("MainWindow", "#weGiveSpecialPackForYou", None))
        self.label_7.setText(_translate("MainWindow", "Status", None))
