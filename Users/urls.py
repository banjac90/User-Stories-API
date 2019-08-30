from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('Registration/', RegisterUserAPIView.as_view(), name='User-Register'),      
]