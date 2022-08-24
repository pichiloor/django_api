# Generated by Django 4.1 on 2022-08-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0004_booking_customer_booking_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('reserved', 'reserved'), ('cancelled', 'cancelled')], default='reserved', max_length=50),
        ),
    ]
