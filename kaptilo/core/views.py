from django.shortcuts import render

# Create your views here.


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
        content = {'form': LinkForm()}
    return render(request, 'create_link.html', content)