# Generated by Django 4.1 on 2022-08-25 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0003_event_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='room',
        ),
    ]
