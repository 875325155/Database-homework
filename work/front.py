#这是前端
import sys


from PyQt5.QtWidgets import QApplication, QMainWindow

import check_left_info
import mainwindow
import show_all_info
import window_add_goods_input
import window_cash
import window_manager
import window_show_cus_food
import window_show_customer
import window_user
import window_show_manager
import window_show_man_emp
import window_show_employee


if __name__ == '__main__':
    #这是主界面
    ss = QApplication(sys.argv)

    view1 = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(view1)
    view1.show()

    #登陆界面
    

    #商品入库输入界面
    view2_goods_input = QMainWindow()
    a = window_add_goods_input.Ui_Dialog()
    a.setupUi(view2_goods_input)


    #检查库存
    view_check_left = QMainWindow()
    c4 = check_left_info.Ui_Dialog()
    c4.setupUi(view_check_left)

    #经理管理
    view_manager = QMainWindow()
    d = window_manager.Ui_Dialog()
    d.setupUi(view_manager)

    #员工管理
    view_user = QMainWindow()
    e = window_user.Ui_Dialog()
    e.setupUi(view_user)

    #信息展示
    view_show = QMainWindow()
    f = show_all_info.Ui_Dialog()
    f.setupUi(view_show)

    #展示cus_food
    view_show_cus_food = QMainWindow()
    f1 = window_show_cus_food.Ui_Dialog()
    f1.setupUi(view_show_cus_food)

    # 展示customer
    view_show_cus_customer = QMainWindow()
    f2 = window_show_customer.Ui_Dialog()
    f2.setupUi(view_show_cus_customer)

    #展示employee
    view_show_employee = QMainWindow()
    f3 = window_show_employee.Ui_Dialog()
    f3.setupUi(view_show_employee)

    #展示man_emp
    view_show_man_emp = QMainWindow()
    f4 = window_show_man_emp.Ui_Dialog()
    f4.setupUi(view_show_man_emp)

    # 展示manager
    view_show_manager = QMainWindow()
    f5 = window_show_manager.Ui_Dialog()
    f5.setupUi(view_show_manager)

    # 收银
    view_cash = QMainWindow()
    g = window_cash.Ui_Dialog()
    g.setupUi(view_cash)


    #点击按钮之后触发的事件
    #主窗口的跳转
    ui.pushButton_cash.clicked.connect(view_cash.show)
    ui.pushButton_checkleft.clicked.connect(view_check_left.show)
    ui.pushButton_show.clicked.connect(view_show.show)
    ui.pushButton_letin.clicked.connect(view2_goods_input.show)
    ui.pushButton_manager.clicked.connect(view_manager.show)
    ui.pushButton_staff.clicked.connect(view_user.show)

    #信息展示窗口的跳转
    f.pushButton.clicked.connect(view_show_cus_food.show)
    f.pushButton_2.clicked.connect(view_show_cus_customer.show)
    f.pushButton_3.clicked.connect(view_show_employee.show)
    f.pushButton_4.clicked.connect(view_check_left.show)
    f.pushButton_5.clicked.connect(view_show_manager.show)
    f.pushButton_6.clicked.connect(view_show_man_emp.show)



    sys.exit(ss.exec_())