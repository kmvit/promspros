# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_thumbs.db.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20161103_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.CharField(max_length=9, verbose_name='\u0411\u0418\u041a', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', '\u0422\u043e\u043b\u044c\u043a\u043e \u0446\u0438\u0444\u0440\u044b!')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', '\u0422\u043e\u043b\u044c\u043a\u043e \u0446\u0438\u0444\u0440\u044b!')]),
        ),
        migrations.AlterField(
            model_name='companyimage',
            name='file_up',
            field=django_thumbs.db.models.ImageWithThumbsField(upload_to=b'images/company', blank=True),
        ),
    ]
