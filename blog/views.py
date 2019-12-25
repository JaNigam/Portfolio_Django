from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
	 'author': 'Ritvik Rathore',
	 'title': 'Blog Post 1',
	 'content': 'First post content',
	 'date_posted': 'Augut 27, 2018'
	},
	{
	 'author': 'Ritvik Dayal',
	 'title': 'Blog Post 2',
	 'content': 'second post content',
	 'date_posted': 'Augut 28, 2018'
	}
]

def home(request):
	return render(request, 'blog/index.html')

def blog_about(requests):
	return render(requests, 'blog/blog_about.html')

def blog(request):
	context = {
	'posts': posts
	}
	return render(request, 'blog/blog.html', context)

def contact(request):
	return render(request, 'blog/contact.html')

def work(requests):
	return render(request, 'blog/work.html')
