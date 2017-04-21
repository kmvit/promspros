# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20161116_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='location',
            new_name='city',
        ),
    ]
