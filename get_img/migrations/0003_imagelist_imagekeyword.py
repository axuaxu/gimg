# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0002_imagelist_imageorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelist',
            name='ImageKeyword',
            field=models.CharField(max_length=100, default='google image'),
            preserve_default=True,
        ),
    ]
