# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsubcategory',
            name='slug',
            field=models.SlugField(default=b'sd', verbose_name=b'URL', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=b'URL'),
        ),
    ]
