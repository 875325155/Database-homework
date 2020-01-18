#后端
import sys
import pymysql
from functools import partial
from PyQt5.Qt import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame, QApplication, QDialog, QDialogButtonBox,
                             QMessageBox, QVBoxLayout, QLineEdit, QTableWidgetItem, QTableWidget, QHBoxLayout)


class database:

    def __init__(self, parent=None):
        # 连接数据库
        global db
        global cur
        #连接数据库，并输入相关信息（好像密码和你的不一样）
        db = pymysql.connect("localhost", "root", "wanjin", "wanjin")
        # 获取游标、数据
        cur = db.cursor()

    def logging_data(self, flag, comm):
        #收银
        if flag == 1:
            #data = (client_ID,goods_ID,num)

            print(comm)
            cur.execute("SELECT price, mynumber FROM  myshop WHERE id = %s",comm[1])
            result = cur.fetchall()
            m = 0
            if(result[0][0] * float(comm[2]) > 5000):
                m = 1
            insert_data0 = (comm[0], result[0][0] * float(comm[2]), m)
            print("2")
            print(insert_data0)
            cur.execute("INSERT INTO customer VALUES(%s,%s,%s)", insert_data0)
            print("3")
            tmp_data = (result[0][1] - int(comm[2]), comm[1])
            cur.execute("UPDATE  myshop SET mynumber = %s WHERE id = %s", tmp_data)
            print("4")
            insert_data1 = (comm[0], comm[1], comm[2])
            cur.execute("INSERT INTO cus_food VALUES(%s, %s, %s)", insert_data1)
            print("5")


            db.commit()

        #员工管理
        elif flag == 2:
            # data = (client_ID,client_salary,his_manager_s_id,choice)

            if comm[3] == 1:  # 已核验
                print("flag1")
                cur.execute("DELETE FROM employee WHERE id = %s", comm[0])
                cur.execute("DELETE FROM man_emp WHERE employee_id = %s", comm[0])
                db.commit()
            else:
                print("flag2")
                cur.execute("SELECT  * FROM  employee where id = %s", comm[0])
                result = cur.fetchall()
                if len(result) != 0:
                    print("flag3")
                    tmp_data0 = (comm[1], comm[0])
                    tmp_data1 = (comm[2], comm[0])
                    print(tmp_data0)
                    cur.execute("UPDATE employee SET salary = %s WHERE id = %s", tmp_data0)

                    cur.execute("UPDATE man_emp SET manager_id = %s where employee_id = %s", tmp_data1)
                if len(result) == 0:
                    insert_data0 = (comm[0], comm[1])
                    insert_data1 = (comm[2], comm[0])
                    cur.execute("INSERT INTO employee VALUES(%s, %s)", insert_data0)
                    cur.execute("INSERT INTO man_emp VALUES(%s, %s)", insert_data1)
            db.commit()
        #经理管理
        elif flag == 3:
            # data = (manager_ID, choice, manager_rank)

            print(comm)
            if comm[1] == 1:
                cur.execute("DELETE FROM manager WHERE id = %s", comm[0])
            if comm[1] == 0:
                cur.execute("select id from  manager where id = %s", comm[0])
                db.commit()
                result = cur.fetchall()
                if len(result) != 0:
                    tmp_data0 = (comm[2], comm[0])
                    # cur.execute("UPDATE manager SET rank = %s WHERE id = %s ", tmp_data0)
                    cur.execute("UPDATE `wanjin`.`manager` SET `rank` = %s WHERE `id` = %s ", tmp_data0)
                else :
                    insert_data0 = (comm[0], comm[2])
                    cur.execute("INSERT INTO manager VALUES(%s, %s)", insert_data0)
            db.commit()
        #商品入库
        elif flag == 4:
            #data = (goods_ID,goods_Price,goods_Num)
            print("flag == 4")
            print(comm)
            cur.execute("SELECT  mynumber FROM  myshop where id = %s", comm[0])
            result = cur.fetchall()
            if len(result) != 0:
                tmp_data0 = (result[0][0] + int(comm[2]), comm[0])
                cur.execute("UPDATE `wanjin`.`myshop` SET `mynumber` = %s WHERE `id` = %s", tmp_data0)
                cur.execute("INSERT INTO myshop VALUES (%s,%s,%s)", comm)
            db.commit()


    #下面为表的显示函数，记得表的名字得改...
    #show cus_food
    def show_cus_food(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.cus_food")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)
    #show customer
    def show_customer(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.customer")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)

    #show employee
    def show_employee(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.employee")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)
    # show man_emp
    def show_man_emp(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.man_emp")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)
    #show manager
    def show_manager(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.manager")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)
    #view_check_left
    def check_left_info(self, tableWidget):
        cur.execute("SELECT * FROM wanjin.myshop")
        data = cur.fetchall()
        db.commit()
        self.Tableshow(data, tableWidget)


    #显示数据
    def Tableshow(self, data, tableWidget):
        tableWidget.clear()
        col_lst = [tup[0] for tup in cur.description]
        tableWidget.setHorizontalHeaderLabels(col_lst)
        for i in range(len(data)):
            for j in range(len(data[0])):
                temp_data = data[i][j]  # 临时记录，不能直接插入表格
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                tableWidget.setItem(i, j, data1)



