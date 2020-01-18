# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_staff.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 420, 64, 64))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/images/cartoon1.ico"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(11, 11, 64, 64))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/images/cartoon3.ico"))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(11, 419, 64, 64))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/images/cartoon2.ico"))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 420, 131, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(11, 82, 351, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(740, 10, 64, 64))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/images/cartoon4.ico"))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show.setGeometry(QtCore.QRect(210, 420, 151, 51))
        self.pushButton_show.setObjectName("pushButton_show")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(410, 90, 281, 291))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton_cash = QtWidgets.QPushButton(self.splitter)
        self.pushButton_cash.setObjectName("pushButton_cash")
        self.pushButton_checkleft = QtWidgets.QPushButton(self.splitter)
        self.pushButton_checkleft.setObjectName("pushButton_checkleft")
        self.pushButton_letin = QtWidgets.QPushButton(self.splitter)
        self.pushButton_letin.setObjectName("pushButton_letin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "退出系统"))
        self.label.setText(_translate("MainWindow", "欢迎您，可爱的员工"))
        self.pushButton_show.setText(_translate("MainWindow", "信息展示"))
        self.pushButton_cash.setText(_translate("MainWindow", "收银"))
        self.pushButton_checkleft.setText(_translate("MainWindow", "检查库存"))
        self.pushButton_letin.setText(_translate("MainWindow", "商品入库"))
        self.menu.setTitle(_translate("MainWindow", "员工主界面"))
import apprcc_rc
