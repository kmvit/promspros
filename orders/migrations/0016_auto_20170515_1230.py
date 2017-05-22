# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20170425_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='company',
            name='bik',
        ),
    ]
