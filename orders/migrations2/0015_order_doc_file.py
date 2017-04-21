# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_remove_companyimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='doc_file',
            field=models.FileField(upload_to=b'files/order', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb\xd1\x8b', blank=True),
        ),
    ]
