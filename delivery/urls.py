from django.contrib import admin
from django.urls import path, include
from . import models
from delivery import views

app_name='delivery'
urlpatterns = [
    path('' , views.deliverylist, name='deliverylist'),
    # path('timeinput'            , views.time_input, name='delivery')
]

