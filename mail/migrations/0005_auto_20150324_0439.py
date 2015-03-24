# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20150323_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='receivers',
            field=models.ManyToManyField(to='mail.Receiver', null=True, blank=True),
            preserve_default=True,
        ),
    ]
