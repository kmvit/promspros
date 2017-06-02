# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20170531_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='category',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='orders.Subsubcategory'),
        ),
    ]
