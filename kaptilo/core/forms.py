from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm


class LinkForm(forms.Form):
    text = forms.CharField(label="Text in note", widget=forms.Textarea)
    # url = forms.SlugField(label="Link name")
    is_delete = forms.BooleanField(label='Delete after reading', required=False)


class LoginForm(AuthenticationForm):
    ...
