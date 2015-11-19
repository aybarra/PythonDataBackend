# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0017_auto_20151118_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careermodel',
            name='pfrtoguidmodel',
        ),
        migrations.AddField(
            model_name='careermodel',
            name='player_name',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
