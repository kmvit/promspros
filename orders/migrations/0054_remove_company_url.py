# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0053_auto_20180713_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='url',
        ),
    ]
