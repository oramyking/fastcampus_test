from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from order.serializers import ShopSerializer, MenuSerializer
from order.models import Shop, Menu, Order, Orderfood
from django.utils import timezone 
from django.urls import reverse

@csrf_exempt
def orderlist(request, shop_id):
    if request.method=='GET':
        order_list=Order.objects.filter(shop=shop_id)
        return render(request,'boss/orderlist.html',{'order_list': order_list})
    else:
        return HttpResponse(status=404)
    
@csrf_exempt
def time_input (request):
    if request.method=='POST':
       order_item=Order.objects.get(pk=int(request.POST['orderid']))
       shop=order_item.shop_id
       order_item.estimate_time= int (request.POST['estimate_time'])
       order_item.save()
       return render(request, 'boss/success.html', {'shop_id':shop})
    else:
       return HttpResponse(status=404)