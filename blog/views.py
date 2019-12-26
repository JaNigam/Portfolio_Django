from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'blog/index.html')

def blog(request):
	return render(request, 'blog/blog.html')

def contact(request):
	return render(request, 'blog/contact.html')
