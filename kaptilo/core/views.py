from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.shortcuts import render, redirect

from core import forms
from . import models


def homepage(request):
    return render(request, 'homepage.html', {})


def logout(request):
    auth.logout(request)
    return redirect('homepage')


@login_required
@transaction.atomic
def create_link(request):
    f = forms.LinkForm()
    if request.method == 'POST':
        f = forms.LinkForm(request.POST)
        if f.is_valid():
            link = f.save(commit=False)
            link.user = request.user
            link.save()
            messages.success(request, "Note created successfully!")
            return redirect('homepage')
    context = {'form': f}
    return render(request, 'create_link.html', context)


def show_link(request, id):
    m = models.Link.objects.get(pk=id)
    return render(request, 'show_link.html', {'data': m})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('homepage')
    context = {
        "form": form
    }
    return render(request, 'login.html', context)


def register(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration completed successfully!")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
