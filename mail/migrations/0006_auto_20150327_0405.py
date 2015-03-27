# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_auto_20150324_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='company_name',
        ),
        migrations.AddField(
            model_name='receiver',
            name='city',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receiver',
            name='company',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receiver',
            name='country',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='receiver',
            name='mail_address',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='receiver',
            name='title',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
