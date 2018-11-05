# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0057_auto_20180808_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='inn',
            field=models.CharField(default=b'000000000000', max_length=12, verbose_name='\u0418\u041d\u041d'),
        ),
        migrations.AlterField(
            model_name='company',
            name='ur_adress',
            field=models.CharField(max_length=300, verbose_name='\u042e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
    ]
