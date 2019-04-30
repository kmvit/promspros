# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0061_page_body_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='price',
        ),
    ]
