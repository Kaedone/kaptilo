from django.shortcuts import render, redirect
from django.contrib import auth, messages
# Create your views here.
from core import forms
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request, 'homepage.html', {})


def logout(request):
    auth.logout(request)
    return redirect('homepage')


def create_link(request):
    content = {}
    if request.method == 'POST':
        pass
    else:
        content = {'form': forms.LinkForm()}
    return render(request, 'create_link.html', content)


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
