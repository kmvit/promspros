# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20170515_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'/icons/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='icon',
            field=models.ImageField(upload_to=b'/icons/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
        ),
    ]
