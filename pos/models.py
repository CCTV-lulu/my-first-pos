from django.db import models
class GoodsList(models.Model):
    type=models.TextField()
    name=models.TextField()
    price=models.TextField()
    unit=models.TextField()
