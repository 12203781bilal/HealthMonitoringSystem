# Generated by Django 5.2.4 on 2025-07-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0005_alter_patient_user_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
