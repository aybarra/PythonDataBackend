# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0026_auto_20151127_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonmodel',
            name='games_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seasonmodel',
            name='season_ff_pts',
            field=models.IntegerField(default=0),
        ),
    ]
