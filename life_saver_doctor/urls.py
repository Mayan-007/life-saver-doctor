from django.urls import path
from life_saver_doctor.views import *

urlpatterns = [
    path('', index, name='index_doctor'),
    path('profile/', profile_completion, name='profile_completion_doctor'),
    path('waitlist/', waitlist, name='waitlist_doctor'),
    path('patients/', patients, name='patients_doctor'),
    
    path('appointments/', appointments, name='appointments_doctor'),
    path('appointment_history/', appointment_history, name='appointment_history_doctor'),
    path('appointment/<int:appointment_id>/', appointment, name='appointment_doctor'),
    path('accept_appointment/<int:appointment_id>/', accept_appointment, name='accept_appointment_doctor'),
    path('reject_appointment/<int:appointment_id>/', reject_appointment, name='reject_appointment_doctor'),
    path('complete_appointment/<int:appointment_id>/', complete_appointment, name='complete_appointment_doctor'),
]