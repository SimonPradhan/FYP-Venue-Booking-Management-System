# Generated by Django 4.1.13 on 2024-03-03 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0007_rename_username_venue_vendor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='Venuename',
            new_name='venuename',
        ),
    ]
