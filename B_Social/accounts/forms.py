# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'school_number', 'department', 'class_name', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

