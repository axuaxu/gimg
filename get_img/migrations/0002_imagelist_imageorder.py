# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelist',
            name='ImageOrder',
            field=models.CharField(max_length=10, default='9999'),
            preserve_default=True,
        ),
    ]
