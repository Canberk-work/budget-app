from django.conf.urls import url
from django.urls import path
from testing_app import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.help, name='help')
]