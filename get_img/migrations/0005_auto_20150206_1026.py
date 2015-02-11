# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0004_auto_20150204_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageStore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ImageOrder', models.IntegerField(default=9999)),
                ('ImageURL', models.CharField(max_length=300)),
                ('ImageREF', models.CharField(max_length=300)),
                ('ImageTitle', models.CharField(max_length=200)),
                ('ImageKeyword', models.CharField(max_length=100, default='google image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ImageList',
        ),
    ]
