# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_profile_level_up_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level_up_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
