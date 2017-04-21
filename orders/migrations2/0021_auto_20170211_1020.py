# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20161127_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderimage',
            name='file',
            field=models.ImageField(upload_to=b'images/order', null=True, verbose_name='\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b', blank=True),
        ),
    ]
