# Generated by Django 4.1.13 on 2024-01-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0004_alter_venue_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
