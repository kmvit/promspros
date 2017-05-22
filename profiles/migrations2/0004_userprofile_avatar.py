# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_liked_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'images/avatar', verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
    ]
