from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('csvDownLoad/', views.csvDownLoad, name='csvDownLoad'),
    path('showCreateAozoraForm/', views.showCreateAozoraForm, name='showCreateAozoraForm'),
    path('addAozora', views.addAozora, name='addAozora'),
]