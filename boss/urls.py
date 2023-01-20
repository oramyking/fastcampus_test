from django.contrib import admin
from django.urls import path, include
from . import models
from boss import views

app_name='boss'
urlpatterns = [
    path('orders/<int:shop_id>' , views.orderlist, name='orderlist'),
    path('timeinput'            , views.time_input, name='timeinput')
]

