from django.urls import path, include
from .views import UserRegister, UserLogin

urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login'),
]
