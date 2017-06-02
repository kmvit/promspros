# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20170531_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsubcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('icon', models.ImageField(upload_to=b'images/icons', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8', blank=True)),
                ('parent', models.ForeignKey(verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c', to='orders.Subcategory')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='orders.Subsubcategory'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='orders.Subsubcategory'),
        ),
    ]
