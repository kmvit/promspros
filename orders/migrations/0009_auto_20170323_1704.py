# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20170323_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='born',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
