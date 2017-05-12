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
    def sum_count():
        sum_count = 0
        for goods in ItemList.objects.all():
            sum_count+=goods.count
        return sum_count

