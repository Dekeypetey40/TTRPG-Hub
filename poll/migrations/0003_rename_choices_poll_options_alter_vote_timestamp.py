# Generated by Django 4.2.4 on 2023-09-19 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='choices',
            new_name='options',
        ),
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 12, 51, 29, 556722, tzinfo=datetime.timezone.utc)),
        ),
    ]
