# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_itemlist_totality'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='free_money',
            field=models.FloatField(default=0),
        ),
    ]
