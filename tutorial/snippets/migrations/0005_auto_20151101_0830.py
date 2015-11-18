# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20151031_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careermodel',
            old_name='end_date',
            new_name='end_year',
        ),
        migrations.RenameField(
            model_name='careermodel',
            old_name='start_date',
            new_name='start_year',
        ),
        migrations.RenameField(
            model_name='pfrtoguidmodel',
            old_name='player_full_name',
            new_name='player_name',
        ),
        migrations.AddField(
            model_name='pfrtoguidmodel',
            name='pos_type',
            field=models.CharField(default=b'ER', max_length=2, choices=[(b'qb', b'qb'), (b'te', b'te'), (b'wr', b'wr'), (b'rb', b'rb')]),
        ),
    ]
