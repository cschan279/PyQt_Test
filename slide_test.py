# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slide_test.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = CustomSlider(self.centralwidget)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(100, 255, 100, 255));\n"
"    border: 0px solid #424242; \n"
"    height: 10px; \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: blue;\n"
"    border: 0px solid black; \n"
"    width: 10px; \n"
"    height: 6px; \n"
"    line-height: 6px; \n"
"    margin-top: -2px; \n"
"    margin-bottom: -2px; \n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 5px;\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


from customslider import CustomSlider
