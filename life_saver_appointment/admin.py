from django.contrib import admin
from life_saver_appointment.models import Appointment

class appointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time')
    
admin.site.register(Appointment, appointmentAdmin)
