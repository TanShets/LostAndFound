# Generated by Django 3.1.7 on 2021-03-13 23:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0016_auto_20210314_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 14, 5, 25, 46, 5319)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 3, 13, 23, 55, 46, 5319, tzinfo=utc)),
        ),
    ]
