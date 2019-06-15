# _*_coding:utf-8_*_
import datetime
from h5 import models
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
# 登陆，存在登陆，不存在退出到登陆页面
def index(request):
	name = request.COOKIES['username']
	return render(request , 'index.html', locals())

def indexCreate(request):
	name = request.POST.get('username')
	token = request.POST.get('password')
	user = models.user.objects
	user.create(name=name, token=token, createTime='1234567890').save()
	return redirect(reverse("html5:userLists"))
def userLists(request):
	user = models.user.objects
	return render(request, 'userList.html', {'list':user.all()})
def userUp(request):
	id = request.GET.get('id')
	user = models.user.objects
	user = models.user.objects
	user.filter(id=id).delete()
	return render(request, 'userList.html', {'list':user.all()})
def userDel(request):
	id = request.GET.get('id')
	user = models.user.objects
	user.filter(id=id).delete()
	return render(request, 'userList.html', {'list':user.all()})