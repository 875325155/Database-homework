mainwindow->主界面  view1  ui
##商品入库
window_add_goods_input->商品入库的输入操作  view2_goods_input  a


##检查库存
check_left_info  ->直接利用Select语句查看结果   view_check_left  c4


##经理管理
window_manager ->对经理进行管理   view_manager   d

##员工管理
window_user ->对员工进行管理    view_user   e

##信息展示
//对6个表进行select操作得到表的内容
show_all_info     view_show  f
{
	window_show_cus_food;   view_show_cus_food  f1
	window_show_customer;    view_show_cus_customer  f2
	window_show_employee;    view_show_employee   f3
	window_show_man_emp;    view_show_man_emp   f4
	window_show_manager;    view_show_manager   f5
	window_show_myshop;--->这个已经由检查库存中check_left_info实现，这里不用考虑   view_check_left  c4
}



##收银
window_cash ->进行收银操作    view_cash   g
 




