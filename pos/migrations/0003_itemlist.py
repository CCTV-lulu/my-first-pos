# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_auto_20170503_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(default=0)),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('unit', models.TextField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
