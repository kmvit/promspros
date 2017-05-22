# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20170425_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='orders.Subcategory'),
        ),
        migrations.AddField(
            model_name='sentence',
            name='category',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='orders.Subcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=300, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', to='orders.Category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='title',
            field=models.CharField(max_length=300, verbose_name='\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
    ]
