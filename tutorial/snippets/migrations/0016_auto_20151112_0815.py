# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0015_auto_20151112_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='pfrtoguidmodel',
            field=models.OneToOneField(null=True, to_field=b'pguid', to='snippets.PFRtoGuidModel'),
        ),
    ]
