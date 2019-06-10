# 学习python笔记

# 缩进使用：tab键


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


# web端显示html界面
#  1、修改应用下views.py文件
#     1》、在上面的案例基础上，应用层下引入render： from django.shortcuts import render
#     2》、在方法里面定义context  = {}：context['html文件名'] = 对应的数据
#     3》、返回到界面：return render(request , 'index.html' , context)
#     4》、案例：
		from django.shortcuts import render
		from django.http import HttpResponse
		def index(request):
			context = {}
			context['index'] = "Hello, world. You're at the polls index."
			return render(request , 'index.html' , context)
#  2、修改配置文件：seetings.py文件下的   TEMPLATES里的DIRS[]
#     1》、创建对应的文件目录，其中：B'ASE_DIR'代表根目录、'+'代表拼接
#     2》、具体案例：
		TEMPLATES = [
		    {
		        'BACKEND': 'django.template.backends.django.DjangoTemplates',
		        # html界面*****************开始
		        'DIRS': [
		            BASE_DIR+"/templates",
		        ],
		        # html界面*****************结束
		        'APP_DIRS': True,
		        'OPTIONS': {
		            'context_processors': [
		                'django.template.context_processors.debug',
		                'django.template.context_processors.request',
		                'django.contrib.auth.context_processors.auth',
		                'django.contrib.messages.context_processors.messages',
		            ],
		        },
		    },
		]
#  3、html页面输出
#     1》、双{} 来接值：{{  context下的数组的键名 }}
#     2》、<h1>{{ index }}</h1>


# 连接数据库：找到seeting.py文件，头部加上注释：    #  -*- coding: UTF-8 -*-   找到DATABASES数组
#  1、代码案例：
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.mysql',
		        'NAME': 'test',
		        'USER': 'root',
		        'PASSWORD': '123456',
		        'HOST':'localhost',
		        'PORT':'3306',
		        # 默认配置
		        # 'ENGINE': 'django.db.backends.sqlite3',
		        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		    }
		}
# 2、找到项目下的__init__.py文件，添加2行代码，案例如下：
	import pymysql
	pymysql.install_as_MySQLdb()
# 3、找到python目录下E:\Python\Lib\site-packages\django\db\backends\mysql的base.py文件，注释
	 if version < (1, 3, 13):
	   raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
# 4、找到python目录下E:\Python\Lib\site-packages\django\db\backends\mysql的operation.py文件，修改
    query = query.decode(errors='replace')修改成query = query.encode(errors='replace')


# sqlite3或者mysql数据库创建用户
#  1、生成迁移表：python manage.py migrate
#  2、创建用户：python  manage.py  createsuperuser  根据提示输出结果


# 接值格式：request.POST.get('username')  /  request.POST['username']

###########
