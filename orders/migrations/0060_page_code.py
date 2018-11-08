# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0059_auto_20181106_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='code',
            field=models.TextField(verbose_name='\u041a\u043e\u0434', blank=True),
        ),
    ]
