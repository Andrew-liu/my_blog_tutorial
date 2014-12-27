# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
