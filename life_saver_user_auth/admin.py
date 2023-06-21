from django.contrib import admin
from life_saver_user_auth.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'password', 'role')
    
admin.site.register(User, UserAdmin)