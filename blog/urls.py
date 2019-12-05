from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('create/', views.blog_create, name='blog-create')
]
