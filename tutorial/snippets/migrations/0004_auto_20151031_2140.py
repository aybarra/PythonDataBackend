# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_careermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pfrtoguidmodel',
            old_name='pro_football_ref_name',
            new_name='pfr_name',
        ),
    ]
