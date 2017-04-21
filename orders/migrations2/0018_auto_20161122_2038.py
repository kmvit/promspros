# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20161122_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435'),
        ),
    ]
