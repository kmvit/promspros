# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20170323_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='info',
            field=models.TextField(max_length=900, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True),
        ),
    ]
