from django.shortcuts import render
from .models import GoodsList
from .models import ItemList
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'pos/homepage.html', {})
def shopping_list(request):
    goodslists = GoodsList.objects.all()
    sum_count = 0
    for c in ItemList.objects.all():
        sum_count += c.count
    if request.method=='POST':
        goods=GoodsList.objects.filter(id=request.POST['id'])
        cartchange=ItemList.objects.filter(goods_id=request.POST['id'])
        if cartchange:
             cartchange[0].count+=1
             cartchange[0].save()
        else:
            ItemList.objects.create(
                goods_id=goods[0].id,
                type=goods[0].type,
                name=goods[0].name,
                price=goods[0].price,
                unit=goods[0].unit,
                count=1
            )
        sum_count +=1
        return HttpResponse(sum_count)
    return render(request, 'pos/shopping_list.html', {'goodslists': goodslists,'sum_count':sum_count})
def shopping_cart(request):
    return render(request, 'pos/shopping_cart.html',{})




