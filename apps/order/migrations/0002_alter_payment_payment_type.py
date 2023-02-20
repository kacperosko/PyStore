# Generated by Django 4.1.5 on 2023-01-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('CashOnDelivery', 'Cash On Delivery'), ('DebitCards', 'Debit Cards'), ('MobilePayment', 'Mobile Payment'), ('TraditionalTransfer', 'Traditional Transfer')], max_length=255),
        ),
    ]