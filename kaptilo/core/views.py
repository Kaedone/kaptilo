from django.shortcuts import render, redirect
from django.contrib import auth
from core import forms
from django.contrib.auth.decorators import login_required
from django.db import transaction
from . import models
from django.contrib import messages


def homepage(request):
    return render(request, 'homepage.html', {})


def logout(request):
    auth.logout(request)
    return redirect('homepage')


@login_required
@transaction.atomic
def create_link(request):
    content = {}
    if request.method == 'POST':
        f = forms.LinkForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            m = models.Link()
            m.user = request.user
            m.text = f.cleaned_data['text']
            m.delete_after_watching = f.cleaned_data['is_delete']
            m.save()
            messages.success(request, "Note created successfully!")
            return redirect('homepage')
        else:
            content = {'form': forms.LinkForm(),
                       'is_alert': True}
    else:
        content = {'form': forms.LinkForm()}
    return render(request, 'create_link.html', content)

def show_link(request, ):
    ...


def login(request):
    form = forms.LoginForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)

