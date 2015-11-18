# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_seasonmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerModel',
            fields=[
                ('pguid', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('ff_pts', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('win_pct', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
