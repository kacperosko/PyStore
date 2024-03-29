# Generated by Django 4.1.5 on 2023-07-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_address_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(blank=True, null=True, through='authentication.User_Address', to='authentication.address'),
        ),
    ]
