# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0058_auto_20181103_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(default=b'000000000000', unique=True, max_length=12, verbose_name='\u0418\u041d\u041d'),
        ),
    ]
