# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-07 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_libro_imagenurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]