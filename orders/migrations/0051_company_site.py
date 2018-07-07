# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0050_auto_20180301_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='site',
            field=models.URLField(max_length=300, verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
    ]
