# Generated by Django 5.0.1 on 2024-02-07 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
    ]
