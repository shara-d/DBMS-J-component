from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DetailsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name',
                  'student_id', 'email', 'level', 'degree_name']
