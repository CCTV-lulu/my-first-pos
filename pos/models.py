from django.db import models
class GoodsList(models.Model):
    type=models.TextField()
    name=models.TextField()
    price=models.TextField()
    unit=models.TextField()

class ItemList(models.Model):
    goods_id=models.IntegerField(default=0)
    type=models.TextField()
    name=models.TextField()
    price=models.TextField()
    unit=models.TextField()
    count=models.IntegerField()


