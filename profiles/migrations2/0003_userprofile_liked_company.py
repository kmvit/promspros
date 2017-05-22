# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20161006_0859'),
        ('profiles', '0002_remove_userprofile_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_company',
            field=models.ManyToManyField(to='orders.Company', verbose_name='\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True),
        ),
    ]
