# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booknow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('TBA', 'To Be Assigned'), ('As', 'Assigned'), ('Can', 'Cancelled'), ('C', 'Completed')], default='TBA', max_length=4),
        ),
    ]
