# Generated by Django 5.0.3 on 2024-05-11 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_departments_hospital_available_departments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='available_departments',
            new_name='departments',
        ),
    ]