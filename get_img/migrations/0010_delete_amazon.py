# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_img', '0009_amazon_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='amazon',
        ),
    ]
