# Generated by Django 5.0.3 on 2024-03-10 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrepreneur',
            old_name='tame_created',
            new_name='time_created',
        ),
        migrations.RenameField(
            model_name='factory',
            old_name='tame_created',
            new_name='time_created',
        ),
        migrations.RenameField(
            model_name='network',
            old_name='tame_created',
            new_name='time_created',
        ),
    ]
