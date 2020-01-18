# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_add_goods_output.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(768, 486)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 701, 331))
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.fresh = QtWidgets.QPushButton(Dialog)
        self.fresh.setGeometry(QtCore.QRect(600, 430, 93, 28))
        self.fresh.setObjectName("fresh")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 409, 411, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.delete_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout.addWidget(self.delete_2)
        self.change = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.change.setObjectName("change")
        self.horizontalLayout.addWidget(self.change)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.fresh.setText(_translate("Dialog", "fresh"))
        self.add.setText(_translate("Dialog", "ADD"))
        self.delete_2.setText(_translate("Dialog", "DELETE"))
        self.change.setText(_translate("Dialog", "CHANGE"))
