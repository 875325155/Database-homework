# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_cash.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(645, 317)
        self.label_Cno = QtWidgets.QLabel(Dialog)
        self.label_Cno.setGeometry(QtCore.QRect(70, 65, 76, 39))
        self.label_Cno.setObjectName("label_Cno")
        self.label_Cno_2 = QtWidgets.QLabel(Dialog)
        self.label_Cno_2.setGeometry(QtCore.QRect(70, 156, 76, 39))
        self.label_Cno_2.setObjectName("label_Cno_2")
        self.label_Eno = QtWidgets.QLabel(Dialog)
        self.label_Eno.setGeometry(QtCore.QRect(70, 110, 76, 40))
        self.label_Eno.setObjectName("label_Eno")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 70, 409, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 120, 409, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(160, 170, 71, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Cno.setText(_translate("Dialog", "顾客ID"))
        self.label_Cno_2.setText(_translate("Dialog", "数目"))
        self.label_Eno.setText(_translate("Dialog", "商品ID"))
        self.pushButton.setText(_translate("Dialog", "Yes"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
