# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(683, 467)
        self.goods_id = QtWidgets.QLabel(Dialog)
        self.goods_id.setGeometry(QtCore.QRect(40, 90, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_id.setFont(font)
        self.goods_id.setObjectName("goods_id")
        self.goods_price = QtWidgets.QLabel(Dialog)
        self.goods_price.setGeometry(QtCore.QRect(40, 160, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_price.setFont(font)
        self.goods_price.setObjectName("goods_price")
        self.goods_num = QtWidgets.QLabel(Dialog)
        self.goods_num.setGeometry(QtCore.QRect(40, 240, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_num.setFont(font)
        self.goods_num.setObjectName("goods_num")
        self.ADD = QtWidgets.QPushButton(Dialog)
        self.ADD.setGeometry(QtCore.QRect(140, 360, 93, 28))
        self.ADD.setObjectName("ADD")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_no = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_no.setGeometry(QtCore.QRect(180, 90, 369, 24))
        self.lineEdit_no.setObjectName("lineEdit_no")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(180, 230, 81, 31))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 160, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.goods_id.setText(_translate("Dialog", "经理ID"))
        self.goods_price.setText(_translate("Dialog", "选项"))
        self.goods_num.setText(_translate("Dialog", "经理Rank"))
        self.ADD.setText(_translate("Dialog", "OK"))
        self.pushButton.setText(_translate("Dialog", "CANCEL"))
        self.comboBox.setItemText(0, _translate("Dialog", "0"))
        self.comboBox.setItemText(1, _translate("Dialog", "1"))
