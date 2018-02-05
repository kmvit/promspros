# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_auto_20180116_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockonPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('block_one', tinymce.models.HTMLField(blank=True)),
                ('block_two', tinymce.models.HTMLField(blank=True)),
                ('block_three', tinymce.models.HTMLField(blank=True)),
            ],
            options={
                'verbose_name': '\u0411\u043b\u043e\u043a \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435',
                'verbose_name_plural': '\u0411\u043b\u043e\u043a\u0438 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435',
            },
        ),
    ]
