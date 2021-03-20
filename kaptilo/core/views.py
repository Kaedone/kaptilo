from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
from core import forms


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
    form = forms.LoginForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)

