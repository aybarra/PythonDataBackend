# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20151101_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='end_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='careermodel',
            name='start_year',
            field=models.IntegerField(),
        ),
    ]
