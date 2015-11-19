# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0019_auto_20151119_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='player_name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
