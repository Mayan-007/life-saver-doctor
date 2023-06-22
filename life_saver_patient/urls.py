from django.urls import path
from life_saver_patient.views import *

urlpatterns = [
    path('', index, name='index_patient'),
    path('profile/', profile_completion, name='profile_completion_patient'),
    
    path('doctors/', doctors, name='doctors_patient'),
    path('appointments/', appointments, name='appointments_patient'),
]