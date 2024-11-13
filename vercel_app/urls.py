from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name = 'write'),
    path('get_last_name/', views.get_last_name, name = 'get_last_name')
]
