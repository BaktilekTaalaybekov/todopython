# Generated by Django 3.1.5 on 2021-01-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Text',
            new_name='text',
        ),
    ]
