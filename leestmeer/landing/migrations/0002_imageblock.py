# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('block_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='landing.Block')),
                ('source', models.URLField()),
                ('caption', models.TextField()),
            ],
            options={
            },
            bases=('landing.block',),
        ),
    ]
