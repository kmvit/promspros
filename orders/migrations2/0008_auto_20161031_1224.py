# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20161031_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyimage',
            old_name='file',
            new_name='file_up',
        ),
    ]
