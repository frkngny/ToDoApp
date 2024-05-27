from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        labels = {'email': 'Email', 'username': 'Username', 'password1': 'Password', 'password2': 'Confirm password'}