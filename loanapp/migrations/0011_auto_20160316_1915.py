# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-16 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0010_auto_20160311_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='purpose',
            field=models.CharField(max_length=500),
        ),
    ]
