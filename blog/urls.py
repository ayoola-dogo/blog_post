from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
]
