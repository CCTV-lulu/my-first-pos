from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^shopping_list',views.shopping_list, name='shopping_list'),
    url(r'^homepage', views.homepage,name='homepage'),
    url(r'^payment', views.payment,name='payment'),
    url(r'^shopping_cart',views.shopping_cart,name='shopping_cart')
]


