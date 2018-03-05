# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0049_auto_20180301_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsubcategory',
            name='title',
            field=models.CharField(max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
