# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-25 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0015_auto_20160425_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='min_monthly_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='monthly_amt',
            field=models.DecimalField(decimal_places=2, default='10.0', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='original_amt',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
    ]