# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Mon Jun 10 18:35:28 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 1280)
        MainWindow.setMaximumSize(QtCore.QSize(720, 1280))
        MainWindow.setStyleSheet("background-image: url(\'/home/isaque/Documents/projetos/ensaio/app_source/imagens/instrumentos/violino2.jpg\');\n"
"background-size: 100%, 100%;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 70, 191, 61))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 90);\n"
"border: 0px;\n"
"")
        self.pushButton.setShortcut("")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 160, 191, 61))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 90);\n"
"border: 0px;\n"
"")
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Relatório de Comparecimento", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Relatório de Comparecimento", None, -1))

