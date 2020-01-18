# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 90, 351, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(929, 48, 64, 64))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/images/cartoon4.ico"))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 64, 64))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/images/cartoon3.ico"))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 450, 64, 64))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/images/cartoon2.ico"))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 10, 64, 64))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/pic/images/cartoon4.ico"))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 440, 64, 64))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/images/cartoon1.ico"))
        self.label_2.setObjectName("label_2")
        self.pushButton_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show.setGeometry(QtCore.QRect(190, 430, 151, 51))
        self.pushButton_show.setObjectName("pushButton_show")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 430, 151, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 130, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 250, 161, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "欢迎您，尊敬的经理"))
        self.pushButton_show.setText(_translate("MainWindow", "信息展示"))
        self.pushButton_5.setText(_translate("MainWindow", "退出系统"))
        self.pushButton.setText(_translate("MainWindow", "人事管理"))
        self.pushButton_2.setText(_translate("MainWindow", "经理调整"))
        self.menu.setTitle(_translate("MainWindow", "经理主界面"))
import apprcc_rc
