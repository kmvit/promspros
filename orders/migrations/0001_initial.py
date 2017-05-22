# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=300, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', blank=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
                ('url', models.CharField(max_length=100, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0430\u0439\u0442')),
                ('city', models.CharField(max_length=140, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('ur_adress', models.CharField(max_length=300, verbose_name='\u042e\u0440\u0438\u0434\u0438\u0435\u0441\u043a\u0438\u0439 \u0430\u0434\u0440\u0435\u0441')),
                ('pochta_adress', models.CharField(max_length=300, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441')),
                ('inn', models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', '\u0422\u043e\u043b\u044c\u043a\u043e \u0446\u0438\u0444\u0440\u044b!')])),
                ('bik', models.CharField(max_length=9, verbose_name='\u0411\u0418\u041a', validators=[django.core.validators.RegexValidator(b'^[0-9]*$', '\u0422\u043e\u043b\u044c\u043a\u043e \u0446\u0438\u0444\u0440\u044b!')])),
                ('bank', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u043d\u043a\u0430')),
                ('user', models.ForeignKey(default=b'1', verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043f\u0430\u043d\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_up', models.ImageField(upload_to=b'images/company', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438', blank=True)),
                ('order', models.ForeignKey(verbose_name='\u0424\u043e\u0442\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438', to='orders.Company')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('born', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('name', models.CharField(max_length=b'200', verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('phone', models.CharField(max_length=b'12', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('city', models.CharField(max_length=b'100', verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('body', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('status', models.CharField(default=b'1', max_length=50, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'1', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'), (b'2', b'\xd0\x9d\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'), (b'3', b'\xd0\x92 \xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba')])),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-born'],
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'images/order', null=True, verbose_name='\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b', blank=True)),
                ('order', models.ForeignKey(verbose_name='\u0424\u0430\u0439\u043b\u044b \u0437\u0430\u043a\u0430\u0437\u0430', to='orders.Order')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u0437\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('keywords', models.CharField(max_length=200, verbose_name='keywords')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('body', tinymce.models.HTMLField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('born', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('name', models.CharField(max_length=b'200', verbose_name='\u0418\u043c\u044f \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('phone', models.CharField(max_length=b'12', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('city', models.CharField(max_length=b'100', verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('body', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('price', models.DecimalField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c', max_digits=6, decimal_places=0)),
                ('status', models.CharField(default=b'1', max_length=50, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'1', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'), (b'2', b'\xd0\x9d\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'), (b'3', b'\xd0\x92 \xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba')])),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-born'],
                'verbose_name': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='SentenceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'images/sentence', null=True, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438', blank=True)),
                ('sentence', models.ForeignKey(verbose_name='\u0424\u043e\u0442\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f', to='orders.Sentence')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e',
            },
        ),
    ]
