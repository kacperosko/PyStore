# Generated by Django 4.1.5 on 2023-07-12 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commentuserlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]