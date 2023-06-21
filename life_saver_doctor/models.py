from django.db import models
from life_saver_user_auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=30)
    experience = models.IntegerField()
    qualification = models.CharField(max_length=30)
    fees = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    is_profile_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.email