# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20161031_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bank',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u043d\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.CharField(max_length=9, verbose_name='\u0411\u0418\u041a'),
        ),
        migrations.AlterField(
            model_name='company',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=140, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='company',
            name='pochta_adress',
            field=models.CharField(max_length=300, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='company',
            name='ur_adress',
            field=models.CharField(max_length=300, verbose_name='\u042e\u0440\u0438\u0434\u0438\u0435\u0441\u043a\u0438\u0439 \u0430\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(max_length=100, verbose_name='\u0421\u044b\u043b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442'),
        ),
    ]
