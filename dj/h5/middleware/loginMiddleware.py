from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, reverse
class LoginMiddleware(MiddlewareMixin):
	def process_request(self,request):
		print(request.path)
	def process_response(self,request,response):
		url = request.path
		bypass = {
			'/h5/login':'/h5/login',
			'/h5/loginPy':'/h5/loginPy',
		}
		if url in bypass:
			return response
		else:
			if 'username' in request.COOKIES:
				return response
			else:
				return redirect(reverse("html5:login"))

