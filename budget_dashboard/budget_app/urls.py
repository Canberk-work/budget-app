from django.conf.urls import url
from django.urls import path
from budget_app import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.help, name='help')
]
