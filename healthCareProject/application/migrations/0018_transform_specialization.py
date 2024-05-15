# Generated by Django 5.0.3 on 2024-05-15 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_remove_transform_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='transform',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.departments'),
        ),
    ]
