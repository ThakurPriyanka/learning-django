# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 07:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 10, 7, 2, 15, 80032, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
