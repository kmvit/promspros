# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_companyimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyimage',
            name='description',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='companyimage',
            name='file',
            field=models.FileField(upload_to=b'images/company', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438', blank=True),
        ),
    ]
