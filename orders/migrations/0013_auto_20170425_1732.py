# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20170324_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
                ('parent', models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to='orders.Category')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
                'verbose_name_plural': '\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'1', max_length=50, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'1', b'\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5'), (b'2', b'\xd0\xbd\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5'), (b'3', b'\xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba\xd0\xb8')]),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='status',
            field=models.CharField(default=b'1', max_length=50, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'1', b'\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5'), (b'2', b'\xd0\xbd\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5'), (b'3', b'\xd1\x87\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba\xd0\xb8')]),
        ),
    ]
