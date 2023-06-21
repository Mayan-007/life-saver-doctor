from django.urls import path
from life_saver_user_auth.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact', contact, name='contact'),
    
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]