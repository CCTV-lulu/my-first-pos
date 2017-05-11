# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('unit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                # ('goods_id', models.IntegerField(default=0)),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('unit', models.TextField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
