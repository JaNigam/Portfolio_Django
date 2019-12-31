from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
	return render(request, 'blog/index.html')

def blog(request):
	context = {
	'title': 'Blog',
	'posts': Post.objects.all()
	}
	return render(request, 'blog/blog.html', context)

def contact(request):
	return render(request, 'blog/contact.html', {'title': 'Contact'})
