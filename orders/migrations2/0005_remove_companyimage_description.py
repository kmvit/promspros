# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_companyimage_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyimage',
            name='description',
        ),
    ]
