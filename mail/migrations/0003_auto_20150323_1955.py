# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='content',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
    ]
