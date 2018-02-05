# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_blockonpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='keywords',
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.TextField(),
        ),
    ]
