from django.shortcuts import render

# Create your views here.
def pos_list(request):
    return render(request, 'pos/pos_list.html', {})