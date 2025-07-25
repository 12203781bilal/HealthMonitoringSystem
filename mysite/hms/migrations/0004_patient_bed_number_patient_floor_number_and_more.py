# Generated by Django 5.2.4 on 2025-07-17 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_patient_blood_group_vitalrecord_sugar_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bed_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='floor_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='room_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
    ]
