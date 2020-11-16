# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tablib

from django.db import migrations, models

from ..resources import CashflowItemsMSCOAResource


def import_initial_data(apps, schema_editor):
    dataset = tablib.Dataset().load(
        open('municipal_finance/fixtures/initial/cash_flow_items_mscoa.csv')
    )
    CashflowItemsMSCOAResource().import_data(dataset, raise_errors=True)


class Migration(migrations.Migration):

    dependencies = [
        ('municipal_finance', '0014_amount_type_mscoa_initial_data'),
    ]

    operations = [
        migrations.RunPython(import_initial_data)
    ]
