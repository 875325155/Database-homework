# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from back import database

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 394)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 90, 411, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_Eno = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Eno.setObjectName("lineEdit_Eno")
        self.verticalLayout.addWidget(self.lineEdit_Eno)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 350, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 290, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 350, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(30, 100, 76, 221))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_Cno = QtWidgets.QLabel(self.splitter)
        self.label_Cno.setObjectName("label_Cno")
        self.label_Eno = QtWidgets.QLabel(self.splitter)
        self.label_Eno.setObjectName("label_Eno")
        self.label_Cno_3 = QtWidgets.QLabel(self.splitter)
        self.label_Cno_3.setObjectName("label_Cno_3")
        self.label_Cno_4 = QtWidgets.QLabel(self.splitter)
        self.label_Cno_4.setObjectName("label_Cno_4")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.addfunc)

        self.pushButton.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Yes"))
        self.comboBox.setItemText(0, _translate("Dialog", "其他（输入0）"))
        self.comboBox.setItemText(1, _translate("Dialog", "删除（输入1）"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_Cno.setText(_translate("Dialog", "员工ID"))
        self.label_Eno.setText(_translate("Dialog", "员工工资"))
        self.label_Cno_3.setText(_translate("Dialog", "所属经理ID"))
        self.label_Cno_4.setText(_translate("Dialog", "选项"))

    def addfunc(self):
        client_ID = self.lineEdit_5.text()
        client_salary = self.lineEdit_2.text()
        his_manager_s_id = self.lineEdit_Eno.text()
        choice = self.comboBox.currentIndex()

        data = (client_ID,client_salary,his_manager_s_id,choice)
        print(data)
        x = database()
        x.logging_data(2, data)
