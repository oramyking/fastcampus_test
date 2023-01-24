from django.contrib import admin
from django.urls import path, include
from . import models
from user import views

app_name='user'
urlpatterns = [
    path('user/'  , views.user, name='user'), 
    path('login/' , views.login, name='login'), 
]
