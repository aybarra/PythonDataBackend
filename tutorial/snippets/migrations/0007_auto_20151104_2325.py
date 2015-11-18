# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20151104_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonmodel',
            name='season_guid',
            field=models.CharField(max_length=45, serialize=False, primary_key=True, blank=True),
        ),
    ]
