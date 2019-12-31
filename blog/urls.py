from django.urls import path

from . import views
from users import views as users_view

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('contact/', views.contact, name='blog-contact'),
    path('register/', users_view.register, name='blog-register'),
]
