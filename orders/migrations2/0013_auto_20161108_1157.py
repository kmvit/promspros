# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20161108_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyimage',
            name='file_up',
            field=models.ImageField(upload_to=b'images/company', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438', blank=True),
        ),
    ]
