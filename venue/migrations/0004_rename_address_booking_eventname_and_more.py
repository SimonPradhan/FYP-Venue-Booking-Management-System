# Generated by Django 4.1.13 on 2024-02-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0003_booking_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='address',
            new_name='eventName',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='email',
            new_name='eventType',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='message',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
