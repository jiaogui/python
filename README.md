# 学习python笔记

# 创建项目：
django-admin  startproject  项目名称

# 创建应用：
diango-admin  startapp  应用名称

# 运行项目：
python  manage.py  runserver

# web端页面展示：
#  1、在应用目录下找到views.py文件，写入试图路由
#     1》、引入包文件：from django.http import HttpResponse
#     2》、定义视图文件：
                  def  方法名 (requerst):
                      return HttpResponse('内容')
#  2、在应用目录下注册路由文件urls.py，写入引入的试图、路由
#     1》、引入包文件：from django.urls import path, include
#     2》、引入views.py视图文件：import h5.views
#     3》、将视图文件写入路由数组里：
                     urlpatterns = [
						    path('index', h5.views.index),
						]
#  3、项目路由引入应用的路由和路由包、写入到路由：
#     1》、引入包文件：from django.urls import path, include
#     2》、将应用路由文件写入路由数组里：
                     urlpatterns = [
						    path('index', include('应用名.urls')),
						]
#  4、添加应用settings.py里找到INSTALLED_APPS数组：'应用名 .apps.首字母大写的应用名Config',