# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0023_seasonaveragemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='game_guid',
            field=models.CharField(max_length=51, serialize=False, primary_key=True, blank=True),
        ),
    ]
