# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20170526_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='icon',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='icon',
            field=models.ImageField(upload_to=b'images/icons', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'images/icons', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
        ),
    ]
