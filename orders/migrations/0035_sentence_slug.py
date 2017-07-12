# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20170614_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='slug',
            field=models.SlugField(default=b'ds', max_length=300, verbose_name=b'URL'),
        ),
    ]
