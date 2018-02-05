# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0044_remove_company_inn'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=orders.models.get_file_path, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='description',
            field=tinymce.models.HTMLField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
    ]
