# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_add_goods_input.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from back import database

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 320)
        self.goods_id = QtWidgets.QLabel(Dialog)
        self.goods_id.setGeometry(QtCore.QRect(10, 50, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_id.setFont(font)
        self.goods_id.setObjectName("goods_id")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 371, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_no = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_no.setObjectName("lineEdit_no")
        self.verticalLayout.addWidget(self.lineEdit_no)
        self.lineEdit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.verticalLayout.addWidget(self.lineEdit_tel)
        self.goods_price = QtWidgets.QLabel(Dialog)
        self.goods_price.setGeometry(QtCore.QRect(0, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_price.setFont(font)
        self.goods_price.setObjectName("goods_price")
        self.goods_num = QtWidgets.QLabel(Dialog)
        self.goods_num.setGeometry(QtCore.QRect(0, 170, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.goods_num.setFont(font)
        self.goods_num.setObjectName("goods_num")
        self.ADD = QtWidgets.QPushButton(Dialog)
        self.ADD.setGeometry(QtCore.QRect(90, 260, 93, 28))
        self.ADD.setObjectName("ADD")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.ADD.clicked.connect(self.addfunc)
        self.ADD.clicked.connect(Dialog.close)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.goods_id.setText(_translate("Dialog", "请输入商品ID"))
        self.goods_price.setText(_translate("Dialog", "请输入商品Price"))
        self.goods_num.setText(_translate("Dialog", "请输入商品Num"))
        self.ADD.setText(_translate("Dialog", "ADD"))
        self.pushButton.setText(_translate("Dialog", "CANCEL"))

    def addfunc(self):
        goods_ID = self.lineEdit_no.text()
        goods_Price = self.lineEdit_name.text()
        goods_Num = self.lineEdit_tel.text()
        data = (goods_ID,goods_Price,goods_Num)

        x = database()
        x.logging_data(4,data);
