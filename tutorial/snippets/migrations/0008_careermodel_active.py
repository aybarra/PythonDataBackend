# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20151104_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
