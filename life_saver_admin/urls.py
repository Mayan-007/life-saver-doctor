from django.urls import path
from life_saver_admin.views import *

urlpatterns = [
    path('', index, name='index_admin'),
    path('waitlist/', waitlist, name='waitlist_admin'),
    
    path('doctors/', doctors, name='doctors_admin'),
    path('accept_doctor/<int:doctor_id>/', accept_doctor, name='accept_doctor'),
    path('reject_doctor/<int:doctor_id>/', reject_doctor, name='reject_doctor'),
    
    path('patients/', patients, name='patients_admin'),
    path('reject_patient/<int:patient_id>/', reject_patient, name='reject_patient'),
    
    path('appointments/', appointments, name='appointments_admin'),
    path('appointment/<int:appointment_id>/', appointment, name='appointment_admin'),
]