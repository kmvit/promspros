# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0055_auto_20180808_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430'),
        ),
    ]
