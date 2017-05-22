from django.shortcuts import render
from .models import GoodsList
from .models import ItemList
from .models import PreferentialGoods
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
import math
import time
# Create your views here.
def homepage(request):
    return render(request, 'pos/homepage.html', {'sum_count': ItemList.sum_count()})
def shopping_list(request):
    goodlists = GoodsList.objects.all()
    if request.method=='POST':
        goods=GoodsList.objects.filter(id=request.POST['id'])
        buy_goods=ItemList.objects.filter(goods_id=request.POST['id'])
        if buy_goods:
            buy_goods[0].count+=1
            buy_goods[0].save()
        else:
             new_item={
                 'count':1,
                 'goods_id':goods[0].id,
                 'type':goods[0].type,
                 'name':goods[0].name,
                 'price':goods[0].price,
                 'unit':goods[0].unit
             }
             ItemList.objects.create(**new_item)
        item=ItemList.objects.filter(goods_id=request.POST['id'])
        free_goods = PreferentialGoods.objects.filter(goods_id=item[0].goods_id)
        if item:
            if free_goods:
                item[0].free_count = math.floor(item[0].count/3)
                item[0].free_money=item[0].free_count*float(item[0].price)
                item[0].totality=item[0].count*float(item[0].price)
            item[0].total = (item[0].count - item[0].free_count) * float(item[0].price)
            item[0].save()
        return HttpResponse(ItemList.sum_count())
    return render(request, 'pos/shopping_list.html', {'goodlists': goodlists,'sum_count': ItemList.sum_count()})
def shopping_cart(request):
    itemlists=ItemList.objects.all()
    if request.method=='POST':
        means=request.POST['count']
        item=ItemList.objects.filter(goods_id=request.POST['id'])
        free_goods = PreferentialGoods.objects.filter(goods_id=item[0].goods_id)
        if item:
            item[0].count=item[0].count+int(means)
            if free_goods:
                item[0].free_count=math.floor(item[0].count/3)
                item[0].free_money = item[0].free_count * float(item[0].price)
                item[0].totality=item[0].count*float(item[0].price)
            item[0].total = (item[0].count-item[0].free_count) * float(item[0].price)
            item[0].save()
            if item[0].count==0:
                item[0].delete()
            else:item[0].save()
            result={'quantity':item[0].count,'total':item[0].total,'sum_count':ItemList.sum_count(),
                    'totality':item[0].totality,'free_count':item[0].free_count,'sum_total':ItemList.sum_total()}
        return JsonResponse(result)
    return render(request, 'pos/shopping_cart.html',{'itemlists':itemlists,'sum_count': ItemList.sum_count(),
                                                     'sum_total':ItemList.sum_total()})
def payment(request):
    item_lists = ItemList.objects.all()
    localtime = time.strftime("%Y年%m月%d日 %H:%M:%S",time.localtime(time.time()))
    print(localtime)
    return render(request,'pos/payment.html',{'item_lists':item_lists,'sum_count':ItemList.sum_count(),
                                              'sum_total':ItemList.sum_total(),'sum_free_money':ItemList.sum_free_money(),
                                              'time':localtime})



