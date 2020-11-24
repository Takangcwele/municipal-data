from django.db import models

from .small_auto_field import SmallAutoField


class AmountType(models.Model):
    code = models.TextField(primary_key=True)
    label = models.TextField()

    class Meta:
        db_table = 'amount_type'


class AmountTypeV2(models.Model):
    id = SmallAutoField(primary_key=True)
    code = models.TextField(unique=True)
    label = models.TextField()

    class Meta:
        db_table = 'amount_type_v2'
