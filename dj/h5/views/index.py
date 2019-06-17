# _*_coding:utf-8_*_
import datetime
from h5 import models
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
# 登陆，存在登陆，不存在退出到登陆页面
def index(request):
	nav = models.Nav.objects
	# 菜单栏目
	navs = nav.values('id','name','img','href').filter(start=1,pid=0)
	for navList in navs:
		navList['chilende'] = nav.values('id','name','img','href').filter(pid=navList['id'])
	# 登陆用户
	name = request.COOKIES['username']
	# 返回后台页面
	return render(request , 'index.html', locals())
