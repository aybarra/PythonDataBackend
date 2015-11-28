# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0024_auto_20151122_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemodel',
            name='player_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='seasonmodel',
            name='player_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
