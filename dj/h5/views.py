# _*_coding:utf-8_*_
from h5 import models
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

# Create your views here.

def index(request):
	return render(request , 'index.html')

def indexCreate(request):
	name = request.POST.get('username')
	token = request.POST.get('password')
	user = models.user.objects
	user.create(name=name, token=token, createTime='1234567890').save()
	return redirect(reverse("html5:userLists"))
def userLists(request):
	user = models.user.objects
	return render(request, 'userList.html', {'list':user.all()})