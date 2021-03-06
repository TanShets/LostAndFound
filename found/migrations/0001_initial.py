# Generated by Django 3.1.2 on 2021-03-13 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('loc_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('tags', models.CharField(max_length=200)),
                ('time_found', models.DateTimeField(auto_now_add=True)),
                ('location_found', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='found.location')),
            ],
        ),
    ]
