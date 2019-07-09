# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0063_remove_company_pochta_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='top_description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x92\xd0\xb5\xd1\x80\xd1\x85\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='top_description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x92\xd0\xb5\xd1\x80\xd1\x85\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='subsubcategory',
            name='top_description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x92\xd0\xb5\xd1\x80\xd1\x85\xd0\xbd\xd0\xb5\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='info',
            field=models.TextField(max_length=1900, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ur_adress',
            field=models.CharField(max_length=300, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
    ]
