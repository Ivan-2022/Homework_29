# Generated by Django 4.1.1 on 2022-10-03 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_location_id_user_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='locations',
        ),
    ]