# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_markdown.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time']},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_markdown.models.MarkdownField(default=datetime.datetime(2014, 12, 27, 11, 32, 19, 170141, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
