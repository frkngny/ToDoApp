from django.urls import path
from .views import UserRegister, UserLogin, UserLogoutView, user_logout

urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout', user_logout, name='logout'),
]
