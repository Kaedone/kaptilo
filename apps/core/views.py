from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.shortcuts import render, redirect

from apps.core import forms
from apps.core import models


def logout(request):
    auth.logout(request)
    return redirect('homepage')


@login_required
@transaction.atomic
def create_link(request):
    form = forms.LinkForm()
    if request.method == 'POST':
        form = forms.LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            link.get_shortened_link(request)
            messages.success(request, "Link was created successfully!")
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'create_link.html', context)


def follow_link(request, pk: int):
    m = models.Link.objects.get(pk=pk)
    m.uses += 1
    m.save()
    return redirect(m.link)


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


def profile(request):
    links = models.Link.objects.filter(user=request.user)
    context = {
        "links": links
    }
    return render(request, "profile.html", context)
