# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_auto_20151112_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='pfrtoguidmodel',
            field=models.OneToOneField(to='snippets.PFRtoGuidModel'),
        ),
    ]
