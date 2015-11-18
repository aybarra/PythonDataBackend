# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonModel',
            fields=[
                ('season_guid', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('pguid', models.CharField(max_length=40)),
                ('year', models.IntegerField()),
                ('games_played', models.IntegerField(default=0, null=True)),
                ('pass_tds', models.IntegerField(default=0, null=True)),
                ('pass_yards', models.IntegerField(default=0, null=True)),
                ('ints_thrown', models.IntegerField(default=0, null=True)),
                ('rec_tds', models.IntegerField(default=0, null=True)),
                ('rec_yards', models.IntegerField(default=0, null=True)),
                ('rush_tds', models.IntegerField(default=0, null=True)),
                ('rush_yards', models.IntegerField(default=0, null=True)),
                ('kr_tds', models.IntegerField(default=0, null=True)),
                ('pr_tds', models.IntegerField(default=0, null=True)),
                ('fumbles_lost', models.IntegerField(default=0, null=True)),
                ('season_ff_pts', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
