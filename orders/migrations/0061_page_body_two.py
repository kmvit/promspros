# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0060_page_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body_two',
            field=tinymce.models.HTMLField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u0432\u0442\u043e\u0440\u043e\u0439 \u0431\u043b\u043e\u043a', blank=True),
        ),
    ]
