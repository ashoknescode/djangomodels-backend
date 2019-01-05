from django.urls import path, include
from django.contrib import admin
from . import views


app_name = 'data'

urlpatterns = [
	path('', views.person_list, name='person_list'),
]