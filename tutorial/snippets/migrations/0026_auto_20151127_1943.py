# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0025_auto_20151127_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='player_name',
        ),
        migrations.RemoveField(
            model_name='seasonmodel',
            name='player_name',
        ),
    ]
