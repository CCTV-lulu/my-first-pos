# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_itemlist_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
