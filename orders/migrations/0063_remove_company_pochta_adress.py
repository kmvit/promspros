# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0062_remove_sentence_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='pochta_adress',
        ),
    ]
