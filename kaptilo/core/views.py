from django.shortcuts import render
from .forms import *

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html', {})


def create_link(request):
    content = {}
    if request.method == 'POST':
        pass
    else:
        content = {'form': LinkForm()}
    return render(request, 'create_link.html', content)