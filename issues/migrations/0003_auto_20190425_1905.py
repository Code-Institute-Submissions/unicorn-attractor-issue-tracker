# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20190410_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('IC', 'Incomplete'), ('IP', 'In-progress'), ('CT', 'Complete')], default='IC', max_length=2),
        ),
    ]