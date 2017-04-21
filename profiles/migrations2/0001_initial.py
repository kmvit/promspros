# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('orders', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default=b'\xd0\xa4\xd0\x98\xd0\x9e', max_length=b'200', verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e')),
                ('phone', models.CharField(default=b'+7123456789', max_length=b'12', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('site', models.CharField(default=b'www.mysite.ru', max_length=b'30', verbose_name='\u0421\u0430\u0439\u0442')),
                ('liked_order', models.ManyToManyField(to='orders.Order', verbose_name='\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0437\u0430\u043a\u0430\u0437\u044b', blank=True)),
                ('liked_sentence', models.ManyToManyField(to='orders.Sentence', verbose_name='\u0418\u0437\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
