# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-14 14:30
from __future__ import unicode_literals

from django.db import migrations
import csv
import os
from django.conf import settings


def drop_indicators(apps, schema_editor):
    Indicator = apps.get_model("metro", "Indicator")
    IndicatorElements = apps.get_model("metro", "IndicatorElements")
    IndicatorQuarterResult = apps.get_model("metro", "IndicatorQuarterResult")

    for element in IndicatorElements.objects.all():
        element.delete()

    for quarter_result in IndicatorQuarterResult.objects.all():
        quarter_result.delete()

    for indicator in Indicator.objects.all():
        indicator.delete()


def add_indicators(apps, schema_editor):
    Indicator = apps.get_model("metro", "Indicator")
    Category = apps.get_model("metro", "Category")
    Geography = apps.get_model("scorecard", "Geography")
    indicator_path = os.path.join(
        settings.BASE_DIR, "metro", "data", "indicator_details.csv"
    )
    with open(indicator_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            category = Category.objects.get(code=row["Category Code"])
            metros = ["BUF", "NMA", "MAN", "EKU", "JHB", "TSH", "ETH", "CPT"]
            for metro in metros:
                try:
                    geography = Geography.objects.get(geo_code=metro)
                    Indicator.objects.create(
                        category=category,
                        geography=geography,
                        code=row["Indicator Code"],
                        name=row["Indicator"],
                        tier=row["Tier"],
                        reporting=row["Reporting Responsibility"],
                        measurement=row["Measurement"],
                        alignment=row["Alignment"],
                        formula=row["Indicator Formula"],
                        frequency=row["Frequency of Reporting"],
                        definition=row["Definition"],
                    )
                except Geography.DoesNotExist:
                    continue


class Migration(migrations.Migration):

    dependencies = [
        ("metro", "0017_indicator_geography"),
    ]

    operations = [
        migrations.RunPython(drop_indicators),
        migrations.RunPython(add_indicators),
    ]
