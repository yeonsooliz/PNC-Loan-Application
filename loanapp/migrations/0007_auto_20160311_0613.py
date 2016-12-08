# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0006_auto_20160311_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loanapp.Account'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='people',
            field=models.ManyToManyField(to='loanapp.Profile'),
        ),
    ]
