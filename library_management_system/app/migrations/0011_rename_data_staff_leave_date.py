# Generated by Django 4.2.5 on 2023-10-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_staff_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_leave',
            old_name='data',
            new_name='date',
        ),
    ]
