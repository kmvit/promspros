# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-born'], 'verbose_name': '\u0417\u0430\u043a\u0430\u0437', 'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b'},
        ),
        migrations.AlterModelOptions(
            name='sentence',
            options={'ordering': ['-born'], 'verbose_name': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.CharField(max_length=9, verbose_name='\u0411\u0418\u041a', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='born',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='born',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
