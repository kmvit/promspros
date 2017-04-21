# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20161122_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderimage',
            name='file',
            field=models.FileField(upload_to=b'images/order', null=True, verbose_name='\u0424\u0430\u0439\u043b\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='order',
            field=models.ForeignKey(verbose_name='\u0424\u0430\u0439\u043b\u044b \u0437\u0430\u043a\u0430\u0437\u0430', to='orders.Order'),
        ),
    ]
