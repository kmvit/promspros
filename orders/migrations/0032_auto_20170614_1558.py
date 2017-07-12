# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20170614_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsubcategory',
            name='slug',
            field=models.SlugField(default=b'sd', max_length=300, verbose_name=b'URL', blank=True),
        ),
    ]
