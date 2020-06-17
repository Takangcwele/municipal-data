# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-02 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("scorecard", "0003_geography_population"),
        ("infrastructure", "0012_auto_20200602_1235"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="project",
            unique_together=set(
                [("geography", "project_number", "function", "project_description")]
            ),
        ),
    ]
