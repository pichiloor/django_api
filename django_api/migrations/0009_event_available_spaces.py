# Generated by Django 4.1 on 2022-08-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0008_alter_room_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available_spaces',
            field=models.IntegerField(default=2),
        ),
    ]
