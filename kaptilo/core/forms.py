from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm


class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['user', 'text', 'delete_after_watching']


class LoginForm(AuthenticationForm):
    ...
