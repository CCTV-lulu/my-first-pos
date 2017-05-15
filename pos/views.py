from django.shortcuts import render
from .models import GoodsList
from .models import ItemList
from django.http import HttpResponse
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
        return HttpResponse(ItemList.sum_count())
    return render(request, 'pos/shopping_list.html', {'goodlists': goodlists,'sum_count': ItemList.sum_count()})
def shopping_cart(request):
    itemlists=ItemList.objects.all()
    return render(request, 'pos/shopping_cart.html',{'itemlists':itemlists,'sum_count': ItemList.sum_count()})




