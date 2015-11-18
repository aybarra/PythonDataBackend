# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_careermodel_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='pguid',
            field=models.ForeignKey(primary_key=True, serialize=False, to='snippets.PFRtoGuidModel'),
        ),
        migrations.AlterField(
            model_name='careermodel',
            name='win_pct',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
    ]
