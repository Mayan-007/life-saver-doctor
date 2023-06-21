from django.urls import path
from life_saver_admin.views import *

urlpatterns = [
    path('', index, name='index_admin')
]