# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_add_goods_output_change.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 394)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 80, 411, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_Eno = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Eno.setObjectName("lineEdit_Eno")
        self.verticalLayout.addWidget(self.lineEdit_Eno)
        self.label_Cno = QtWidgets.QLabel(Dialog)
        self.label_Cno.setGeometry(QtCore.QRect(80, 110, 72, 15))
        self.label_Cno.setObjectName("label_Cno")
        self.label_Eno = QtWidgets.QLabel(Dialog)
        self.label_Eno.setGeometry(QtCore.QRect(80, 160, 72, 15))
        self.label_Eno.setObjectName("label_Eno")
        self.yes = QtWidgets.QPushButton(Dialog)
        self.yes.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.yes.setObjectName("yes")
        self.label_Cno_2 = QtWidgets.QLabel(Dialog)
        self.label_Cno_2.setGeometry(QtCore.QRect(80, 210, 72, 15))
        self.label_Cno_2.setObjectName("label_Cno_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Cno.setText(_translate("Dialog", "ID"))
        self.label_Eno.setText(_translate("Dialog", "Price"))
        self.yes.setText(_translate("Dialog", "Yes"))
        self.label_Cno_2.setText(_translate("Dialog", "Num"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
