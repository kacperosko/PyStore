# Generated by Django 4.1.5 on 2023-06-04 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_discount_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='selected_attributes',
        ),
    ]
