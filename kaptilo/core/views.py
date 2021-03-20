from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.


def homepage(request):
    return render(request, 'homepage.html', {})


def logout(request):
    auth.logout(request)
    return redirect('homepage')

