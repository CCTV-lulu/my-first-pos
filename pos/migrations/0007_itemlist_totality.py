# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_auto_20170519_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='totality',
            field=models.FloatField(default=0),
        ),
    ]
