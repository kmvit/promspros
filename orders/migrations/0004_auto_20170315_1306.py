# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20170308_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='phone',
            field=models.CharField(max_length=b'18', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
