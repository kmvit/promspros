# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0043_auto_20170803_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='inn',
        ),
    ]
