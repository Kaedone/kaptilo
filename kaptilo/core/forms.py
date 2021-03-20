from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LinkForm(forms.Form):
    text = forms.CharField(label="Text in note", widget=forms.Textarea, required=False)
    header = forms.CharField(label="Header", required=True)
    is_delete = forms.BooleanField(label='Delete after reading', required=False)


class RegisterForm(UserCreationForm):
    class Meta:
        help_texts = {
            'email': "Specify your email to receive notifications"
        }
        model = User
        fields = ['username', 'password1', 'password2', 'email']
