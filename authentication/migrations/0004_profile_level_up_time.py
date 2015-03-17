# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150315_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level_up_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 18, 54, 21, 961526, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
