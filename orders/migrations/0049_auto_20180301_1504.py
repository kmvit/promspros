# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0048_auto_20180119_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(verbose_name=b'URL', blank=True),
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=b'URL'),
        ),
    ]
