# Generated by Django 4.1.4 on 2023-01-09 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_alter_domain_slug_alter_member_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='domain',
            new_name='title',
        ),
    ]