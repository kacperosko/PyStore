# Generated by Django 4.1.5 on 2023-06-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_user_address_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(through='authentication.User_Address', to='authentication.address'),
        ),
    ]
