from django.shortcuts import render
from .models import GoodsList
from .models import ItemList
from django.http import HttpResponse
from django.http import JsonResponse
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
    if request.method=='POST':
        means=request.POST['count']
        item=ItemList.objects.filter(goods_id=request.POST['id'])
        if item:
            item[0].count=item[0].count+int(means)
            # item[0].total=(item[0].count)*float(item[0].price)
            if item[0].count==0:
                item[0].delete()
            else:item[0].save()
            quantity=item[0].count
            # total=item[0].total
            totality=ItemList.totality()
            print(totality)
            sum_count=ItemList.sum_count()
            print(sum_count)
            result={'quantity':quantity,'totality':totality,'sum_count':sum_count}
        return JsonResponse(result)
    return render(request, 'pos/shopping_cart.html',{'itemlists':itemlists,'sum_count': ItemList.sum_count(),'totality':ItemList.totality()})




