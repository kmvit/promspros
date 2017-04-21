# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20161108_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyimage',
            name='description',
        ),
    ]
