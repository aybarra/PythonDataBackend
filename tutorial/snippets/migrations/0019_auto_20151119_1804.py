# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0018_auto_20151119_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='player_name',
            field=models.CharField(max_length=50),
        ),
    ]
