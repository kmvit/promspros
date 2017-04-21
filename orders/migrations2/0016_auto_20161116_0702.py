# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_doc_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='doc_file',
            field=models.FileField(upload_to=b'files/sentence', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd1\x8c \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='doc_file',
            field=models.FileField(upload_to=b'files/order', verbose_name=b'\xd0\x94\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd1\x8c \xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb\xd1\x8b', blank=True),
        ),
    ]
