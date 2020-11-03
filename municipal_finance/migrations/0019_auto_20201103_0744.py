# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-11-03 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import municipal_finance.models.small_auto_field


class Migration(migrations.Migration):

    dependencies = [
        ('municipal_finance', '0018_income_expenditure_items_mscoa_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BsheetFactsMSCOA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demarcation_code', models.TextField()),
                ('period_code', models.TextField()),
                ('amount', models.BigIntegerField(null=True)),
                ('financial_year', models.IntegerField()),
                ('period_length', models.TextField()),
                ('financial_period', models.IntegerField()),
                ('amount_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='municipal_finance.AmountTypeMSCOA')),
            ],
            options={
                'db_table': 'bsheet_facts_mscoa',
            },
        ),
        migrations.CreateModel(
            name='BsheetItemsMSCOA',
            fields=[
                ('label', models.TextField()),
                ('position_in_return_form', models.IntegerField(null=True)),
                ('return_form_structure', models.TextField(null=True)),
                ('composition', models.TextField(null=True)),
                ('id', municipal_finance.models.small_auto_field.SmallAutoField(primary_key=True, serialize=False)),
                ('code', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'bsheet_items_mscoa',
            },
        ),
        migrations.RenameModel(
            old_name='BsheetFacts',
            new_name='BsheetFactsLegacy',
        ),
        migrations.RenameModel(
            old_name='BsheetItems',
            new_name='BsheetItemsLegacy',
        ),
        migrations.AddField(
            model_name='bsheetfactsmscoa',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='municipal_finance.BsheetItemsMSCOA'),
        ),
        migrations.AddIndex(
            model_name='bsheetfactsmscoa',
            index=models.Index(fields=['item_id'], name='bsheet_fact_item_id_0e1e16_idx'),
        ),
        migrations.AddIndex(
            model_name='bsheetfactsmscoa',
            index=models.Index(fields=['amount_type_id'], name='bsheet_fact_amount__a1b81c_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='bsheetfactsmscoa',
            unique_together=set([('amount_type', 'demarcation_code', 'financial_period', 'financial_year', 'item', 'period_length'), ('demarcation_code', 'period_code', 'item')]),
        ),
    ]