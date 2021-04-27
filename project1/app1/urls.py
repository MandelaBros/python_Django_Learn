from django.urls import path
from . import views
from modules import inputView

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('csvDownLoad/', views.csvDownLoad, name='csvDownLoad'),

]