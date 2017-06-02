# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170525_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=profiles.models.get_file_path, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True),
        ),
    ]
