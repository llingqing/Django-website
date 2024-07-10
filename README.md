Django 项目部署(进入文件夹 cd login)

1.安装所需软件

    python 3.6或更高版本

    pip

    Vscode所需扩展：Django,python



2.创建并激活虚拟环境

vscode中按CTRL+shift+p选择python选择解释器



创建虚拟环境-->创建.venv虚拟环境



显示出上图效果或命令行中有venv字样即为激活成功

3.安装Django

    打开命令行，输入以下命令安装Django

    pip install Django

（此命令需要在src文件夹下执行）



4.运行Django项目

    打开命令行，输入以下命令运行Django项目

    python manage.py runserver --insecure



5.浏览器访问

首页

登录界面

注册界面

站点管理 | Django 站点管理员

管理员账号：admin 

管理员密码：p@sswod1234

 数据库可以在管理系统查看，也可以在vscode查看
