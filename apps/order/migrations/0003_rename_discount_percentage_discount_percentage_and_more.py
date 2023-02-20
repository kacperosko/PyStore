# Generated by Django 4.1.5 on 2023-01-17 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_payment_payment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='discount_percentage',
            new_name='percentage',
        ),
        migrations.AddField(
            model_name='discount',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
