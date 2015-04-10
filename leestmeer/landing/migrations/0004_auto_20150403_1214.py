# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20150403_1142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlockAdmin',
        ),
        migrations.RemoveField(
            model_name='blockholderadmin',
            name='blocks',
        ),
        migrations.DeleteModel(
            name='BlockHolderAdmin',
        ),
        migrations.RemoveField(
            model_name='textblock',
            name='title',
        ),
        migrations.AddField(
            model_name='block',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
