# Generated by Django 4.1.5 on 2023-06-04 12:35

import apps._custom_models.custom_models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=apps._custom_models.custom_models.UpperCaseCharField(max_length=255, unique=True),
        ),
    ]
