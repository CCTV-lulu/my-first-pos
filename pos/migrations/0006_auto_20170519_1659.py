# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_preferentialgoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferentialgoods',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
