# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('answer', models.CharField(max_length=20)),
                ('level', models.IntegerField(unique=True)),
                ('options', models.CharField(max_length=50)),
                ('hint', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
