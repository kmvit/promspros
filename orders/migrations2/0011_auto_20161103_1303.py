# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20161103_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d', validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only alphanumeric characters are allowed.')]),
        ),
    ]
