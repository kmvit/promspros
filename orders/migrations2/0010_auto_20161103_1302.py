# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20161103_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.CharField(max_length=9, verbose_name='\u0411\u0418\u041a', validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only alphanumeric characters are allowed.')]),
        ),
    ]
