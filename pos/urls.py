from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.pos_list, name='pos_list'),
]