from django.shortcuts import render
from .models import GoodsList
# Create your views here.
def homepage(request):
    return render(request, 'pos/homepage.html', {})
def shopping_list(request):
    goodslists = GoodsList.objects.all()
    return render(request, 'pos/shopping_list.html', {'goodslists':goodslists})
def shopping_cart(request):
    return render(request, 'pos/shopping_cart.html',{})