# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_sentence_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='slug',
            field=models.SlugField(unique=True, max_length=300, verbose_name=b'URL'),
        ),
    ]
