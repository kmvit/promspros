# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0052_auto_20180713_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='site',
            field=models.URLField(default=b'', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442', blank=True),
        ),
    ]
