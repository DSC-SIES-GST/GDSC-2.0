# Generated by Django 4.1.4 on 2023-01-07 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]