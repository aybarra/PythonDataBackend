# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0020_auto_20151119_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='pos_type',
            field=models.CharField(default=b'ER', max_length=2, choices=[(b'qb', b'qb'), (b'te', b'te'), (b'wr', b'wr'), (b'rb', b'rb')]),
        ),
    ]
