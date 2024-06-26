# Generated by Django 5.0.3 on 2024-05-12 09:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_doctor_assistant_name_doctor_assistant_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientName', models.CharField(max_length=100)),
                ('patientIMG', models.ImageField(blank=True, null=True, upload_to='PatientIMG/')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('patient_id', models.CharField(max_length=14, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{14}$', 'patient_id must be exactly 14 digits')])),
                ('medicalHistory', models.TextField(blank=True, null=True)),
                ('prescription', models.ImageField(blank=True, null=True, upload_to='prescriptions/')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.location')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.patient'),
        ),
    ]
