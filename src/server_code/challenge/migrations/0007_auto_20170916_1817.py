# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_auto_20170916_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='cops_code_link',
            field=models.CharField(blank=True, help_text='Link to Cops student code', max_length=300),
        ),
        migrations.AddField(
            model_name='settings',
            name='robbers_code_link',
            field=models.CharField(blank=True, help_text='Link to Robbers student code', max_length=300),
        ),
    ]