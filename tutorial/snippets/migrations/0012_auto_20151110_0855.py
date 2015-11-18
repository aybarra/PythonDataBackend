# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20151110_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='pguid',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
        ),
    ]
