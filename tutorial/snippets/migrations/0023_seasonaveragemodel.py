# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0022_auto_20151119_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonAverageModel',
            fields=[
                ('year', models.IntegerField(serialize=False, primary_key=True)),
                ('ff_pt_average', models.IntegerField()),
            ],
        ),
    ]
