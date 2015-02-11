# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0006_imagestage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ImageOrder', models.IntegerField(default=9999)),
                ('ImageURL', models.CharField(max_length=300)),
                ('ImageREF', models.CharField(max_length=300)),
                ('ImageTitle', models.CharField(max_length=200)),
                ('ImageKeyword', models.CharField(default='google image', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
