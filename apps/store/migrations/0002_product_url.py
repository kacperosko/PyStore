# Generated by Django 4.1.5 on 2023-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
