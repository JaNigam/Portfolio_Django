from django.urls import path

from . import views

urlpatterns = [
    path('register\', views.register, name='blog-register'),
    path('test\', views.register, name='blog-test'),
]
