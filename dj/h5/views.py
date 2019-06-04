from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {}
	context['index'] = "Hello, world. You're at the polls index."
    # return HttpResponse(context['index'])
	return render(request , 'index.html' , context)
