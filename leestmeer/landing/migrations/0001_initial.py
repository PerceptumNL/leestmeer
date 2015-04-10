# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlockHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('block_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='landing.Block')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=('landing.block',),
        ),
    ]
