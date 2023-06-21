from django.contrib import admin
from life_saver_doctor.models import Doctor

class doctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'is_profile_complete')
    
admin.site.register(Doctor, doctorAdmin)