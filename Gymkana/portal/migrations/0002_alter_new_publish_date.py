# Generated by Django 3.2.7 on 2021-09-08 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 14, 39, 8, 22803, tzinfo=utc)),
        ),
    ]
