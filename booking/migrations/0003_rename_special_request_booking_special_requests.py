# Generated by Django 5.0.6 on 2024-07-05 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_number_booking_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='special_request',
            new_name='special_requests',
        ),
    ]
