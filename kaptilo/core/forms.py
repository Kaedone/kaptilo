from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = ['permanent', 'link']
        help_texts = {
            "permanent": "If selected, the link won't be deleted after the first use",
            "link": "People will be redirected to this address after following the link"
        }
        widgets = {
            "link": forms.TextInput(attrs={
                "placeholder": "https://..."
            })
        }


class RegisterForm(UserCreationForm):
    class Meta:
        help_texts = {
            'email': "Specify your email to receive notifications"
        }
        model = User
        fields = ['username', 'password1', 'password2', 'email']
