# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0021_careermodel_pos_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='player_name',
            field=models.CharField(max_length=50),
        ),
    ]
