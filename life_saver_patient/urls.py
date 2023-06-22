from django.urls import path
from life_saver_patient.views import *

urlpatterns = [
    path('', index, name='index_patient'),
    path('profile/', profile_completion, name='profile_completion_patient'),
    
    path('doctors/', doctors, name='doctors_patient'),
    path('appointments/', appointments, name='appointments_patient'),
    path('book_appointment/<int:doctor_id>/', book_appointment, name='book_appointment_patient'),
    path('reschedule_appointment/<int:appointment_id>/', reschedule_appointment, name='reschedule_appointment_patient'),
    path('cancel_appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment_patient')
]