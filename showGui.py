# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiV2.ui'
#
# Created: Tue Jan 12 18:51:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import sys
import random
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 240)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Temp_Bar = QtGui.QProgressBar(self.centralwidget)
        self.Temp_Bar.setGeometry(QtCore.QRect(280, 20, 51, 151))
        self.Temp_Bar.setProperty("value", 24)
        self.Temp_Bar.setOrientation(QtCore.Qt.Vertical)
        self.Temp_Bar.setInvertedAppearance(False)
        self.Temp_Bar.setObjectName("Temp_Bar")
        self.RPM_LCD = QtGui.QLCDNumber(self.centralwidget)
        self.RPM_LCD.setGeometry(QtCore.QRect(10, 185, 71, 31))
        self.RPM_LCD.setProperty("intValue", 0)
        self.RPM_LCD.setObjectName("RPM_LCD")
        self.Current_LCD = QtGui.QLCDNumber(self.centralwidget)
        self.Current_LCD.setGeometry(QtCore.QRect(90, 185, 71, 31))
        self.Current_LCD.setObjectName("Current_LCD")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(33, 174, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 174, 47, 13))
        self.label_2.setObjectName("label_2")
        self.Battery_Bar = QtGui.QProgressBar(self.centralwidget)
        self.Battery_Bar.setGeometry(QtCore.QRect(260, 190, 81, 23))
        self.Battery_Bar.setProperty("value", 24)
        self.Battery_Bar.setObjectName("Battery_Bar")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(189, 174, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Voltage_LCD = QtGui.QLCDNumber(self.centralwidget)
        self.Voltage_LCD.setGeometry(QtCore.QRect(170, 185, 71, 31))
        self.Voltage_LCD.setObjectName("Voltage_LCD")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(265, 174, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 0, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 261, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("speedometer.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 41, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDefault(False)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 60, 47, 13))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("released()"), self.updateUi)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateUi(self):
        self.Temp_Bar.setValue(random.randint(0,100))
        self.Battery_Bar.setValue(random.randint(0,100))
        self.RPM_LCD.display(random.randint(0,100))
        self.Voltage_LCD.display(random.randint(0,100))
        self.Current_LCD.display(random.randint(0,100))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "RPM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Battery Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Motor Temp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 

app = QtGui.QApplication(sys.argv)
mySW = ControlMainWindow()
mySW.show()
sys.exit(app.exec_())
