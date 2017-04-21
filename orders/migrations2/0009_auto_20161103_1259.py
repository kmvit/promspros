# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20161031_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.IntegerField(verbose_name='\u0411\u0418\u041a'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442'),
        ),
        migrations.AlterField(
            model_name='companyimage',
            name='description',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
