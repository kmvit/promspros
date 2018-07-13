# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0051_company_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='site',
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.URLField(default=b'', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442', blank=True),
        ),
    ]
