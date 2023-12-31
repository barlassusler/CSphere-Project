from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CustomAuthenticationForm(AuthenticationForm):


    class Meta:
        model = AuthenticationForm
        fields = ['student number', 'password']