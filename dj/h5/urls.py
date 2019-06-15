from django.urls import path, include
from h5.views import login, index

import h5.views

app_name = 'html5'

urlpatterns = [
	# 登陆
    path('login', login.login, name='login'),
    path('loginPy', login.loginPy),
    path('sign_out', login.sign_out),
    # 系统首页
    path('index', index.index, name='index'),
    path('userLists', index.userLists, name='userLists'),
    path('indexCreate', index.indexCreate),
    path('userUp', index.userUp,),
    path('userDel', index.userDel),
]