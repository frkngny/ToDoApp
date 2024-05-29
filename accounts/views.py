from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.conf import settings

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

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

def user_logout(request):
    logout(request)
    return redirect('%s' % (settings.LOGIN_URL))