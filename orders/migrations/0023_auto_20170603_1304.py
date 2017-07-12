# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20170601_0615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('my_order',), 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['title'], 'verbose_name': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', 'verbose_name_plural': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='subsubcategory',
            options={'ordering': ['title'], 'verbose_name': '\u041f\u043e\u0434\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438', 'verbose_name_plural': '\u041f\u043e\u0434\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'},
        ),
        migrations.AddField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
