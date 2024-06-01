# CmdUi
A command user interface for Windows/一个运行在Windows上的命令行界面.
> Warm Tips/温馨提示
> 
> This project is developed voluntarily by the developer. Please do not insult the developer, otherwise it may cause the developer to permanently stop updating/本项目为开发者自愿开发，请不要谩骂开发者，否则会导致开发者永久停更
> 
##How to use/如何使用
#导入模块
import cmdui

#一个简单的选择UI
s = cmdui.simpleChooseObject("标题","选项1","选项2","选项3",default=0) #default为默认选择项目，第一个项目为0
v = s.startup() #向用户展示UI
print(v) #打印用户选择的项目,从0开始

#一个复杂的表单UI
p = cmdui.customChooseObject() #创建对象
p.add_lable("文字A") #添加文字
p.add_input("输入框标题","string",30,"默认数据") #创建一个长度为30的输入框且含有默认数据
p.add_input("密码框","password",30,"123456") #创建一个长度为30的密码框且含有默认数据​
p.add_checkbox("复选框",True) #创建一个选中的复选框
p.add_radio("单选框A","test",True) #创建一个在test组中的单选框且选中
p.add_radio("单选框B","test") #创建一个在test组中的单选框
v = p.startup() #向用户发送表单
print(v) #打印用户选择的数据
