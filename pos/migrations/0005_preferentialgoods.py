# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_itemlist_free_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferentialGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('goods_id', models.IntegerField()),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('unit', models.TextField()),
                ('price', models.IntegerField()),
                ('activity', models.TextField()),
            ],
        ),
    ]
