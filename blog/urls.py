from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('contact/', views.contact, name='blog-contact'),
    path('work/', views.work, name='blog-work'),
    path('about/', views.blog_about, name='blog-about')
]
