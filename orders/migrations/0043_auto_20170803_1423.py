# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_auto_20170803_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='price',
            field=models.DecimalField(null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', max_digits=6, decimal_places=0, blank=True),
        ),
    ]
