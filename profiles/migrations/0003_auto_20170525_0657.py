# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170525_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to=b'images/avatar', verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True),
        ),
    ]
