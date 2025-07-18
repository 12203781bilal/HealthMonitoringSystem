from django.contrib import admin
from .models import Patient, VitalRecord, Feedback


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'gender',
        'blood_group',
        'contact_number',
        'room_number',
        'floor_number',
        'bed_number',
        'patient_id',  # computed field
    )
    search_fields = ('name', 'contact_number')
    list_filter = ('gender', 'blood_group')


@admin.register(VitalRecord)
class VitalRecordAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'date_recorded',
        'blood_pressure',
        'heart_rate',
        'temperature',
        'sugar_level',
    )
    list_filter = ('date_recorded',)
    search_fields = ('patient__name',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'submitted_at',
        'message',
    )
    list_filter = ('submitted_at',)
    search_fields = ('patient__name', 'message')
