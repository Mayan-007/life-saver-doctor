from django.contrib import admin
from life_saver_patient.models import Patient

class patientAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_profile_complete')
    
admin.site.register(Patient, patientAdmin)
