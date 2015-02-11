# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0003_imagelist_imagekeyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelist',
            name='ImageOrder',
            field=models.IntegerField(default=9999),
            preserve_default=True,
        ),
    ]
