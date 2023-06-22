from django.db import models
from life_saver_doctor.models import Doctor
from life_saver_patient.models import Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, default='pending')
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.doctor.user.first_name + ' ' + self.doctor.user.last_name + ' - ' + self.patient.user.first_name + ' ' + self.patient.user.last_name + ' - ' + str(self.date) + ' - ' + str(self.time)
    
    class Meta:
        verbose_name_plural = 'Appointments'
        ordering = ['-date', '-time']

