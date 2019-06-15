# _*_coding:utf-8_*_
import hashlib
from h5 import models
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
# 登陆界面
def login(request):
	return render(request, 'login.html')
# 登陆后台
def loginPy(request):
	name = request.POST.get('username')
	token = request.POST.get('password')
	user = models.user.objects
	data = user.filter(name=name , token=token)
	if data:
		# reverse跳转的重定向路径
		response = HttpResponseRedirect(reverse("html5:index"))
		md5 = hashlib.md5()
		md5.update((token+name).encode())
		response.set_cookie('token',md5.hexdigest())
		response.set_cookie('username',name)
		# 后台首页
		return response
	else :
		# 提示账号不存在，返回登陆页面
		return render(request , 'login.html',{'message':'账号不存在，或者账号不存在'})
# 退出登陆
def sign_out(request):
	response = HttpResponseRedirect(reverse("html5:login"))
	response.delete_cookie('username')
	return response
