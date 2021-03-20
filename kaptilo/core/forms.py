from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['user', 'text', 'delete_after_watching']


class RegisterForm(UserCreationForm):
    class Meta:
        help_texts = {
            'email': "Specify your email to receive notifications"
        }
        model = User
        fields = ['username', 'password1', 'password2', 'email']
