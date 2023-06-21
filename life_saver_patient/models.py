from django.db import models
from life_saver_user_auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=30)
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    is_profile_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.email