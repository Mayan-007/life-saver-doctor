from django.urls import path
from life_saver_doctor.views import *

urlpatterns = [
    path('', index, name='index_doctor'),
    path('profile/', profile_completion, name='profile_completion_doctor'),
    path('waitlist/', waitlist, name='waitlist_doctor')
]