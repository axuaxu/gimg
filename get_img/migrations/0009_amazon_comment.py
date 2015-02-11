# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0008_amazon'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazon',
            name='comment',
            field=models.CharField(max_length=100, default='aabb'),
            preserve_default=True,
        ),
    ]
