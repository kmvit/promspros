# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20170603_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('body', tinymce.models.HTMLField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0411\u043b\u043e\u043a \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xbe\xd0\xba'),
        ),
    ]
