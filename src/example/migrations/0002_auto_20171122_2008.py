# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='fieldsignal',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Do not touch it'),
        ),
    ]
