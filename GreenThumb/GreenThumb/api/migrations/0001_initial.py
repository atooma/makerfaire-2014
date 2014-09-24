# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DHTSensor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('humidity', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
