# Generated by Django 5.0.3 on 2024-05-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_doctor_aboutme_doctor_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='departments',
            new_name='available_departments',
        ),
    ]
