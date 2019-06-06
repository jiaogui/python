# _*_coding:utf-8_*_
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request , 'index.html')

def indexCreate(request):
	return HttpResponse(request.POST.get('username'))
