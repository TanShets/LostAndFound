# Generated by Django 3.1.2 on 2021-03-13 10:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0004_auto_20210313_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 13, 15, 52, 26, 359213)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 3, 13, 10, 22, 26, 359213, tzinfo=utc)),
        ),
    ]
