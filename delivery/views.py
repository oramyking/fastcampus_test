from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from order.serializers import ShopSerializer, MenuSerializer
from order.models import Shop, Menu, Order, Orderfood
from django.utils import timezone 
from django.urls import reverse

@csrf_exempt
def deliverylist(request):
    if request.method=='GET':
        delivery_list=Order.objects.all()
        return render(request,'delivery/deliverylist.html',{'delivery_list': delivery_list})
    elif request.method=='POST':
       order_item=Order.objects.get(pk=int(request.POST['orderid'])) 
       print (order_item.deliver_finish)
       order_item.deliver_finish=1
       order_item.save()
       return render(request, 'delivery/success.html')
    