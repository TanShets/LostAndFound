# Generated by Django 3.1.7 on 2021-03-13 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_meetup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='receiver',
            new_name='found_end',
        ),
        migrations.RenameField(
            model_name='meetup',
            old_name='sender',
            new_name='lost_end',
        ),
    ]