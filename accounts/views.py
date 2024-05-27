from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import RegisterForm


class UserRegister(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

class UserLogin(LoginView):
    template_name = 'accounts/login.html'

class UserLogout(LogoutView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return redirect('login')