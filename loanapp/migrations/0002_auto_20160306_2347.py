# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='borrower',
        ),
        migrations.AddField(
            model_name='profile',
            name='loans',
            field=models.ManyToManyField(to='loanapp.Loan'),
        ),
    ]
