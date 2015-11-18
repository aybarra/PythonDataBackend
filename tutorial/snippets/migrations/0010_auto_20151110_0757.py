# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20151110_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='pguid',
            field=models.OneToOneField(primary_key=True, serialize=False, to='snippets.PFRtoGuidModel'),
        ),
    ]
