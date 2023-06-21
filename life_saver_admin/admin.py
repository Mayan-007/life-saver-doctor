from django.contrib import admin
from life_saver_admin.models import Admin

class adminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    
admin.site.register(Admin, adminAdmin)