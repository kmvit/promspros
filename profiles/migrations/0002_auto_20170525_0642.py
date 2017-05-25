# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=b'images/avatar', verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='liked_company',
            field=models.ManyToManyField(to='orders.Company', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb1\xd1\x80\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='liked_order',
            field=models.ManyToManyField(to='orders.Order', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb1\xd1\x80\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='liked_sentence',
            field=models.ManyToManyField(to='orders.Sentence', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb1\xd1\x80\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=b'+7123456789', max_length=b'12', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
        ),
    ]
