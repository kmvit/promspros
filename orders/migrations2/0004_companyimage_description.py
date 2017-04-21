# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20161006_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyimage',
            name='description',
            field=models.CharField(max_length=b'200', verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=b'True'),
        ),
    ]
