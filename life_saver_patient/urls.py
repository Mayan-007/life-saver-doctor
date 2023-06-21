from django.urls import path
from life_saver_patient.views import *

urlpatterns = [
    path('', index, name='index_patient'),
    path('profile/', profile_completion, name='profile_completion_patient'),
]