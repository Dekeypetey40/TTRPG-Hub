# Generated by Django 4.2.4 on 2023-09-18 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_polloption_poll'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='PollOption',
        ),
    ]
