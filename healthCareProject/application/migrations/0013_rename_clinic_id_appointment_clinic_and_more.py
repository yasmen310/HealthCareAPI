# Generated by Django 5.0.3 on 2024-05-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_rename_clinic_appointment_clinic_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='clinic_id',
            new_name='clinic',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='specialization_id',
            new_name='specialization',
        ),
    ]
