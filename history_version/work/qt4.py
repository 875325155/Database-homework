# coding:utf-8

from PyQt5 import QtGui,QtCore,QtWidgets,QtSql
import sys
from PyQt5.QtWidgets import (QFrame,QApplication,QDialog, QDialogButtonBox,
        QMessageBox,QVBoxLayout, QLineEdit,QTableWidgetItem,QTableWidget,QHBoxLayout)
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit, QInputDialog)
import pymysql


class MainUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()


    # 初始化UI界面
    def initUi(self):
        # 设置窗口标题
        self.setWindowTitle("商店管理系统")
        # 设置窗口大小
        self.resize(400,400)

        # 创建一个窗口部件
        self.widget = QtWidgets.QWidget()
        # 创建一个网格布局
        self.grid_layout = QtWidgets.QGridLayout()
        # 设置窗口部件的布局为网格布局
        self.widget.setLayout(self.grid_layout)

        # 创建一个按钮组
        self.group_box = QtWidgets.QGroupBox('功能按钮')
        self.group_box_layout = QtWidgets.QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        # 将上述两个部件添加到网格布局中
        self.grid_layout.addWidget(self.group_box,0,0)

        # 创建多行文本框
        self.textEdit = QTextEdit()

        # 创建按钮组的按钮
        self.b_buy = QtWidgets.QPushButton("收银")
        self.b_buy.clicked.connect(self.buy)
        self.b_people0 = QtWidgets.QPushButton("员工管理")
        self.b_people0.clicked.connect(self.people0)
        self.b_people1 = QtWidgets.QPushButton("经理管理")
        self.b_people1.clicked.connect(self.people1)
        self.b_insert = QtWidgets.QPushButton("商品入库")
        self.b_insert.clicked.connect(self.my_insert)
        self.b_check = QtWidgets.QPushButton("检查库存")
        self.b_check.clicked.connect(self.check)
        self.b_close = QtWidgets.QPushButton("退出")
        self.b_close.clicked.connect(self.close)
        # 添加按钮到按钮组中
        self.group_box_layout.addWidget(self.b_buy)
        self.group_box_layout.addWidget(self.b_people0)
        self.group_box_layout.addWidget(self.b_people1)
        self.group_box_layout.addWidget(self.b_insert)
        self.group_box_layout.addWidget(self.b_check)
        self.group_box_layout.addWidget(self.b_close)

        # 设置UI界面的核心部件
        self.setCentralWidget(self.widget)

    # 浏览数据
    def buy(self):

        mul_text, ok = QInputDialog.getMultiLineText(self, "收银", "收银", "按行输入顾客id，商品id，数目")
        if (ok):
            print(mul_text)  # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。
            mydata = mul_text.splitlines()
            print("-"*50)
            # 获取游标
            db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='wanjin')
            db.select_db('wanjin')
            # 获取游标
            cur = db.cursor()
            tmp_data = [mydata[2], mydata[1]]
            print("flag1")
            try:
                # 执行sql语句
                #得到所选商品id的商品的所有信息，如价格，总数等
                cur.execute("SELECT * FROM  `wanjin`.`myshop` WHERE `id` = '%s'"% mydata[1])
                result = cur.fetchall()
                # print(result)
                result0 = result[0][3]
                # print(result0)
                result1 = float(float(result[0][2]) * int(result0))
                #商品新的数量
                # print(int(mydata[2]))
                tmp_data[0] = str(result0-int(mydata[2]))
                # print(tmp_data[0])
                insert_data0 = (mydata[0], result1, '0')
                insert_data1 = (mydata[0], mydata[1], mydata[2])
                tmp_data=tuple(tmp_data)
                #python格式化输出需要使用tumple!!!
                tmp_data0_up = "UPDATE  `wanjin`.`myshop` SET `number` = %s WHERE `id` = '%s'"%tmp_data
                cur.execute(tmp_data0_up)

                #customer表为消费记录表
                data0="INSERT INTO `wanjin`.`customer`(`id`, `expenditure`, `member`) VALUES ('%s', %s, %s)"%insert_data0
                cur.execute(data0)
                data1 = '''
                INSERT
                INTO
                `wanjin`.
                `cus_food`(`customer_id`, `food_id`, `number`)
                VALUES('%s', '%s', %s)
                '''

                cur.execute(data1%insert_data1)
                #执行sql语句
                db.commit()

            except:
                # 发生错误时回滚
                print("ERROR!")
                db.rollback()
            cur.execute("SELECT*FROM cus_food")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            # 关闭数据库连接
            cur.close()
            db.close()

    # 员工管理界面
    def people0(self):
        mul_text, ok = QInputDialog.getMultiLineText(self, "员工管理", "员工管理", "按行输入员工id，员工工资，所属经理id，开除（1）|其他（0)")
        if (ok):
            print(mul_text)  # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。
            mydata = mul_text.splitlines()
            # 获取游标
            db = pymysql.connect(host='127.0.0.1', user='root', password='wanjin', port=3306, db='wanjin')
            db.select_db('wanjin')
            # 获取游标
            cur = db.cursor()
            print("flag1")
            try:
                # 执行sql语句
                if mydata[3] == '1':#已核验
                    cur.execute('''DELETE FROM `wanjin`.`employee` WHERE id = (%s);''', mydata[0])
                    db.commit()
                else:
                    cur.execute('''SELECT  * FROM  `wanjin`.`employee` where id = (%s);''', mydata[0])
                    print("flag2")
                    result = cur.fetchall()
                    if len(result) != 0:
                        print("flag3")
                        tmp_data0 = (mydata[1], mydata[0])
                        tmp_data1 = (mydata[2], mydata[0])
                        # cur.execute("UPDATE  `wanjin`.`employee` SET `salary` = %s WHERE `id `= '%s'"%tmp_data0)
                        tmp_data0_up= "UPDATE  `wanjin`.`employee` SET `salary` = %s WHERE `id`= '%s'"%tmp_data0
                        cur.execute(tmp_data0_up)

                        tmp_data1_up= "UPDATE  `wanjin`.`man_emp` SET `manager_id` = '%s' where employee_id = '%s'"% tmp_data1
                        cur.execute(tmp_data1_up)




                        # cur.execute("UPDATE  `wanjin`.`man_emp` SET manager_id = '%s' where id = '%s';"% tmp_data1)
                        # cur.execute(s)
                        db.commit()
                    if len(result) == 0:
                        print("flag4")
                        insert_data0 = (mydata[0], mydata[1])
                        insert_data1 = (mydata[2], mydata[0])
                        data0 = '''
                                        INSERT
                                        INTO
                                        `wanjin`.
                                        `employee`(`id`, `salary`)
                                        VALUES(%s, %s)
                                        '''
                        cur.execute(data0 % insert_data0)
                        data1 = '''
                                        INSERT
                                        INTO
                                        `wanjin`.
                                        `man_emp`(`manager_id`, `employee_id`)
                                        VALUES(%s, %s)
                                        '''
                        print("flag5")
                        cur.execute(data1 % insert_data1)
                        # 执行sql语句
                        db.commit()

            except:
                # 发生错误时回滚
                db.rollback()
            cur.execute("SELECT*FROM employee")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            # 关闭数据库连接
            cur.close()
            db.close()
    def people1(self):
        mul_text, ok = QInputDialog.getMultiLineText(self, "经理管理", "经理管理", "按行输入经理id，开除（1）|其他（0)，经理rank")
        if (ok):
            print(mul_text)  # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。
            mydata = mul_text.splitlines()

            # 获取游标
            db = pymysql.connect(host='127.0.0.1', user='root', password='wanjin', port=3306, db='wanjin')
            db.select_db('wanjin')
            # 获取游标
            cur = db.cursor()
            print("flag1")
            try:
                # 执行sql语句
                if mydata[2] == '1':
                    cur.execute('''DELETE FROM `wanjin`.`manager` WHERE id = (%s);''', mydata[0])
                    db.commit()
                else:
                    cur.execute('''select * from  `wanjin`.`manager` where id = (%s);''', mydata[0])
                    print("flag2")
                    result = cur.fetchall()
                    if len(result) != 0:
                        print("flag3")
                        tmp_data0 = (mydata[2], mydata[0])
                        # cur.execute("UPDATE  `wanjin`.`employee` SET `salary` = %s WHERE `id `= '%s'"%tmp_data0)
                        tmp_data0_up = "UPDATE  `wanjin`.`manager` SET `rank` = '%s' WHERE `id`= '%s'" % tmp_data0
                        cur.execute(tmp_data0_up)

                        # cur.execute("UPDATE  `wanjin`.`man_emp` SET manager_id = '%s' where id = '%s';"% tmp_data1)
                        # cur.execute(s)
                        db.commit()
                    if len(result) == 0:
                        insert_data0 = (mydata[0], mydata[2])
                        data1 = "INSERT INTO `wanjin`.`manager`(`id`, `rank`)VALUES(%s, %s)"
                        print("flag4")
                        cur.execute(data1 % insert_data0)

                        print("flag5")
                        # 执行sql语句
                        db.commit()

            except:
                # 发生错误时回滚
                db.rollback()
            cur.execute("SELECT*FROM manager")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            # 关闭数据库连接
            cur.close()
            db.close()
    def my_insert(self):
        mul_text, ok = QInputDialog.getMultiLineText(self, "添加商品", "输入商品信息", "请按行输入id,price,number")
        if (ok):
            print(mul_text)  # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。
            data = mul_text.splitlines()

            # 获取游标
            db = pymysql.connect(host='127.0.0.1', user='root', password='wanjin', port=3306, db='wanjin')
            db.select_db('wanjin')
            # 获取游标
            cur = db.cursor()
            sql = "INSERT INTO wanjin.myshop(\
                  id, price, number) \
                  VALUES ('%s',  %s,  '%s')" % \
                  (data[0], data[1], data[2])
            try:
                # 执行sql语句
                cur.execute(sql)
                # 执行sql语句
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()
            cur.execute("SELECT*FROM myshop")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            # 关闭数据库连接
            db.close()
    def check(self):
        db = pymysql.connect(host='127.0.0.1', user='root', password='wanjin', port=3306, db='wanjin')
        db.select_db('wanjin')
        # 获取游标
        cur = db.cursor()
        cur.execute("SELECT*FROM myfood")
        rows = cur.fetchall()
        self.textEdit.setPlainText("...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MainUi()
    c.show()
    sys.exit(app.exec_())
