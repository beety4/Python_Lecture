from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dict', views.dict, name='dict'),
    path('name', views.name, name='name'),
    path('news', views.news, name='news'),
]