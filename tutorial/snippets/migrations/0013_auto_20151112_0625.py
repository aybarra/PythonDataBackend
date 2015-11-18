# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20151110_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='pfrtoguidmodel',
            field=models.OneToOneField(related_name='careermodel', null=True, to_field=b'pguid', to='snippets.PFRtoGuidModel'),
        ),
        migrations.AlterField(
            model_name='pfrtoguidmodel',
            name='pguid',
            field=models.CharField(unique=True, max_length=40, editable=False, blank=True),
        ),
    ]
